Profiling, algorithms, and optimization
=======================================


Scientists "know" that faster programs is better.  But what does this
mean?

First, most of the time you will spend more time writing programs than
running them.  All the previous talks optimize writing, debugging,
collaborating, and maintaining programs and is the most important
thing you can do.

But as for optimizing program speed, there is one saying you see
everywhere: **Premature optimization is the root of all evil**.  This
means, first you want to make a *good* program, then *profile* it to
see where the slow parts are, then *optimize just those parts*.  This
talk is about **profiling: the process of systematically examining
program execution times to learn the bottlenecks**





Outline
~~~~~~~

- What is profiling?

  - Real example: profile and call graph

- How to generate profiles

- What to look for

- Advanced tools and tips

- "Optimizing"





Profiling and optimizing
~~~~~~~~~~~~~~~~~~~~~~~~

- **Profiling**: A form of dynamic program analysis that measures time
    (or space) usage of a program.

- Faster is better.  But what part is slowest?
  - Usually writing, debugging, collaborating, maintaining.

- 10% of code is 90% of run time.
  - You only want to work on that 10%, but what 10% is it?

Famous saying:

  **Premature optimization is the root of all evil**

.. epigraph::

   What this saying means is that you should not try to optimize your
   program before writing it.  Programs are very complex interactions
   between processor architectures, memory, multiple layers of caches,
   compilers, and the instructions themselves.  If you try to guess
   where the slow part is, you will probably get it wrong and end up
   wasting your time.





Example from my work
~~~~~~~~~~~~~~~~~~~~

- Call graph: directed graph showing which functions call which.  Can
  also have time information associated with it when profiling.

- The image linked here is an example of a profile call graph from my
  work.  Let's examine it.

Example output (click link):

.. image:: profile-growsf-zoom.png
   :alt: Example of gprof2dot profile.  Click for full image.
   :target: profile-growsf.png
   :height: 5cm





Profiling
~~~~~~~~~

Wikipedia: **Profiling** is dynamic program analysis of time, space, or
other resource usage.

- This talk focuses exclusively on *time profiling*.

- Profiling will help us find **bottlenecks** in the code, that use up
  most of the time.  We then work on the code around the bottleneck.

- Computers and programs are very complex, with many subtleties in
  processor pipelines, caches, compiler optimizations, and so on.

- The actual program speed *can't* always be easily predicted from
  the code itself!  **This is the point of profiling first, then
  optimizing**.





How to make the profile
~~~~~~~~~~~~~~~~~~~~~~~

- Step 1: have a good, clean program that works correctly.

- In this example I assume you have a normal command line program.





Generating profiling information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We run the program under the ``cProfile`` module.

.. python::

   $ python -m cProfile -o profile.out  SCRIPT.py arg1 arg2 ....

- ``python -m cProfile``: Run library module ``cProfile`` as a script.

- ``-o profile.out``: Tells ``cProfile`` to write the profile to the
    file ``profile.out``.

- ``SCRIPT.py arg1 arg2 ...``: Your normal ``python`` interpreter arguments.

- The output ``profile.out`` contains details of all function calls
  and times.

The next step is to visualize or analyze the data in ``profile.out``.

.. epigraph::

   Sample output: `profile-growsf.out <./profile-growsf.out>`_





Visualizing the profile information (gprof2dot)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``gprof2dot.py`` is a call graph visualizer.  It is my go-to tool.

- It takes the ``profile.out`` and converts it to a call graph in the
  ``graphviz`` language, which can then be visualized or analyzed in
  different ways.  You then use graphviz (``dot``) to make a picture.

- This command runs everything and displays the output.

  .. code:: console

     $ python gprof2dot.py -f profile.out | dot -Tpng | display

  This creates and displays the PNG all in one go.

- Source (single script file) and help:
  https://code.google.com/p/jrfonseca/wiki/Gprof2Dot

Example output (click link):

.. image:: profile-growsf-zoom.png
   :alt: Example of gprof2dot profile.  Click for full image.
   :target: profile-growsf.png
   :height: 5cm



Some nomenclature
~~~~~~~~~~~~~~~~~

- Total time: time spent in a function itself.

  - Tells you that *the code in this function* is taking a lot of time.

- Cumulative time: time spent in a function and all functions it
  called.

  - Tells you that *this function* is taking a lot of time.  Perhaps
    it is calling other functions unnecessarily.

- Callers: functions which called some function.

- Callees: functions which some function calls.




What to look for in a profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- What functions take most time?

- Who calls the functions that take most time?  Often, the actual
  critical function is several steps up.

- (Python) C-implemented functions or methods do not appear.

- You generally want to find things that are surprising: that are
  using lots of time but *shouldn't* be major operations.  You want
  the actual computation part to take most of the time.

- Each time you improve some things, re-generate the profile to see
  new hotspots.

- Threads or multi-processes take more work (they won't appear in
  traces by default)!

.. epigraph::

   Line-based profiling?





Example: profile before and after optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here, you see two call graphs: before and after optimization.

.. image:: profile-temporal-2-pre.png
   :alt: Call graph before optimizing
   :target: profile-temporal-2-pre.png
   :height: 5cm

