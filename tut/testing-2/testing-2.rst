Software testing with Python and nose
*************************************


Git repository for the talk:  https://git.becs.aalto.fi/complex-networks/tutorial



The presentation
================

In this talk, I will cover:

* The pieces that go into unit testing (functions, assertions, etc)

* I have an example directory with a lot of functions and unit tests

* We will go through these tests and experience the key points.

The pieces
----------

Test modules
~~~~~~~~~~~~

* General practice is to put your tests in a separate module from the main code itself.

* The name should include the word "test" either at the beginning or after a "_" or some special symbol.

* My recommendation: either call it ``NAME_test.py`` or ``test_NAME.py``.  I  use the second.

* The modules must be importable (no side effects when run, if it has primary code put it in a ``if __name__ == "__main__":``) block

`nosetests` command line program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Use to run tests.

* Usage:

   

    ::

       nosetests
       nosetests test_NAME.py
       nosetests test_NAME.py:test1

  * First version: Run all tests in this directory

  * Second version: Run all tests in this file

  * Third version: You are working on one function and want to run it's tests repeatedly and quickly.

* Standard output is hidden by default, unless a test fails!  Use ``-s`` to make all standard output be shown.

Test functions and classes
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Test functions: extremely simple to write.

* Test classes: Needs a little bit more structure (but not too much), but you can easily use other thinsg like:

  * setup and teardown methods.  

    * setup: something run before the test (e.g. create an object or create temporary files)

    * teardown: something run after the test (e.g. remove temporary files)

  * Inheritance for customization.

Assertions
~~~~~~~~~~

* wiktionary: **a condition expected to be true at a particular point**

* The fundamental unit of a test.  One test function or method can have many assertions in it.

* Use ``assertions functions`` that do the following:

  * Compare the arguments according to some rules to verify the assertion

  * If the condition is false, raise ``AssertionError`` and print some useful error message.

  EXample:

::

   >>> assert_set_equal(set([1, 2, 3]), set([1, 2, 4]) )

   AssertionError: Items in the first set but not the second:
   3
   Items in the second set but not the first:
   4

Look at how it prints exactly what the difference is.  Maybe you don't even need to go debugging it yourself if this is enough to realize what went wrong.

* You can also use the ``assert`` keyword:

  ::

     assert func(5) == 1

What assertions are available?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the list of ``assert*`` methods https://docs.python.org/2/library/unittest.html#assert-methods

* I recommend you to ``from nose.tools import *``.  This module provides *functional versions* of these ``assert*``.

* Instead of ``assertSetEqual``, it will be called ``assert_set_equal`` in nose.tools.

::

   nose.tools.assert_almost_equal
   nose.tools.assert_almost_equals
   nose.tools.assert_dict_contains_subset
   nose.tools.assert_dict_equal
   nose.tools.assert_equal
   nose.tools.assert_equals
   nose.tools.assert_false
   nose.tools.assert_greater
   nose.tools.assert_greater_equal
   nose.tools.assert_in
   nose.tools.assert_is
   nose.tools.assert_is_instance
   nose.tools.assert_is_none
   nose.tools.assert_is_not
   nose.tools.assert_is_not_none
   nose.tools.assert_items_equal
   nose.tools.assert_less
   nose.tools.assert_less_equal
   nose.tools.assert_list_equal
   nose.tools.assert_multi_line_equal
   nose.tools.assert_not_almost_equal
   nose.tools.assert_not_almost_equals
   nose.tools.assert_not_equal
   nose.tools.assert_not_equals
   nose.tools.assert_not_in
   nose.tools.assert_not_is_instance
   nose.tools.assert_not_regexp_matches
   nose.tools.assert_raises
   nose.tools.assert_raises_regexp
   nose.tools.assert_regexp_matches
   nose.tools.assert_sequence_equal
   nose.tools.assert_set_equal
   nose.tools.assert_true
   nose.tools.assert_tuple_equal

Invoking the python debugger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a test fails, you can automatically invoke the debugger:

