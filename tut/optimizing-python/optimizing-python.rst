Optimizing Python
=================


Optimization
~~~~~~~~~~~~
* Optimization: making code faster
* Don't prematurely optimize
* Your development loop

  - Plan
  - Write
  - Test
  - Profile
  - Optimize
  - Goto "Test"

Basic steps
~~~~~~~~~~~

1) Strength reduction
2) Reduce memory operations
3) Reduce number of instructions

   - Python tricks
   - by transferring loops into C
   - by using special libraries

Python is not C
~~~~~~~~~~~~~~~
* In C, you write to do everything manually and explicitly
* In Python, that's a bad idea and slow
* The advantage of Python is you think at a high level, and low-level
  is managed automatically

Strength reduction
~~~~~~~~~~~~~~~~~~
* This was the previous session
* If you don't do that first, you'll eventually have to re-write and
  you lose your optimizations

Reducing memory operations
~~~~~~~~~~~~~~~~~~~~~~~~~~
* Consider memory size and operations in your analysis
* Know what operations are inplace

Memory example: tuples vs lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* With tuples: :math:`O(N^2)` copies

  .. code::

     x = ( ,)
     for i in range(10):
         x = x + (i, )

* With lists: :math:`O(N)`

  .. code::

      x = [ ]
      for i in range(N):
          x.append(x)

Memory example: ``numpy`` arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* makes a new copy

  .. code::

     a = numpy.arange(500)
   a = a * 2

* Use *inplace* numpy ``ufunc``\ s

  .. code::

     a = numpy.arange(500)
     numpy.multiply(a, 2, a)

* The last argument is an **output** argument
* If given, no new memory is allocated

``range`` vs ``xrange``
~~~~~~~~~~~~~~~~~~~~~~~
* ``range`` function: makes a list, :math:`O(N)` memory use
* ``xrange`` function: generator, :math:`O(1)` memory use
* In Python 3, ``range`` is a generator and ``xrange`` is gone

  - Similar for other things, like ``dict.items()`` vs
    ``dict.iteritems()``

Reduce the number of operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* Move things into internal Python loops
* Most of these things are good Python practice anyway

**Warning: don't make things unmaintainable**


Iteration
~~~~~~~~~

* **Iteration**: repetition in a loop

* Anything that fits here is an **iterable**

  .. code::

     for x in ITERABLE:
     # loop body

Formal iterator protocol
~~~~~~~~~~~~~~~~~~~~~~~~

* The methods ``__iter__()`` and ``next()`` define an iteration
  protocol
* Your can define iteration over your custom objects

  .. code::

     iterator = ITERABLE.__iter__()
     while True:
         try:
             x = iterator.next()   # __next__ in python 3
         except StopIteration:
             break
         # loop body

.. epigraph::

   https://docs.python.org/2/library/stdtypes.html#iterator-types

Advantages of iterators
~~~~~~~~~~~~~~~~~~~~~~~
* A core, unifying Python concept
* Modularity: keep distinct concepts separate
* Generality: allows better abstraction and clean interface
* Speed: when properly implemented, moves loops to C

Types of iterators
~~~~~~~~~~~~~~~~~~
* List comprehensions: transform iterator to a list

  .. code::

     [ f(x) for x in IT ]  # within square brackets

* Generator expressions: transform one iterator to another

  .. code::

     ( f(x) for x in IT )  # within parentheses
     # Or this:
     list.extend( f(x) for x in IT ) # function call parentheses

* Generator functions

  .. code::
     def it(N):
         for i in xrange(N):
	     yield i

     # usage
     for x in it(10):
         ....

Built-in iterators of objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``set``: iterate elements
* ``dict``: iterate keys
* ``dict.iteritems()``: iterate ``(key, value)`` pairs
* ``open(fname)``: iterate over file lines
* ``str``: characters in string
* ... and many more

Iterators: modularity
~~~~~~~~~~~~~~~~~~~~~

* Reader function:

 .. code::

   def read_file(fname):
       for line in open(fname):
           a, b = line.split()
	   yield int(a), int(b)

* Calculation function

 .. code::

   def calculate():
       stats = collections.defaultdict(int)
       for (x, count) in read_file('filename.txt'):
           stats[x] += i

* If you ever wanted to read different formats, you only need to make
  a new ``read_*`` function and plug it in

Iterators: speed
~~~~~~~~~~~~~~~~
* This uses an explicit loop to append:

  .. code::

     for x in IT:
         lst.append(x)

* This does the loop in C:

  .. code::

     lst.extend(IT)

* If you need transformation:

  .. code::

     lst.extend(x*2 for x in IT)


List comprehension: formal definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* General syntax

  .. code::

     [ expression for VAR in ITERATOR <if CONDITION_EXPRESSION>
                  for VAR2 in ITERATOR2 <if CONDITION_EXPRESSION2>
                  ... ]

