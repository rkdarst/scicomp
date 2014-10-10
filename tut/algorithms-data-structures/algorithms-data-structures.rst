

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




Examples
~~~~~~~~


Introduction to computational complexity

Step 1: understand O() of all algorithms

Have two sample programs and profile them.



..


copying numpy arrays