* ``nosetests --pdb``  starts pdb when an exception is raised (NOT ``AssertionError``)

* ``nosetests --pdb-fail`` starts pdb when an ``AssertionError`` is raised.

* Note: these options change in recent versions of node, ``--pdb`` should be sufficient to catch all errors.

Useful pdb commands:

* ``l`` or ``list`` - list lines of code around the point

* ``bt`` or ``backtrace`` - list full call stack.

* ``u`` or ``up`` and ``d`` or ``down`` - Go up or down the call stack

* ``p`` or ``print`` - print any variable or expression

* Anything else: run this command in python 

Full list of commands: https://docs.python.org/2/library/pdb.html#debugger-commands

The ``ipython`` debugger is functionally equivalent to ``pdb``.

If you want to invoke the debugger at one specific point, just use the ``raise`` keyword at that point:

::

   raise

::

   if n == 5:
       raise

Learning by example
-------------------

Recommendations for making tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Think about what axes can be used to simplify the problem.  For example, if the problem scales as a function of ``n``, write tests for low ``n`` where the solution is easily checked in your head.

* Try to think of all important boundary cases to handle

* Testing is easiest for ``pure functions``: the return value depends only on arguments and the function does not have any side effects.

* You will be tempted to import the module and run it.  Don't do that.  Whatever you would do in the shell,

  * Put it in a test instead - it's the same amount of work.

  * If there is an exception or ``AssertionError``, then use ``--pdb`` or ``--pdb-fail`` to 

* Have two windows open: one with the editor, and one to run ``nosetests`` over and over again.

How to debug a failing test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Is the test correct?

* Run with ``-s`` option to show standard output (if needed)

Full example: Permutations
~~~~~~~~~~~~~~~~~~~~~~~~~~

* You will find ``perm.py`` and ``test_perm.py`` in the repository.

Prime number testing
~~~~~~~~~~~~~~~~~~~~

* ``prime.py`` contains a function for testing for primality of numbers.

* Run ``test_prime.py`` in nosetests.

* When it fails, use ``--pdb`` or ``--pdb-fail`` to invoke the debugger and examine the situation.

* Try to fix the line in the debugger so that it works.

* Copy your fix to the module, then repeat.

Fibonacci numbers
~~~~~~~~~~~~~~~~~

* ``fib.py`` contains two functions to calculate the ``n``\ th Fibonacci number

* In ``test_fib.py`` you see a class-based method of testing both the functions.

  * Notice that both functions are expected to pass the exact same tests.

Instructions:

* Use ``nosetests`` to run ``TestFib1`` only.  Does it pass?

* Use ``nosetests`` to run ``TestFib2`` only.  Does it pass?

* If any don't pass, use ``--pdb`` or ``--pdb-fail`` to examine the situation, if you think it will help.

* Fix the problem until the test suite passes.

Test-driven development
~~~~~~~~~~~~~~~~~~~~~~~

* A function that returns the counts of items in an iterable as a dictionary.

  * Example:  ``[1, 1, 5, ]  -->   {1:2, 5:1}``

* You will find ``count.py`` and ``test_count.py`` in the repository.

Instructions:

* Run the test module.  Notice it fails because ``count.py`` is empty but there is one test.

* Write a ``count`` function to make the test pass.

* Do the following over and over until you are satisfied:

  * Think: What else should this function return (hint: the example above)

  * Write a test script for that example.

  * Run the test script: notice it fails.

  * Fix the function so that it passes.

Euler 001: sum of multiples of 3 and 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem: https://projecteuler.net/problem=1

**If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23**.

**Find the sum of all the multiples of 3 or 5 below 1000.**

Instructions:

* Make a module ``e001.py`` and solve this problem for general ``n``.

* Make a module ``test_001.py`` and write a test for this function.  Hint:

  ::

     from nose.tools import *
     from e001 import euler001

     def test_001():
        ...

Further topics
--------------

Statistical tests
~~~~~~~~~~~~~~~~~


