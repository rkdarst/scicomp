==================
Profiling software
==================


Scientists "know" that faster programs is better.  But what does this
mean?

First, you will usually be spending more time writing programs than
running them.  All the previous talks optimize writing, debugging,
collaborating, and maintaining programs and is the most important
thing you can do.

But as for optimizing program speed, there is one saying you see
everywhere: **Premature optimization is the root of all evil**.  This
means, first you want to make a *good* program, then *profile* it to
see where the slow parts are, then *optimize just those parts*.  This
talk is about **profiling: the process of systematically examining
program execution times to learn the bottlenecks**





Profiling software
~~~~~~~~~~~~~~~~~~


Outline
~~~~~~~

- What is profiling?

- How to generate profiles

- How to read and use profiles to improve your code


Profiling and optimizing
~~~~~~~~~~~~~~~~~~~~~~~~

- **Profiling**: A form of dynamic program analysis that measures resource
  usage of a program.

- **Optimizing**: Improving your code so that it is faster (or uses
  less memory, or...)

- Faster is better.  But remember writing code can be the slowest
  part.

- 10% of code is 90% of run time:

  - You only want to optimize that 10%, but what 10% is it?


There is a famous saying:

  **Premature optimization is the root of all evil** - Donald Knuth, 1974

.. epigraph::

   What this saying means is that you should not try to optimize your
   program before writing it.  Programs are very complex interactions
   between processor architectures, memory, multiple layers of caches,
   compilers, and the instructions themselves.  If you try to guess
   where the slow part is, you will probably get it wrong and end up
   wasting your time.  Worse yet, you will end up having unreadable
   and unmaintainable optimized code, and end up working slower in the
   future.





Profiling
~~~~~~~~~

Wikipedia: **Profiling** is dynamic program analysis of time, space, or
other resource usage.

- This talk focuses mostly on *time profiling*.

- Profiling will help us find **bottlenecks** in the code, that use up
  most of the time.

  - Computers and programs are very complex, with many subtleties in
    processor pipelines, caches, compiler optimizations, and so on.

  - It is hard to predict the slowest part of code, even for experts.
    **This is the point of profiling first, then optimizing**.

What you can't see, you can't improve.  Just like in science.


Level 0 profiling: timing code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* On Linux, anything can be run using the ``time`` shell utility

  .. console::

     $ time ./research-code -x 1 InFile1

     real    16m37.055s
     user    6m13.786s
     sys     1m25.012s

* This tells you how much total time a program took (divided into
  user and system call time)

* We have no idea how that time was divided up in the program.  Can we
  do better?

Some nomenclature
~~~~~~~~~~~~~~~~~

- **Total time**: time spent in a function itself.

  - Tells you that *the code in this function* is taking a lot of time.

- **Cumulative time**: time spent in a function and all functions it
  called.

  - Tells you that *this function* is taking a lot of time.  Perhaps
    it is calling other functions unnecessarily.

- **Callers**: functions which called some function.

- **Callees**: functions which some function calls.



Example from my work
~~~~~~~~~~~~~~~~~~~~

.. image:: profiling/profile-growsf-zoom.png
   :alt: Example of gprof2dot profile.  Click for full image.
   :target: profiling/profile-growsf.png
   :height: 5cm
   :align: right

- A profile contains detailed information on run time at the level of
  functions or lines of code.

- Call graph: directed graph showing how functions call each other.

  - They can include time information

- The image linked here is an example of a profile call graph from my
  work.  Let's examine it.


.. epigraph::

   We find one slow branch that takes most time.  To optimize, we
   focus only on that branch.

   This is a directed graph showing the flow of time through the
   program.  At the top is the entry point, and looking down you see
   the flow of time (in fraction of total time) distributed among all
   functions.  Colors serve as a visual aid to see where the hot spots
   are.  Arrows point from callers to callees, and include number of
   times called.

   This is not "a profile".  This is one representation of a profile.



Example: profile before and after optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here, you see two call graphs: before and after optimization.

.. image:: profiling/profile-temporal-2-pre.png
   :alt: Call graph before optimizing
   :target: profiling/profile-temporal-2-pre.png
   :height: 5cm

