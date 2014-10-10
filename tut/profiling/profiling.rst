Profiling, algorithms, and optimization
=======================================




Summary of this talk
~~~~~~~~~~~~~~~~~~~~

- Profiling

  - Seeing what takes a long time.

- Algorithms and data structures

  - Making your program have a chance of being "fast"

- Optimization

  - Techniques to make your thing actually run faster

  - The least important of everything on this page


Premature optimization is the root of all problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

My traditional approach:

- Think about the problem and find the best algorithm for it.

- Write your code as beautifully and extensible as possible.

- If it's slow, profile and find exactly what lines or functions are
  slow.

- Usually, there will be something obvious to do to speed up that
  little bit.



Profiling
~~~~~~~~~

Wikipedia: **Profiling** is dynamic program analysis of time, space, or
other resource usage.

- This talk focuses exclusively on *time profiling*.

- Profiling will help us find **bottlenecks** in the code, that use up
  most of the time.

- Computers and programs are very complex, with many subtleties in
  processor pipelines, caches, compiler optimizations, and so on.

  - The actual program speed *can't* always be easily predicted from
    the code itself!  **This is the point of profiling first, then
    optimizing**.


Types of profiling
~~~~~~~~~~~~~~~~~~

- **Deterministic profiling**: Trace every function execution and
  return and record all times.

  - Introduces overhead in *every* function call.

  - More accurate in that it records every function call.

- **Statistical profiling**: At random intervals, record the program's
  call stack.

  - Less overhead in the execution.

  - More accurate in that it won't affect the runtime so much.


Deterministic profiling with gcc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compile with ``gcc -pg``

- This compiles the code to output profiling data when run (adds hooks
  for profiling)

- Different compilers can have different options.

Run the program as normal

- Makes a file ``gmon.out`` with the profiling data.

View it with ``gprof``: ``gprof a.out gmon.out``


Example profile output
~~~~~~~~~~~~~~~~~~~~~~

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



Deterministic profiling with Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First compile it:

.. python::

   $ python -m cProfile -o profile.out  SCRIPT.py arg1 arg2 ....

- ``python -m cProfile``: Run library module ``cProfile`` as a script.

- ``-o profile.out``: Tells ``cProfile`` to write the profile to the
    file ``profile.out``.

- ``SCRIPT.py arg1 arg2 ...``: Your normal ``python`` interpreter arguments.

- The contents of ``profile.out`` is every function call and return.

The next step is to visualize or analyze the data in ``profile.out``.



Python profiles with ``gprof2dot.py``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``gprof2dot.py`` is a call graph visualizer.  I have found it very
  robust.

- It takes the ``profile.out`` and converts it to a call graph in the
  ``graphviz`` language, which can then be visualized or analyzed in
  different ways.

- My usage:

  .. code:: console

     $ python gprof2dot.py -f profile.out | dot -Tpng | display

  This creates and displays the PNG all in a pipe.

- Multi-language and configurable.

- Source (single script file) and help:
  https://code.google.com/p/jrfonseca/wiki/Gprof2Dot

Example output:

.. image:: profile-growsf-zoom.png
   :alt: Example of gprof2dot profile.  Click for full image.
   :target: profile-growsf.png
   :height: 5cm



Things to examine in the profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- What functions take most time?

- Who calls the functions that take most time?  Often, the actual
  most important function is several steps up.

- C-implemented functions or methods do not appear.

- You generally want to find things that are using lots of time but
  *shouldn't* be major operations.

- Each time you improve some things, re-generate the profile to see
  new hotspots.

- Threads or multi-processes take more work (they won't appear in
  traces by default)!



Advanced: using pstats directly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can examine the raw ``profile.out`` data using the command line:

.. code:: console::

   $ python -m pstats profile

Available commands:

strip
    shorten filenames (recommended)
sort [ time | cumtime ]
    sort the data by time or cumulative time
print 15
    print first 15 entries
callees [funcname]
    Print functions which ``funcname`` called and time spent in each -
    *only* time spent in direct calls from ``funcname``

callers [funcname]
    Print functions which called ``funcname`` and how much time was
    spent in calls from each function.


Reference: https://docs.python.org/2/library/profile.html
Better tutorial: ???




Other programs and extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- pycallgraph (produces .png directly from running program)

- Line-based profiles

- ``runsnakerun``: simple area-based view.

- ``oprofile`` - system-wide statistical profiler.

- Memory profiling in Python: Meliae: https://launchpad.net/meliae









Conclusions
~~~~~~~~~~~



What do we want to talk about next?


