Algorithms and data structures
==============================


..

    P art 2: Algorithms and data structures
    ~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Once you know which functions (or lines) are slow what do you do?

    - This is where you **optimize** to make these parts (and only these
      parts) faster.

    - However, optimization is pointless until you are using the best
      algorithms and data structures for the job.

    - That is what this part is about.




Why are algorithms important?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Once I was given a program in C, a "fast" language.

* I re-wrote it in Python, a "slow" language.

* My Python code was faster, for large networks.

Why was this?  The Python code used better algorithms.



Another example: graph representations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Methods of storing a graph with ``N`` nodes:

 * Matrix

 * List of lists

* How long does it take to compute the number of edge in the graph?

  * Matrix: have to look at ``N*N`` elements.

  * List of lists: have to take ``len()`` of ``N`` lists

* The lists of lists is clearly much faster in computing



Big-O notation
~~~~~~~~~~~~~~

Expressing "speed" and memory usage of algorithms?

* **Big-O notation**: used to classify algorithms by how they
    respond (processing time or memory requirements) to changes in
    input size.

* Important since scientists tend to want to process bigger data.

* "time ``O(N^2)``" means "time to run is proportional to ``N^2``",
  ``N`` is some property of the input

  * ``N`` can be different parameters, e.g. array size, number of
    records, number of nodes.

  * Can be combined: ``O(N*m)``

* We do not care about constant factors.


Big-O example
~~~~~~~~~~~~~

This is ``O(N)``:
.. code::

   for i in range(N):
       pass

This is ``O(N)``:

.. code::

   for i in range(N):
       for j in range(N):
           pass

How to calculate big-O: multiply sizes of all loops and the inner
statements.

.. epigraph::

   ``pass`` is a single statement (that does nothing), so is O(1), the
   best possible.

   ``for i in range(N):`` does the loop ``N`` times.



Data structures
~~~~~~~~~~~~~~~

* Algorithms are intrinsically tied to data structures.

* This talk will focus on *time complexity of data structures*.

Example:

.. python::

   lst = range(10000)
   lst.append(5)        # time complexity O(1)
   list.insert(0, 5)    # time complexity O(N)

If your list is big, you do **not** want to be doing the second one!

.. epigraph::

   This talk doesn't have the depth to go into a deep algorithmic
   analysis.  Instead, I will talk about specific data structures and
   their time complexities.  This time complexity is really about the
   algorithms behind the data structures, which I am not


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
