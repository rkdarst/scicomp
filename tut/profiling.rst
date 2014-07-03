


Summary of this talk
~~~~~~~~~~~~~~~~~~~~

- Profiling

  - Seeing what takes a long time



- Algorithms and data structures

  - Making your program have a chance of being "fast"

- Optimization

  - Techniques to make your thing actually run faster

  - The least important of everything on this page


Premature optimization is the root of all problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

My traditional approach:

- Think about the problem and find the best algorithm for it

- Write your code as beautifully and extensible as possible.

- If it's slow, 


Time complexity in python data structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

n = 100
L = range(n)
S = set(L)

timeit n//2 in L
timeit n//2 in S


Time complexity of Python data structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lists

Dicts/sets

numpy arrays

collections

https://wiki.python.org/moin/TimeComplexity


Use the short prefactors built into data structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Good algorithms are more important than any optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Profiling
~~~~~~~~~


Types of profiling
~~~~~~~~~~~~~~~~~~

- Deterministic profiling

- Statistical profiling


Deterministic profiling with gcc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complie with -pg

Makes a file prof.out

View it with gprof


Deterministic profiling with Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- $ python -m cProfile -o profile  SCRIPT.py arg1 arg2 ...

- $ python -m pstats profile

The contents of pstats is every function call and return


Using pstats
~~~~~~~~~~~~

strip




Examples
========


Introduction to computational complexity

Step 1: understand O() of all algorithms

Have two sample programs and profile them.



..


