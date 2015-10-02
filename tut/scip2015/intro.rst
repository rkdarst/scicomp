SCiP Day 2: Software tools
==========================


Outline of the day
------------------
* Version control
* Profiling
* Debugging
* Compilers, computer architecture, and optimization
* Extension to parallel programming debugging/profiling

Version control
---------------
* Provides *history* for projects
* Who did this?  When did this bug appear?  What version was used for
  the paper?
* Collaboration tools
* **Reproducible research**

Debugging
---------
* There are better ways to debug than adding prints !
* More broadly, there are many tools for inspecting program internals
  as they are running.

Profiling
---------
* Scientists understand things by quantifying them
* Computer architecture is complicated and bottlenecks are not obvious
* We can quantify internals of programs to find bottlenecks
* Never optimize without profiling first

Extension to high performance computing
---------------------------------------
* Computer architecture
* Optimization
* Advanced profiling and debugging

Extension to parallel programming
---------------------------------
* We begin with serial concepts then extend to parallel in the
  afternoon
* You must trace and track multiple things at the same time

  - Multiple points of execution
  - Multiple memory spaces
  - Communication between these

Question: what are your backgrounds?
------------------------------------


Software development: important or not?
---------------------------------------
* Idea [science]
* Code [implementation]
* Management of code and data [software development practices]

Components of software development
----------------------------------
* **Planning and design**: think before you start
* **Change tracking**: each individual change should be checked
* **Collaboration**: science isn't solitary anymore
* **Testing and ensuring correctness**: correctness is the most
  important part
* **Bug tracking and fixing**: especially when it's used by many people
* **Long-term maintenance**: sometimes, extensions and modifications
  are needed

Software testing
----------------
* Just run it and see if it is correct?

  - Is it re-tested when it changes?

* Automated tests: testing frameworks

  - Define code that should always complete successfully
  - Test against "correct" results
  - Can be re-run often: after each change, each day, each release

* Automated testing is one of the core principles of modern software
  development

Example: automatic tests
------------------------

.. python::

    def test_union():
        # Test unions of sets
        set1 = set([0, 1, 'A', 5.5])
	set2 = set([0, 1, 'B', 5])
        assert_equal(set1 || set2,  set([0, 1, 'A', 'B', 5, 5.5]))

Running with ``nosetests``

.. console::

   $ nosetests .
    ................................................................................
    ................................................................................
    ................................................................................
    ----------------------------------------------------------------------
    Ran 240 tests in 55.373s

    OK

* If there were errors, it would say exactly what tests failed, and
  how the result differed
* I can directly go and find the problem

Research vs production code
---------------------------
* **Research code**: value is in result, not code
* **Production code**: value is in the quality of the code
* Research code *often* outlives its original purpose and quality
  becomes important

The value of software design
----------------------------
* There are plenty of famous software bugs
* Beware the fallacy of "research code"

* **Scientific code must be correct**, and often also maintainable long-term
* The structure of good software development practices even helps
  scientists



The end
-------
