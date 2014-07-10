

Practical ways to write correct code
====================================

We've covered testing.  We've covered version control.  But still




Life-critical programming
~~~~~~~~~~~~~~~~~~~~~~~~~

Can you imagine programming a traffic control system?  Or a Mars
rover?  We would completely fail at that.

There are techniques that professionals use in order to circumvent
human error.

I can't claim to know these techniques, but I can talk about what I
do.


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

When you commit, don't just commit all at once (``git commit -a``),
use ``git commit -p`` to verify each change individually.


Use lots of functions
~~~~~~~~~~~~~~~~~~~~~



Reuse code as much as possible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The more something is used, the more situations it is tested in
different circumstances.  That is _good_.

You should try to reuse your code in as many projects as possible.

Different people should use the same code in different contexts in
order to maximize the number of chances for bugs to appear.

.. epigraph::

   But never copy and paste code!



Write as clearly as possible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even if something is more verbose or slower, clearer is better.

Beautiful is easy to read and understand, easy to understand is more
likely to be correct, and more likely to be correct is more productive.

Think as if you want someone else to be able to read it and use it.



Program incrementally
~~~~~~~~~~~~~~~~~~~~~

- Use the debugger / interact to test each step of the way.



Complete rewrites are bad
~~~~~~~~~~~~~~~~~~~~~~~~~

Once I saw something about complete rewrites being bad:

- In good code, every hack/complexity in the existing codebase is
  there for a reason, to solve some bug or problem.

- Re-writing means that all of these have to be figured out again.



Run on test data first
~~~~~~~~~~~~~~~~~~~~~~

When writing anything non-trivial, compare to known results
first.  Make sure that you get existing things right.

- Make a set of small, known test datasets to use for development.

Corollary: your code should be flexible enough to run on smaller or
test data first for verification.



Use assertions
~~~~~~~~~~~~~~

- Wikipedia: `Fail-fast <https://en.wikipedia.org/wiki/Fail-fast>`_

  A fail-fast system is designed to immediately report at its
  interface any failure or condition that is likely to lead to
  failure. Fail-fast systems are usually designed to stop normal
  operation rather than attempt to continue a possibly flawed
  process.

- Think if you can sanity-check all function inputs

- Raise exceptions for input domain which is not handled yet.

.. Good use of assertions


References
~~~~~~~~~~

- https://en.wikipedia.org/wiki/Life-critical_system

  - There is a section on software engineering considerations, with
    different standards for development.

- Fail-safe and Fail-secure



Other notes
~~~~~~~~~~~

- Fail-fast
