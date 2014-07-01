Introduction to software testing
********************************


This talk is designed to discuss the concepts of software testing.  In it, I will outline the concept of software testing and summarize the current real-world best practices and procedures.  We will then discuss how to, and the difficulties of, applying this to scientific software, but we won't actually discuss how to do it this week: next time will be a tutorial for that, based on this week's feedback.



The presentation
================

Preliminaries
-------------

Before you start
~~~~~~~~~~~~~~~~

* You are a scientist, and your code is what gives you results.

* How do you personally convince yourself that what you write is correct?

  * Do you have enough confidence that you just write and use?

  * Do you write and then run it a few times and see if the results look good?

Outline
~~~~~~~

* First, I will discuss basic concepts of testing and how other projects use it.

* Then, I will describe some of the common tools for testing

* Finally, we will discuss things that make *scientific* code testing hard

Basic concepts of unit testing
------------------------------

Testing is considered one of the cornerstones to good software.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Benefits according to wikipedia:

  * Find problems early

  * Find regressions when you make big change

  * Simplifies integration

  * Documentation

  * Design

* This talk is about systematically doing so **automatically** and **systematically**, instead of just testing only while developing.

* The key to making testing work is *balance*.

Test driven development
~~~~~~~~~~~~~~~~~~~~~~~

https://en.wikipedia.org/wiki/Test-driven_development

* Testing taken to the extreme

* You write the tests first, then write code to make the test pass.

* Nothing exists without a test.

* You can feel free to change anything and not think about it, as long as the tests pass you are good to go.

Examples of unit tests of different libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* python - http://hg.python.org/cpython/file/tip/Lib/test

  * never-ending screens of huge files.

* networkx - https://github.com/networkx/networkx/tree/master/networkx

  * All tests collected in tests/ directory in each module directory.

* sqlite3 - http://sqlite.org/testing.html

  * This project is especially proud of its tests.  1000 times more test code than project code, including three independent complete test suites, comparison against other DB engines, testing against power failures, corruptions, etc.

* django web framework - https://docs.djangoproject.com/en/1.6/topics/testing/

  * Web frameworks have lots of complications, like databases, web interfaces, etc.  Serious projects like django will include tools to manage these things: making fake databases, automatic web clients, etc.

Good projects have a policy of never accepting contributions without tests.

Good projects have a policy: if someone reports a bug, add a test to reproduce the bug, then fix it.  Bug will not appear again.

Tests can be a lot of work!  You can easily write more lines of code to test than to solve the problem sometimes.  But if code is designed well, it can be very easy.

Different types of testing
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Unit testing

  * Testing the smallest atomic components, each function in isolation without risk of other functions affecting things.

  * A *test failure* here is easy to track down since it should have only one function used.

* Integration testing

  * Testing how things work together, functions or components can communicate properly.

* System testing

  * Testing everything together, an entire run and OS interaction.

  * *Example: having test dataset that calculates quickly.  You can quickly and often run on test data to make sure the script completes and has proper output.*

* You can make tests at different levels of this hierarchy.

* Each level of this hierarchy is good for different things

* In our work we may not want to test every function at every level.

  * *Example: you may want unit tests on calculations, integration tests on some components, and no system tests: if the whole thing breaks, you'll notice anyway.*

How to test
~~~~~~~~~~~

* Tests should be **automatic** - can run and check themselves in a script, without any user interaction.

* Tests should generally be fast to run.

* Commit hooks - tests are automatically run before before you can commit, or before pushing to a central server.  (**Continuous integration**)

* There can be significant technical overhead in testing certain applications (e.g. web applications)

* Code coverage - some tools can watch the tests run and automatically tell you what lines were NOT run in any test.

As scientists, should we, and how should we, use testing in our work?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Discussion time.

* You can design things properly the first time, but what happens when you change something?  If it breaks, you may not know.

* Good test coverage gives you the ability to change things up without risking unknown breaking.

* Good testing will rely on knowing the testing hierarchy and writing the right tests for the right jobs.