.. image:: profile-temporal-2-post.png
   :alt: Call graph after optimizing
   :target: profile-temporal-2-post.png
   :height: 5cm

- What I actually changed: I realized my caching was not working and
  it was generating some data too many times.

- Notice that the "hot" branch slows becomes less important, and we
  see the rest of the branches appear.




Advanced
~~~~~~~~




Examining profile.out from the command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can examine the raw ``profile.out`` data using the command line,
without making a picture.

.. code:: console::

   $ python -m pstats profile

   % strip           # make output names shorter
   % sort time       # Sort by time
   % stats 15        # Print top 15 lines

Output::

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1000020  119.340    0.000  134.635    0.000 cluster.py:59(_triangles_and_degree_iter)
       21   53.178    2.532   53.178    2.532 {time.sleep}
      381   18.685    0.049   18.685    0.049 {cPickle.loads}
       20    9.450    0.473   13.629    0.681 cmtyembed.py:67(nembed_m)
 10999400    7.203    0.000    7.203    0.000 graph.py:294(__getitem__)



Available commands:

strip
    shorten filenames (recommended)
sort [ time | cumul | other ]
    sort the data by total time, cumulative time, or any of the options.
print N
    print first N entries
callees [funcname]
    Print functions which ``funcname`` called and time spent in each -
    *only* time spent in direct calls from ``funcname``

callers [funcname]
    Print functions which called ``funcname`` and how much time was
    spent in calls from each function.


Reference: https://docs.python.org/2/library/profile.html
Better tutorial: ???





Profile C code (and other languages)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any decent language will have profiling facilities.

- Compile with ``gcc -pg``

  - This compiles the code to output profiling data when run (adds hooks
    for profiling)

  - Different compilers can have different options.

- Run the program as normal

  - You will then find a file ``gmon.out`` with the profiling data.

- View it with ``gprof``: ``gprof a.out gmon.out``.  The interface is
  like the Python command-line profiling.






gprof example profile output (C code)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. pyinc:: c c-profiling.c

Output::

    %   cumulative   self              self     total
   time   seconds   seconds    calls  us/call  us/call  name
  101.15      0.62     0.62    30000    20.57    20.57  y
    0.00      0.62     0.00    10000     0.00    41.13  f

% time
  Self explanatory, fraction of time in this function.

self seconds
  Seconds spent in this functions code.

total seconds
  Seconds spent in a function *and functions called by this function*.

.. epigraph::

   "Self seconds" and "total seconds" serve complimentary purposes.
   "Self seconds" is where the time is spent, "total seconds" tells
   you tree branches that took a lot of time.





Stochastic vs deterministic profiling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Deterministic profiling**: Trace every function execution and
  return and record all times.

  - Introduces overhead in *every* function call.

  - More accurate in that it records every function call.

- **Statistical profiling**: At random intervals, record the program's
  call stack.

  - Less overhead in the execution.

  - More accurate in that it won't affect the runtime so much.

  - ``oprofile`` is a suite (with Linux kernel module) that can do
    this on already running code (C only).

.. epigraph::

   Everything in this talk uses deterministic profiling, and probably
   it is the main thing you will use.  However, you should know that
   there is a wide variety of techniques behind profiling, including
   some serious tools for dynamic program analysis.  If you ever have
   a program with mainly small, fast function calls, consider
   stochastic profiling.





Other profiling tools for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- pycallgraph (produces .png directly from running program)

- Line-based profiles

- ``runsnakerun``: simple area-based view.

- ``oprofile`` - system-wide statistical profiler.

- Memory profiling in Python: Meliae: https://launchpad.net/meliae





Profiling from the Python shell (and ipython)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To profile something from the Python shell, or only one function
within a program:

.. code::

   import cProfile
   cProfile.run('func()', 'filename.out')

- Stores pstats output in ``filename.out`` for examination in other
  programs.  Leave off filename argument to just print it.


IPython has a shortcut for running this.  I would usually save it to
another file and visualize with ``gprof2dot.py``.

.. code::

   %prun [-s sort-key] [-D filename.out]  [statement]

- Prints a profile to the screen.  With -D, save the standard pstats
  output for visualization in gprof2dot or other programs.





How to use your profile: Actually optimizing your code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This talk does *not* talk about optimizing, the process of actually
  making these things go faster.

- Rough suggestions:

  - Try different methods for calculating stuff.

  - Find functions that are called more times than needed and add caching?

  - Algorithmic improvements (future talk).

  - Move just the slow part to C.

- There are some optimization resources at the end of this talk.





Conclusions
~~~~~~~~~~~

- Premature optimization is the root of all evil.

- Profile before you optimize.

- Call graphs represent the flow of time through your program.

- This talk does *not* talk about optimizing itself.




Resources
~~~~~~~~~

- Profiling

  - https://en.wikipedia.org/wiki/Profiling_%28computer_programming%29

- Other languages


- Optimization

  - https://wiki.python.org/moin/PythonSpeed

  - https://wiki.python.org/moin/PythonSpeed/PerformanceTips

  - https://wiki.python.org/moin/TimeComplexity

  - http://wiki.scipy.org/PerformancePython - moving slow parts into numpy/C