.. image:: profiling/profile-temporal-2-post.png
   :alt: Call graph after optimizing
   :target: profiling/profile-temporal-2-post.png
   :height: 5cm

- What I actually changed: I realized my caching was not working and
  it was generating some data too many times.  I fixed that

- Then,  notice that the "hot" branch slows becomes less important, and we
  see that its importance greatly decreases, and many other branches
  appear.  By default ``gprof2dot`` has a node time threshold of 0.5%.

.. epigraph::

   Profile sources: `before <profile-temporal-2-pre.prof>`_ and `after
   <profile-temporal-2-post.prof>`_.





Example: calling external processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: profiling/profile-external.png
   :alt: Call graph after optimizing
   :target: profiling/profile-external.png
   :height: 5cm

Profile source: `profile-external.out <profile-external.out>`_

.. epigraph::

   On the left of this figure, we see various external community
   detection methods running using the ``subprocess`` module.

Example: using a library for work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: profiling/profile-dynsnap-1.png
   :alt: Call graph after optimizing
   :target: profiling/profile-dynsnap-1.png
   :height: 5cm



How to collect the profiling data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Step 1: Have a good, clean program that works correctly.

- Step 1.5: Have a reproducible function or script to run

  - Fast, and demonstrates the bottlenecks

- Ways to collect the data

  - Run program, immediately prints some statistics

  - Run program, profiling data is saved to another file.  Analyze
    file later.

  - As part of Integrated Development Environments.

.. epigraph::

   Remember, the whole point of this is that you should write good
   programs first, and then profile.  Of course, sometimes you will
   profile during development, but don't go crazy sacrificing
   readability for optimizations.  Chances are that will be refactored
   out later anyway.


Collecting profiling information: C
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To do the most basic ``C`` profiling, we need to compile with special
options in order to **instrument** the code.

- Compile with the ``-g -pg`` options.

- Run code normally: ``./a.out``

- A file ``gmon.out`` is created with profiling information

- Examine timings with ``gprof``

  .. console::

     $ gprof a.out gmon.out




Collecting profiling information: Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the first step, we run the program using the ``cProfile`` module.
This just stores up the profile information, and we will examine it in
the next step.

* Run your script under control of the ``cProfile`` module:

  .. python::

     $ python -m cProfile -o profile.out  SCRIPT.py arg1 arg2 ....

* ``python -m cProfile``: Run library module ``cProfile`` as a script.

* ``-o profile.out``: Tells ``cProfile`` to write the profile to the
  file ``profile.out``.

* ``SCRIPT.py arg1 arg2 ...``: Your normal ``python`` interpreter arguments.

* The output ``profile.out`` contains details of all function calls
  and times.

The next step is to visualize or analyze the data in ``profile.out``.

.. epigraph::

   I personally prefer first running and storing the profile in
   ``profile.out``, and then visualizing, to be better.  If the call
   graph is not useful enough, I can visualize it again using
   different options or examine it using the command line for more
   details.  Also, if I make a change, I can compare the new and old
   profiles to see how it affected things.  This is important!

   ``python -m MODULE`` is the same as "python /path/to/the/MODULE.py".
   It is a common shortcut.

   This step works on any platform.

   Sample output: `profile-growsf.out <./profile-growsf.out>`_

Viewing profile information: Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* There is a simple interactive browser for the profile information

  .. console::

     $ python -m pstats profile.out

* Key commands to run:

  - ``strip``: strip out unnecessary information (full file paths)

  - ``sort [time|cumulative]``: cumulative

  - ``stats N``: print out the top ``N`` stats.

..
    Example: IDE
    ~~~~~~~~~~~~
    - Profiling can be run directly from integrated development
      environments


What can be profiled?
~~~~~~~~~~~~~~~~~~~~~
- Entire operating systems
- Microchips
- Mobile devices
- Web browser rendering
- Human behavior...
- ...


Exercises: Hands-on profiling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. role:: c
    :class: red

.. role:: py
    :class: blue

- The following exercises will guide you through profiling yourself.

