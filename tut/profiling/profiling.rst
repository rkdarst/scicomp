


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



Using pstats directly
~~~~~~~~~~~~~~~~~~~~~

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
Better tutorial: 


Extensions to profiling
~~~~~~~~~~~~~~~~~~~~~~~

- Line-based profiles



Part 2: Algorithms and data structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you know which functions (or lines) are slow what do you do?

- This is where you **optimize** to make these parts (and only these
  parts) faster.

- However, optimization is pointless until you are using the best
  algorithms and data structures for the job.

- That is what this part is about.



Time complexity in python data structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Time complexity**: Time needed to complete an operation or
  algorithm as a function of the input size.

- Expressed as a scaling: ``O(1)``, ``O(N)``, or ``O(N*k)``, for example.

.. python::
    n = 100
    L = range(n)
    S = set(L)

    %timeit n//2 in L
    %timeit n//2 in S

=====  =====  =====  ======  ========
\      n=1    n=10   n=100   n=1000
=====  =====  =====  ======  ========
list   181ns  289ns  1270ns  11000ns
set    202ns  202ns  203ns   235ns
=====  =====  =====  ======  ========

.. epigraph::
   Different implementations have different constanst: ``c*O(n)``.
   These constants can matter, but generally the ``O(*)`` matters more
   for initial design.



Time complexity of Python data structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full story: https://wiki.python.org/moin/TimeComplexity

- Lists: O(1) appending, indexing, length

- Dicts/sets: O(1) lookup, ``in`` operator, addition, and removal.

- numpy arrays: O(n) for all operations, but very low constants.

- ``collections`` module

  - deque: O(1) append, appendleft, pop, popleft, O(n) selecting from
    middle.

.. epigraph::
   "Slow" code using O(1) operations is better than "fast" code using
   O(n) or worse operations.



Use the short constants built into data structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``O(1)`` operations are great, but you usually have to loop over
things, sometime.

- Improve the innermost loop first.  That is probably all you need.

- If you have to do math, use numpy arrays, not lists.

- Using internal python operations better than doing it explicitly:

  .. python::

      [ (a+b) for a,b in zip(A, B) ]

  vs

  .. python::

     L = [ ]
     for a, b in zip(A, B):
         L.append(a+b)

.. epigraph::

   This is the realm of optimizing.  We will discuss this later.



Good algorithms are more important than any optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Conclusions
~~~~~~~~~~~



What do we want to talk about next?


Examples
========


Introduction to computational complexity

Step 1: understand O() of all algorithms

Have two sample programs and profile them.



..


copying numpy arrays
