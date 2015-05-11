Algorithms and data structures
==============================

This page uses MathML, if this does not appear as "n squared" then it
does not work in your browser: :math:`n^2`

.. ::

    P art 2: Algorithms and data structures
    ~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Once you know which functions (or lines) are slow what do you do?

    - This is where you **optimize** to make these parts (and only these
      parts) faster.

    - However, optimization is pointless until you are using the best
      algorithms and data structures for the job.

    - That is what this part is about.


Outline
~~~~~~~

* Algorithms: What and why?

* Basic meaning of ``O()`` notation and why it is important.

* Properties of different data structures




What are algorithms?
~~~~~~~~~~~~~~~~~~~~

* **Algorithm**: A series of steps to complete some process.

* There can be different algorithms that produce the same result.

* All computational research involves calculating some results via
  algorithms.

* You could argue that this is **the** core Computer Science topic,
  and I can **not** do it justice.

  - This is a brief intro for scientific programmers.



Why are algorithms important?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Once I was given a program in C, a "fast" language.

* I re-wrote it in Python, a "slow" language.

* My Python code was faster, for large networks.

Why was this?  The Python code used better algorithms.

.. epigraph::

   The exact situation was that the C code used a linear search to do
   a weighted random choice.  This meant that the C code saw four
   times as slow for a network of twice the size.  In my code, I used
   a binary search I already had written, and doubling the network
   size makes the problem :math:`2*\log(2)` times slower.  That C code
   doesn't stand a chance.

   This also nicely illustrates a benefit of high-level languages.
   It is easier to use good algorithms.




Another example: graph representations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Methods of storing a graph with :math:`N` nodes:

 * Adjacency matrix: :math:`N \times N` matrix.

 * List of lists: :math:`N` lists of neighbors.

* How long does it take to compute the number of edges in the graph?

  * Matrix: have to look at :math:`N^2` elements.

  * List of lists: have to take ``len()`` of :math:`N` lists, which takes
    time :math:`c \ times N`.

* The lists of lists is clearly much faster, *for this problem*.



Big-O notation
~~~~~~~~~~~~~~

How do we express the "speeds" of algorithms?

* **Big-O notation**: used to classify algorithms by how they respond
  (processing time or memory requirements) to changes in input size.

* "Time :math:`O(N^2)`" means "time to run is proportional to :math:`N^2`".

  * Double problem size, four times as long to run.

  * :math:`N` can be different parameters, e.g. array size, number of
    records, number of atoms.

  * Different variables can be combined: :math:`O(N \times m)`

* Important since scientists tend to want to process bigger data (data
  size: :math:`N`).

* Algorithmic analysis does not care about constant factors.

.. epigraph::

   You've probably seen this before.  This is a quick formalization
   and review.

   There is not just :math:`O()`, but also :math:`o()`,
   :math:`\Theta()`, :math:`\Omega()`, and :math:`\omega()`.  These
   all represent different degrees of bounding.  For the purposes of
   this talk, I am ignoring these differences.

   I say that we don't care about constant factors.  They *are*
   important for optimization, but generally you want to first find
   the best algorithm, and then optimize constant factors.  For small
   problems, a higher complexity algorithm with smaller constant is
   better.



How am I going to explain this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Simple examples of short code lines.
* *Not* a formal analysis.
* Ignoring questions of when algorithms terminate.
* Again, this is *not* a complete picture.



Example 1: trivial
~~~~~~~~~~~~~~~~~~

.. code::

   for i in range(N):
       pass

This is :math:`O(N)`.

How to calculate big-O: multiply sizes of all loops and the inner
statements.

.. epigraph::

   ``pass`` is a single statement (that does nothing), so is O(1), the
   best possible.

   ``for i in range(N):`` does the loop ``N`` times.

   If :math:`N` doubles, the amount of work we have to do also
   doubles.


Example 2: nested
~~~~~~~~~~~~~~~~~

.. code::

   for i in range(N):
       for j in range(N):
           pass

This is :math:`O(N^2)`.

.. epigraph::

   Hopefully this is clear.  The total number of lines that execute
   here is :math:`constant \times N^2`.




Example 3: consider complexity of functions called
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose :math:`func(L)` is :math:`O(L)`:

.. code::

   for i in range(N):
       for j in range(M):
       	   func(L)

This is :math:`O(NML)`.