- There are examples in :py:`Python` and :c:`C`.


Exercise Profiling-1.1: Running code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. First, we just need to run some code and collect profiling
   information.  Then we will process it to get information.  The
   first examples will be *console based*, not graphical like I showed
   you above.  A console-based profile shows the same information and
   is good for computers like Triton.

   The examples are in the ``/triton/scip/profile`` directory.

#. :c:`For C, you need to compile your code with an option to enable
   profile generation.  This adds an extra overhead, so is not enabled
   by default.  The flag is` ``-pg`` for ``gcc``.

   .. console::

      $ gcc -g -pg c-profiling.c

#. Run your code.  :c:`For C, just run it like normal and you will get
   a` ``gmon.out`` :c:`file that has the profiling data`.

   .. console::

      $ ./a.out

   :py:`For python, you don't need to recompile, but you need to tell
   a profile to trace everything.  We do this by running with the`
   ``cProfile`` :py:`module and saving the output to` ``profile.out``.

   .. console::

      $ python -m cProfile -o profile.out py-profile.py

#. You should now either have a ``gmon.out`` or ``profile.out`` file
   in this directory.  This contains all your profiling information.
   Next we just have to look inside.


Exercise Profiling-1.2: Getting profile information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. We look at the profiling information in two ways.  For :c:`C, you
   use gprof to do this` and for :py:`Python you use the pstats
   module`.

#. C: We use the ``gprof`` utility to study the output.  Run it like this:

   .. console::

      $ gprof a.out gmon.out

   It directly prints out a summary report.  You may need to scroll up
   some in order to see the important timing parts

#. Python: There is a interactive profile viewer in the ``pstats``
   module.  Open it using ``-m pstats``, and then execute the commands
   ``strip``, ``sort cumulative``, and ``stats 15`` to print the data.  You
   can use different

   .. console::

      $ python -m pstats profile.out
      strip
      sort cumulative
      stats 15

Exercise Profiling-1.3: Examining the output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Now that we have the profiling information, let's examine what is
   in it.

#. Which function takes the most time?

#. Which function, when also considering sub-functions, take the most
   time?

..
  FIXME: Examples that depend on both total time and cumulative time.  


..
    Exercise Profiling-1.4: Bonus: More fancy visualization
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #. You can make nice call graphs like you saw earlier.  This is done
       via the ``gprof2dot.py`` script, which is already in the
       ``scip/profiling/`` folder.

    ..
      FIXME: Demonstrate use of gprof2dot.py






What to look for in a profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- What functions take most time?

- Who calls the functions that take most time?  Often, the actual
  critical function is several steps up.

- (in Python) some C-implemented functions or methods do not appear.

- You generally want to find things that are surprising: that are
  using lots of time but *shouldn't* be major operations.  You want
  the actual computation part to take most of the time.

- Each time you improve some things, re-generate the profile to see
  changes.

.. epigraph::

   There are also tools for line-based, instead of function-based,
   profiling.  However, due to the overheads of Python it's not common
   there.

   I don't have magic suggestions on how to improve things.  After
   seeing enough profiles, and a future optimization talk, you will
   gain intuition on how to do things.  Most importantly, by examining
   profiles before and after your changes, you will be in a position
   to know what works and what doesn't.


Optimizing
~~~~~~~~~~
- Generally, you will use your profile to improve you code

- But, speed is an interaction of many things on your computer

- In the second half of this day, you will cover all sorts of
  optimization considerations.



Exercise Profiling-2.1: Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. In this set of exercises, we will go through the optimization of a
   program.  We will look at the profile, see where the slow parts
   are, improve those parts, and see how the profile changes.

#. There is a Python code for calculating :math:`\pi` using a simple
   Monte Carlo method at ``/triton/scip/profile/pi.py``.  Copy this to
   your working directory.  This code takes one command line argument, the number
   of iterations.  Run the code in the console, just using the
   ``time`` command line utility to see how long it takes.

   .. console::

      $ time python pi.py 1000000
      3.141936
      time elapsed: 1.6  per iteration: 1.6e-06

      real    0m1.634s
      user    0m1.579s
      sys     0m0.055s


Exercise Profiling-2.2: Profiling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Run this code and generate a profile in the shell. and generate the
   ``pi-profile-1.out`` (note the number 1):

   .. console::

      $ python -m cProfile -o pi-profile-1.out pi.py 1000000

   Write down the total time.

#. Use pstats to try to figure out what functions take the most time:

   .. console::

      $ python -m pstats profile.out
      strip
      sort time
      stats 5

   You see that ``get_coords`` takes up most of the time.  Then sort
   by cumulative time and see what the difference is:

   .. console::

      sort cumulative
      stats 5

#. Bonus/optional: Generate a ``gprof2dot`` picture of this for future
   reference.  Copy ``gprof2dot`` from the ``/triton/scip/profile``
   directory.

   .. console::

      $ python gprof2dot.py -f pstats pi-profile-1.out | dot -Tpng > pi-prof-1.png

Exercise Profiling-2.3: Improving based on the profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. We saw that the function ``get_coords`` took most of the time.
   Luckily, I have already programmed a new version of this, called
   ``get_coords_numpy``.  Change the call of ``get_coords`` to
   ``get_coords_numpy``::

     x, y = get_coords(N)    --->    x, y = get_coords_numpy(N)

#. Re-run the profile, saving as ``pi-profile-2.out``.  View it in the pstats viewer.  You see that
   get_coords is so fast that it doesn't show up anymore.  Now, the
   function ``circle_count`` takes up most of the time.

#. Bonus: In fact, you notice that the total time of ``circle_count`` went
   up.  Why do you think that is?

#. Bonus: Make another ``gprof2dot`` picture of this for future reference.

   .. console::

      $ python gprof2dot.py -f pstats pi-profile-2.out | dot -Tpng > pi-prof-2.png

Exercise Profiling-2.4: More improvement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Repeat all of the same things as above, but replace the function
   ``circle_count`` with the function ``circle_count_numpy`` since
   this is the new bottleneck.  Remember to save as
   ``pi-profile-3.out``.  How much faster do things get?

#. Bonus: Save a ``gprof2dot`` image again.

   .. console::

      $ python gprof2dot.py -f pstats pi-profile-3.out | dot -Tpng > pi-prof-3.png

Exercise Profiling-2.4: What happened?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Now that we are done, we will look at all the ``gprof2dot``
   pictures we have made.  This allows us to quickly compare the
   different runs.

   For convenience, my own copy of the pictures are here:

   - `Original <profiling/pi-prof-1.png>`_
   - `With get_coords_numpy <profiling/pi-prof-2.png>`_
   - `With circle_count_numpy <profiling/pi-prof-3.png>`_

#. What is the slowest in #1?  What is the difference between #1 and
   #2?

#. What is the slowest function in #2?  What is the difference between
   #2 and #3?

#. ``gprof2dot`` thresholds and only shows nodes with greater than
   0.5% of the total time.  Why do lots of other functions start
   appearing in #3?  Are these a concern in practice?


..
    Exercise Profiling-2.4: Bonus: Line profiling
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Exercise Profiling-2.5: Bonus: Memory profiling
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Exercise Profiling-2.6: Bonus: Line counting with ``gcov``
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Stochastic vs instrumenting profiling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Instrumenting profiling**: Trace every function execution and
  return and record all times.

  - Introduces overhead in *every* function call.

  - More accurate in that it records every function call.

- **Statistical profiling**: At random intervals, record the program's
  call stack.

  - Less overhead in the execution.

  - More accurate in that it won't affect the runtime so much.

  - ``perf`` is a suite that can do this.

.. epigraph::

   Everything in this talk uses instrumenting profiling, and probably
   it is the main thing you will use.  However, you should know that
   there is a wide variety of techniques behind profiling, including
   some serious tools for dynamic program analysis.  If you ever have
   a program with mainly small, fast function calls, consider
   stochastic profiling.


How to read profiles
~~~~~~~~~~~~~~~~~~~~
How do each of these profile items interact:

- Call counts
- Cumulative time
- Total time
- Callers/Callees and their time



Advanced profiling techniques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* **Line-profiling**: track timings at a line level
* **Memory profiling**: memory usage, cache hits/misses
* **Input/Output profiling**: disk access...


Conclusions
~~~~~~~~~~~

- You *must* know what is happening inside your code before you can optimize.

- Profiling provides a detailed insight into time and memory usage.

- Call graphs represent the flow of time through your program.

- When optimizing, focus on a bottleneck, improve it, then repeat.


The end
~~~~~~~



































..
    How to use your profile: Actually optimizing your code
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - This tutorial does *not* talk about optimizing, the process of actually
      making these things go faster (that's a future tutorial!).

    - Rough suggestions:

      - Try different methods for calculating stuff.

      - Add a caching layer to save computing things over and over.  Use
	dictionaries well.

      - Algorithmic improvements (future talk).  If possible, it's best to
	replace, not rewrite, these parts.

      - Move just the slow part to C.

    - There are some optimization resources at the end of this talk.

..
    Other profiling tools
    ~~~~~~~~~~~~~~~~~~~~~

    - pycallgraph (produces .png directly from running program)

    - ``runsnakerun``: simple area-based view, for Python.

    - ``oprofile`` - system-wide statistical profiler.

    - Memory profiling in Python: Meliae: https://launchpad.net/meliae

    .. epigraph::

       ``oprofile`` is a neat kernel-based profiler.  It can profile
       everything on your system, and make line-based profiles.  (Example
       `line profile <oprofile_annotate_APM>`_ and `summary report
       <oprofile_report_APM>`_)

       Memory profiling is tricky in Python.  Since objects have shared
       ownership, you can't tie them to specific locations in code so
       easily.  I have rarely needed to use memory profiling in Python.


Resources
~~~~~~~~~

- Profiling in general

  - https://en.wikipedia.org/wiki/Profiling_%28computer_programming%29

- Python tools

  - http://docs.python.org/2/library/profile.html

  - https://code.google.com/p/jrfonseca/wiki/Gprof2Dot (also has
    instructions for other languages)

  - http://www.vrplumber.com/programming/runsnakerun/

  - Python line profiler https://pypi.python.org/pypi/line_profiler/
    (`source <https://github.com/rkern/line_profiler>`_)