Unit testing tools and workflows
--------------------------------

unittest / nose
~~~~~~~~~~~~~~~

* ``unittest``: In python standard library, provides a base to build on

  * Fully object oriented (to the point of being annoying to use)

* ``nose`` - Module to make unit testing nicer

  * "nose extends unittest to make testing easier."

  * Provides a wrapper "nosetests" to automatically find and run tests

  * Tests can also be simple functions.

The simplest way to do unit tests is to use nose.

Example:

::

   from nose.tools import assert_true, assert_equal, assert_greater_equal, assert_less

   from pcd.support.growsf_gb import *

   def test_sole():
       # For small graphs we can exactly specify what the outcome should be:                      
       # alpha=0, delta=0                                                                         
       assert_isomorphic(sole(T=3, alpha=0, delta=0),
                         G({0:(1,2), 1:(0,2)}))

       assert_isomorphic(sole(T=4, alpha=0, delta=0),
                         G({0:(1,2), 1:(0,2), 3:(1,2)}))

http://docs.python.org/library/unittest.html https://nose.readthedocs.org/

* Example bits: 

doctests
~~~~~~~~

* Put tests in the docstring of functions.

   

    ::

       >>> factororial(5)
       120

* When run with the doctest framework, the ``>>>`` lines are input, and output is below.

* Input is evaluated and must match output.

* Very simple to make, and **document as well as test**

Example:

::

   def factorial(n):
       """Return the factorial of n, an exact integer >= 0.

       If the result is small enough to fit in an int, return an int.
       Else return a long.

       >>> [factorial(n) for n in range(6)]
       [1, 1, 2, 6, 24, 120]
       >>> [factorial(long(n)) for n in range(6)]
       [1, 1, 2, 6, 24, 120]
       >>> factorial(30)
       265252859812191058636308480000000L
       >>> factorial(30L)
       265252859812191058636308480000000L

https://docs.python.org/2/library/doctest.html

Assertions
~~~~~~~~~~

* inline sanity checks - not unit tests!

* They catch things that your code and unit tests don't catch.

* They should exist in any good language - if not, make them yourself.

* Recommendation: write assertions when making new functions.  Remove them later once the function works AND if speed is an issue.

* Can be removed automatically for performance purposes 

  * ``python -o`` runs python without assertions,  ``gcc -DNDEBUG`` compiles without assertions.

  * I personally leave them in as long as possible - you never know when an assumption will be violated by changing conditions.  Correctness is more important to me than speed.

Example usage:

* I am making a growing model of a network.  

* My calculations say the next edge should be added between a and b.  

* Before calling g.add_edge(a, b), I ...

* ... write assert not g.has_edge(a, b).

* If my calculations were wrong, I will know instead of it passing silently.

Python syntax:

::

   assert test_expression, message
       # test__expression - evaluated, if True then nothing happens, if false raise AssertionError
       # message - only evaluated if expression is False, used as the assertion message.

C syntax:

::

   #include <assert.h>

   assert(expression);

Code coverage
~~~~~~~~~~~~~

* Tools that take the unit tests and run and show you which lines were NOT tested.

* Integrated with other tools.

Examples:

* Coverage report with nose: http://nedbatchelder.com/code/coverage/sample_html/

* Some other program: pybee.org/duvet/static/images/screenshot.png

Thought process behind making test scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Think about the simplest problem with an easily computed answer.  That is your benchmark.

  * You will need to make *mock data* that has known properties

* Write tests to verify those mock properties.

* Make other small changes and test them.

* Test all options to the functions.

  * Do they work together?

Benefits from this:

* Forces you to think about testing.

* Better design earlier.

* Less chance of random bugs being introduced later on.

.. === test modules and functions ===

.. * Tests should be in a separate module from the file they test (according to standard practices)

.. * Modules have functions within them.  Generally, one test function tests one real function and has many different asserts in it.

Scientific software testing
---------------------------

"Is this worth it?"
~~~~~~~~~~~~~~~~~~~

* Making test scripts is hard.

* But you _do_ always test your code anyway, just interactively and non-repeatably (you just run things).  **Right?**

* In fact, as a scientist your obligation is to make sure that your code is correct by reproducing certain things.

* You "just" need to think about this some and turn it into an automatic system.

  * Instead of testing by running stuff interactively and seeing the output, put it in a test script and run that until you get the right output.

* So in terms of the concept of making testable code, it's something you should do anyway, even though it's hard.

"Is this worth it?" Part 2
~~~~~~~~~~~~~~~~~~~~~~~~~~

* It does take some time to write them and run them.

* We need to learn ways to make this easier.

* There are tools and techniques to make this easier.

* Some aspects of scientific programming, like stochastic problems, may need extra thought.

Code structure issues
~~~~~~~~~~~~~~~~~~~~~

* You need to design code in a testable fashion

* Functions should be sufficiently modular, and do only one thing

* Suggestion: **Separate input/output/processing from calculation**.  It's easy to test calculation in isolation.

  * Example: Raj's temporal network stuff.

* Sometime, you'll need to make some real scripts and functions that can be called automatically, instead of just running everything interactively.

Combinatiorial issues
~~~~~~~~~~~~~~~~~~~~~

* With 5 different options, that is 32 different combinations to test!  Do all combinations need testing?

* Ideally, yes, but practically, no, unless you automatically write something to test them all.

* Test corner cases: Corner cases: invalid input, overflows inputs.

* Ideally, try to make sure that all code paths are hit at least once (see the coverage tests)

Stochastic issues
~~~~~~~~~~~~~~~~~

* What happens if the function depends on randomness?  You can't test that the output matches a fixed value.

* Possible solutions:

  * Seeding for reproduciblity.

    * makes it immediately reproducible, but test depends on internal structure.

  * Compare results to a distribution.

    * This requires extra tools.  `Here is a paper about that`_

  * Taking extreme values to eliminate stochasticity.

    * I tested a model by using extreme parameter values.  The output then should have been either a clique or a tree.  It's easy to verify that, and then I hope that the middle values work.

  * Making the stochastic part modular and mocking it.

Management issues
~~~~~~~~~~~~~~~~~

* It's always tempting to do something faster to get results than to do things right.

* Does management care about testing?

What should our standards be for our group library and our code?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Discussion time

* All code in the library should have some sort of tests, with enough comments to know what's going of if you read them together

* If you are using something that someone else wrote, you should look at the tests before using it.  You verify the tests are correct before using anyone else's code.

* If the tests aren't there, I guess you have to write them.  That makes you understand what's going on.

* Should there be peer review before merging with the group repository?

Recommendations for now
~~~~~~~~~~~~~~~~~~~~~~~

* Start using assertions

* Try to adapt your code to be more modular, with the most important scientific calculations in separate functions.  Next time, we can write tests for these.

Summary
~~~~~~~

* Testing is a key point of modern software development

* There are many tools and procedures to help people do this 

* Making the tests can be significant work in itself

* As scientists, we have some unique difficulties in making tests, but also a unique responsibility to do so.

*My goal is to study feedback from this presentation, and prepare a follow-up that gives specific instructions for how to use this in your work*.

What do you want for the next talk?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please give me feedback and requests.

Resources
=========

Simply doing an internet search for most of these topics will yield plenty of reading and tutorials of all sorts of levels.

Reading list
------------

* unittest docs

* nose docs

* some link to agile programming thing

* some link to TDD / extreme programming

* http://blog.stevensanderson.com/2009/08/24/writing-great-unit-tests-best-and-worst-practises/

* http://stackoverflow.com/questions/67299/is-unit-testing-worth-the-effort

.. ############################################################################

.. _CategoryTutorial: ../CategoryTutorial

.. _Here is a paper about that: ../www.urbansim.org/pub/Research/ResearchPapers/sevcikova-issta-2006.pdf