.. epigraph::

   You can't forget the time complexity of the functions you call.


Example 4: more called functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose ``func(N)`` is :math:`O(N)`

.. code::

   for i in range(N):
       func(N)

This is :math:`O(N^2)`.

Why?  First and second lines combine to give a time of
:math:`1+2+\cdots+N = \frac{N(N-1)}{2} = O(N^2)`.




How is complexity reduced?
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Figuring :math:`O()` is good, but what's the difference between a
  good and bad algorithm?

.. code::

   for i in range(len(data)):
       if data[i] == value:
           return i

* This is :math:`O(\mathrm{len}(\mathrm{data}))`

* But most lines do nothing!  Ideally we could short-circuit and
  return the right index directly!

.. epigraph::

   I'm not getting into formal algorithmic analysis, but here is when
   more formal theory could be helpful.  For each problem, there is
   some theoretical minimum amount of work that could be done.  Some
   algorithms are less efficient than that.

   In the case above, see compare every element in a list to
   ``value``, but just return one.  All of those needless comparisons
   could be avoided if we could filter down candidates somehow.



Complexity reduction 2
~~~~~~~~~~~~~~~~~~~~~~

.. code::

   for i in range(len(data)):       # O(N)
       if data[i] != 0:
           f(data[i])

* In this case, we do :math:`O(\mathrm{len}(\mathrm{data}))`
  operations, but the important part could be called much less often
  if ``data`` is sparse.

  .. code::

     for dat in nonzero_data:       # O(actual_data)
         f(dat)

* In this case, one should keep track of important elements
  separately, if ``data`` will be mostly zeros.



Memory complexity
~~~~~~~~~~~~~~~~~

* Memory complexity judges the amount of extra space needed for an
  algorithm.

* Example: Graph adjacency matrix is :math:`O(N^2)`.

.. code::

   range(N)        # allocates O(N) immediately
   xrange(N)       # allocates O(1)



Algorithms: summary
~~~~~~~~~~~~~~~~~~~

* *Think* about time and memory complexity when you write things.

  * I haven't taught you how to write algorithms.

  * Just know where to look for slow algorithms.  You can come back to
    them if needed, and maybe ask someone for ideas.

* In practice, do your best to make things :math:`O(\mathrm{size of data})`

* Recursion can greatly increase complexity.

* "Big data" has *extremely* clever algorithms for complexity
  reduction.

  * They can make anything :math:`O(N)`!

.. epigraph::

   I haven't even come close to giving you an understanding of the
   field of analysis of algorithms.  A CS person would be ashamed.
   However, the main point I am trying to make is *think* about what
   you are doing.  When you identify something slow, you can

   * See if you can figure out something better.

   * Remember to come back to it.

   * Ask someone for help, or search for better algorithms yourself.

   * When you do come back to algorithms, it will be much easier.

   For an example of a clever big data algorithm, see one of my last
   examples.




Data structures
~~~~~~~~~~~~~~~

The practical portion of this talk

* Data structures are specific arrangements of data in memory.

* Arrangements allow low-complexity operations on the data.

* Key point: **Using data structures properly is the most important
  way to have fast code**.

  * They package optimal algorithms for you so that you don't have to
    know about them.

* Memory/time tradeoff: Using more memory often can mean faster.




Why are data structures important?  Python list insertion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. python::

   lst = range(10000)
   lst.append(5)        # time complexity O(1)
   list.insert(0, 5)    # time complexity O(N)

If your list is big, you do **not** want to be doing the second one!

.. epigraph::

   The point of the second half of this talk is to understand the
   property of data structures, so that you don't accidentally be
   doing things like the second one, adding unneeded factors of
   :math:`O(N)` (or more) to your code!




Example 2: Time complexity of lists and sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Let us do a quick example of lists and sets: Time to find an
  "average" element.

.. python::

    n = 100
    L = range(n)
    S = set(L)

    %timeit n//2 in L
    %timeit n//2 in S

Actual time used:

=====  =====  =====  ======  ========
\      n=1    n=10   n=100   n=1000
=====  =====  =====  ======  ========
list   181ns  289ns  1270ns  11000ns
set    202ns  202ns  203ns   235ns
=====  =====  =====  ======  ========

.. epigraph::

   We see that sets take about the same of time to use the ``in``
   operator, regardless of size.  For lists, it scales with :math:`N`.
   Clearly, if we want to analyze big data, we want to be using sets!




