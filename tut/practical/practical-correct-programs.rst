

Practical ways to write correct code
====================================

We've covered testing.  We've covered version control.  But still


Life-critical programming
~~~~~~~~~~~~~~~~~~~~~~~~~

Can you imagine programming a traffic control system?   Or a mars rover?



Types of bugs
~~~~~~~~~~~~~

- Undetectable from final results

- Detectable from final results

  - Raises exceptions or fails during running/compilation

  - Obviously wrong errors



Use version control a lot
~~~~~~~~~~~~~~~~~~~~~~~~~

Every change should be seen at least two times:

- when you write it

- when you commit it



Use lots of functions
~~~~~~~~~~~~~~~~~~~~~



Reuse code as much as possible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The more something is used, the more situations it is tested in
different circumstances.  That is _good_.



Write as clearly as possible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even if something is more verbose or slower, clearer is better.

Think as if you want someone else to be able to read it and use it.



Program incrementally
~~~~~~~~~~~~~~~~~~~~~

- use debugger /interact to test each step of the way



Complete rewrites are bad
~~~~~~~~~~~~~~~~~~~~~~~~~



Run on test data first
~~~~~~~~~~~~~~~~~~~~~~

When writing anything non-trivial, compare to known results
first.  Make sure that you get existing things right.

Corollary: your code should be flexible enough to run on smaller or
test data first for verification.



Use assertions
~~~~~~~~~~~~~~

- Think if you can sanity-check all function inputs

- Raise exceptions for input domain which is not handled yet.




References
~~~~~~~~~~

- https://en.wikipedia.org/wiki/Life-critical_system

  - There is a section on software engineering considerations, with
    different standards for development.

- Fail-safe and Fail-secure



Other notes
~~~~~~~~~~~

- Fail-fast