* Creates a ``list`` all at once: watch out for memory use
* Fast loop that can run

  - Loop over iterator
  - Have a conditional expression
  - Function of loop variable
  - Nested loops

* Generates a true ``list`` object (with all its memory)
* Examples

  .. code::

     [ (line[0], line[1])  for line in open(file) ]
     [ (line[0], line[1])  for line in open(file)  if X in line ]

.. epigraph::

   https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions

Generator expressions: formal definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Exactly the same syntax as list comprehensions
  - But in ``()`` instead of ``[]``
* Generates data "just in time": uses less memory
* Use as feeder to something that consumes the data

* Example

  .. code::

     sum(len(line)  for line in open(fname)  if not line.startswith('#'))


Namespace lookup optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Every ``.`` results in a dictionary lookup
  - highly optimized, but still some time
  - function local variables are optimized
* In tight loops, remove the number of dots by making local references
  to variables

* Example:

  .. code::

     for i in range(10):
         print module.f(i)

  .. code::

     f = module.f
     for i in range(10):
         print f(i)

.. epigraph::

   This is a case of "don't over optimize and lose readability or
   maintainability".  Be careful what you do, profile to see if you
   are actually saving time, and only use this on inner loops *if you
   need to*.


Dynamic name binding
~~~~~~~~~~~~~~~~~~~~
* If you have to use functions anyway, you can move up the "if"
  conditions.

  .. code::

     for c in read_data(fname):
         if measure == 'nmi':
             calc_nmi(c)
         elif measure == 'vi':
             calc_vi(c)

  .. code::

     if measure == 'nmi':
         calc = calc_nmi
     elif measure == 'vi':
         calc = calc_vi
     for c in read_data(fname):
         calc(c)

* Perhaps this is most useful on objects
* The "right" way to design things would be to pass the function as an
  argument.


..
   a note said "Have some slides of data structure methods" as a
   separate slide.


Sorting
~~~~~~~
* ``list.sort()``: sorts a list in-place
* ``sorted(IT)``: sorts any iterable, returns new list
* ``key=`` argument to select sort key

  - Example: ``key=lambda x: x[1]`` to sort ``[(5, 'e'), (4, 'c')]``
    by second argument

* ``reverse=True`` to reverse sort
* These are very efficient, use existing sorting, and are stable.

String concatenation
~~~~~~~~~~~~~~~~~~~~
* Strings (e.g. ``x``) are immutable
* ``x += 'a'`` is not operate *in place* but makes a *new* string
  ``x``.
* This loop is :math:`O(N^2)`:

  .. code::

     x = ''
     for line in open(fname):
         x += line.split()[0]

* Use the ``"".join(IT)`` to make it ``O(N)``:

  .. code::

     lst = [ ]
     for line in open(fname):
         lst.append(line.split()[0])
     x = "".join(x)

* You can probably tell this should actually be:

  .. code::

     x = "".join(line.split()[0] for line in open(fname))

.. epigraph::

   Actually, these days, CPython can be smarter about the
   :math:`O(N^2)` loop, however some other implementations aren't.
   Anyway, you want to use the good practices anyway.  The last
   example is the Pythonic method.

Use exceptions instead of conditionals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Conditionals (``if``) take time and disrupt flow
* There is a different paradigm: try and catch failures

  .. code::

     for x in IT:
         if x in D:
             D[x] += 1
         else:
             D[x] = 1

  .. code::

     for x in IT:
         try:
             D[x] += 1
         except KeyError:
             D[x] = 1

* Works best if the exception is unlikely
* This is a general method of signaling between functions, without
  having to trap errors in every single place

..
   Combine with loops
   ~~~~~~~~~~~~~~~~~~
   .. code::

      try:
          for x in open(fname):
	      lst.append(float(line))
      except VlaueError:
          ... wrong format



Imports
~~~~~~~
* Imports have overhead
  - First time imported
  - Each time something is re-imported
* Important imports, put at top of file, not in functions
* If module is infrequently used, put import only in function that
  uses it.

String methods instead of functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* The ``string`` module exists, but is mostly unneeded
* Use string methods instead of those functions

  .. code::

     # not this
     import string
     string.upper(x)

     # instead this
     x.upper()

Caching
~~~~~~~
* **Cache**: temporary storage to increase performance

Other tools
~~~~~~~~~~~
* ``sqlite`` and key-value datastores


Other Python implementations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* "Normal" Python is **CPython**, which is written in C and best
  supported.
* There are other implementations, that are optimized in other ways.
* **Python** its


Cython
~~~~~~
* Translates ``python`` -> ``C``, then normal C compiler translates to
  machine code.
* Compiled C compatible with CPython as modules
* Best for
  - micro-operations on numpy arrays
  - functions where all data can be translated in to machine types.

PyPy
~~~~
* Python implementation written in Python
* This allows a powerful Just-in-time compiler