Time complexity of typical data structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rest of talk: data structures and complexities.

* Efficient use of these is key

* Python full story: https://wiki.python.org/moin/TimeComplexity




Dynamic heterogeneous array (Python: ``list``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data layout: resizable linear array of :math:`N` elements.

* *Front operations:* ``.append(...)`` and ``del[-1]``: :math:`O(1)`

* *Back operations:* ``.insert(0, ...)`` and ``del[0]``: :math:`O(N)`

* *Indexing:* lst[...]: :math:`O(1)`



Python ``tuple``
~~~~~~~~~~~~~~~~

* Same as list, but is immutable.

* More memory efficient, especially if creating/destroying often.



Hash table mapping (Python: ``dict``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Underlying data structure: hash table

 * Lookups are an :math:`O(1)` operation!

   .. code::

       def get(x):
           return hash_table[ hash(x) % len(hash_table) ]

* *Insertions:*  ``d[k] = v`` :math:`O(1)`
* *Deletions:* ``del d[k]``   :math:`O(1)`
* *Lookups:* ``d[k]``         :math:`O(1)`
* *Contains:*: ``k in d``     :math:`O(1)`
* *Size:*: ``len(d)``         :math:`O(1)`
* There is no ordering.
* Greater memory use than lists (but still :math:`O(N)`)

Basically, all operations here is :math:`O(1)`.  ``dict``\ s trade extra
memory for fastest lookups and modification.

.. epigraph::

   Hash tables have been called "one of the most important data
   structures known".  When studying big data algorithms, most somehow
   use hash tables to turn a :math:`O(N^k)` operation into
   :math:`O(N)`.  Their properties seem almost magical.



Hash table set (Python: ``set``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Same storage as dictionary, but no values.
* Insert/delete/contains also :math:`O(1)`.
* Optimal ``intersection`` and ``union`` operations:
  :math:`O(\mathrm{min}(N,M))` and :math:`O(N+M)`



Native arrays (Python: ``numpy`` arrays)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Linear array of values *of the same type*.
* Inserting at beginning is :math:`O(N)`.
* Resizing is :math:`O(1)` but not recommended.
* Fast vector operations: ``+``, ``*``, ``numpy.add``, etc.

  * :math:`O(N)` which is optimal.



Other useful data structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Linked list - fast ``d.appendleft()`` and
  ``d.popleft()``.  Can't index middle.
  - Python: ``collections.deque``
* Heap - list which is cleverly sorted.
  - Python: ``collections.hepaq``
* Trie and DAWG

I'm not saying to write things yourself: use libraries


Other complexities
~~~~~~~~~~~~~~~~~~
* Worst case performance
* Best case performance
* Amortized worst case performance



Transitions in complexity
~~~~~~~~~~~~~~~~~~~~~~~~~
* Example: my Python code from the start

  - My code was fast in most cases, but when :math:`\beta` became
    large it got slow.  Same :math:`N`.

* You could leave problem size the same, but vary other parameters...
* ... and everything slows down greatly.
* In your parameter space, you transitioned to a different complexity.




Algorithms vs optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Algorithmic optimization provides world-changing improvements.

* Once you have the best algorithm, tricks to speed it up are
  optimization.

  * This is language and domain specific, *not covered here*.

* Most important part is good algorithms and clean code.

  - *My personal philosophy is "use the best possible algorithm, then
    optimization usually isn't needed".  :math:`O(N)` is fast enough.*



"Big data algorithms"
~~~~~~~~~~~~~~~~~~~~~
* Book: "Mining of massive datasets", http://mmds.org/
* Use hash tables to transform :math:`O(N^x)` operations to
  :math:`O(N)` operations
* Example: locality-sensitive hashing and comparing books

  - Finding similar books appears to be an :math:`O(N^2)`
    operation (you are comparing every pair)
  - Hash functions which tend to put similar documents in same bin.
  - Combine them to magnify effect, reduce number of pairs to check.



What next?
~~~~~~~~~~

* There is a standard CS course "Algorithms and data structures"

  - Probably too abstract for most general scientific programmers.

* "Hard" problems


Conclusions
~~~~~~~~~~~

* Algorithms are the key to making good programs

* Consider complexity of functions you call and write

* Try to use something optimal, and search for better option if it
  seems bad.




Examples
~~~~~~~~