- Optimization of Python

  - https://wiki.python.org/moin/PythonSpeed

  - https://wiki.python.org/moin/PythonSpeed/PerformanceTips

  - https://wiki.python.org/moin/TimeComplexity

  - http://wiki.scipy.org/PerformancePython - moving slow parts into numpy/C

- Other tools/languages

  - gprof: http://www.cs.utah.edu/dept/old/texinfo/as/gprof.html

  - Valgrind (huge dynamic program analysis tool): http://valgrind.org/


Matlab
~~~~~~
- Reference: http://se.mathworks.com/help/matlab/ref/profile.html

- Tutorial: http://se.mathworks.com/help/matlab/matlab_prog/profiling-for-improving-performance.html

- Example:

  ::

     profile on
     # Code to be profiled here
     profile viewer   # stop profiler, view it

     p = profile('info');
     profsave(p,'profile.html')


Line profiling in Python
~~~~~~~~~~~~~~~~~~~~~~~~

- There is a package ``line_profiler``: https://github.com/rkern/line_profiler

- There is a *lot* of overhead, so you must specify which functions to
  profile!

- Run program with ``kernprof.py``

  .. code:: console

     $ kernprof -l program.py

- Decorate functions to profile

  .. python::

     @profile
     def bottleneck_function(...):
         ....
         ....

- ``IPython``: ``%lprun`` magic command.


Memory profiling in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~

- RAM usage takes time.  Reduce memory usage to improve performance
  (and scale up).

- Heapy:

  .. python::

     from guppy import hpy
     h = hpy()
     print h.heap()

- ``memory_profiler``

  - Line-by-line profiling, of *increase of* memory usage

  .. code:: console

     python -m memory_profiler example.py

  .. python::

     @profile
     def bottleneck_function(...):
         ....
         ....

