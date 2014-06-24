Introduction to debugging
=========================

:author: Richard Darst
:date: 2014-06-24



What is debugging?
~~~~~~~~~~~~~~~~~~

- Debugging is a general process of making code work correctly, which
  can involve many different things.

  - We've already covered tools like version control, testing, and assertions

- This talk will focus on interactive debugging tools: **tools that
  allow you to interact with code as it's running in order to find
  bugs more efficiently**.

- You could say that this is about **more effective ways of figuring
  out what you code is doing than adding lots of print statements**.



Outline
~~~~~~~

- First, we will cover the general basic concepts needed to understand
  debuggers.

- Then, I will talk about simple ways of debugging things
  interactively, instead of using print statements.

- Then, we will get to actual debuggers.  This will cover the standard
  debugger usage, which is a concept that exists in *any* development
  environment.

- Then, we will get more specific again and discuss more Python shortcuts.


..
  Types of debugging I will cover
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  There are two distinct concepts I will cover in this talk:
  
  - Dropping into an interactive environment in order to check out the
    variables and execute statements.  This is extremely useful for
    development and interactive work.
  
  - "Normal" debugging, using a separate debugging tool to control
    program execution.



Stacks and Scopes
~~~~~~~~~~~~~~~~~

In order to best understand what is going on, let's introduce some
terminology:

call stack:
    A data structure that stores active subroutines in a computer
    program.  On the stack is the ``main`` function, then the first
    function called, then the second function called, and so on.  The
    python exception tracebacks are a listing of the stack.

execution frame:
   All the context within a function.  In Python, this is basically
   the local variables (``locals()``), global variables of the module
   (``globals()``).

scope:
   I use this to mean the current attribute lookup path, ``locals()``
   then ``globals()`` and so on.  All of our interaction occurs in a
   certain scope.



Debuggers for different languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Debugging is a concept that exists across programming languages.
Creating a debugger is a necessary step of creating any programming
language, toolchain, or operating system.

.. epigraph::

   Debuggers exist not just for "normal" programs like we use here,
   but for operating system kernels (which have to operate at a very
   low level, maybe by external network connections since a kernel
   can't pause to debug itself), embedded devices (which may have to
   run over dedicated cables attached to the circuit board), or over
   network links.

- Python has a debugger named ``pdb``.

- For C (and any language in the Gnu Compiler Collection), we have
  `gdb`_.  This would include C, C++, Fortran, and more.

  ..  _`gdb`: https://www.gnu.org/software/gdb/

  - Different C compilers *may* have different debuggers.  You may
    have to search some to find the right debugger for your language,
    compiler, and architecture.

- Other interpreted languages will have their own debuggers.

- Debugging is actually an *interface*, so there can be more friendly
  front-ends available.  For example,

  - The "Data Display Debugger" (``ddd``) is a more graphical debugger
     for ``gcc``.
  - ``pudb`` is a console (ncurses) based Python debugger.
  - Most IDEs (e.g. emacs, spyder, ...) will integrate debuggers somehow.



.. epigraph::
   Basically, whatever you do, you should be able to find a debugger for
   it.  Most of the operations I describe below should work with your
   environment.  The commands within the debuggers seem to be fairly
   standard.



Prerequisites
~~~~~~~~~~~~~~

- In C, you must compile with **debugging symbols**.

  - Since C programs are basically raw machine code, the program
    doesn't include the source code for each machine instruction,
    variable names, or anything human-understandable.
  - Compile using the ``-g`` option:

    .. code:: shell

      $ gcc -g filename.c

- Python, being interpreted, always has the source code available, no
  nothing special is needed.

- Other languages or compiler options may vary.



Actual programs vs running functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I have observed two main ways people write their code:

- As programs, with a start and end point.

  - There are discrete files for each task.
  - Run from the command line, does something, and exits.
  - Most classic debugger tools are designed to handle this case.

- As functions that are run from the shell

  - There is a library of functions, but it can't be run directly.
  - There is one persistent interactive shell, where the library is
    continually reloaded and functions called over and over again.
  - Debugging is equally applicable here, but you need different ways
    to start.

- The concepts of debugging for both of these is similar.



Interactive debugging
~~~~~~~~~~~~~~~~~~~~~

Let's say you have a program, and there is one function you are
working on.  This is how you **print debug**:

- Add in some print statements.
- Run the code, see the output.
- You get an idea of what might be wrong, and you try fixing it and it
  still dosn't work.  You add more print statements, and repeat.
- Eventually, you figure out what's wrong, fix the code, and have to
  go remove all of the print statements.


This is a long, annoying process.  It takes many rounds, and you are
basically doing the same things over and over.

You wish that you could:

- Run the entire program up until a point in the function.
- **Stop** and get an interactive shell with all of the local function
  variables.
- Play with the variables in the function yourself, observing the
  results until you figure out the correct code.
- Copy that code back into the file at the right place.

Example:

- This is the rawest, most basic form that doesn't rely on any
  external dependencies.
- We call ``code.interact`` with a given``locals()`` dictionary.

.. pyinc:: ex1.py

Output:

.. python::

    Python 2.7.3 (default, Mar 13 2014, 11:03:55)
    [GCC 4.7.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> print a
    1
    >>> print a+b == c
    True
    ^D
    3

- The interactive console starts *inside* the function
- This is *much* faster than editing the file to add prints,
  - especially since you can adapt what you print to what you see.
- Don't use this only for debugging: use this as a faster way of
  writing things correctly in the first place.



Other options for interactive debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- It is better to use my ``verkko.misc.interact`` module than
  ``code.interact``.

  - ``locals()`` are automatically found and set.
  - ``globals()`` is also passed (not possible with ``code.interact``
  - No banner
  - Enables tab completion

- To use it

  .. python::

        from verkko.misc import interact ; interact.interact()

- Even faster method:

  - Simply include this in your file at the place you want to
    interact:

    .. python::

       import verkko.misc.interactnow

  - This is easier to type quickly, but only interacts on the *first*
    round through the code.

  - Example:

    .. pyinc:: ex2.py





Debuggers
~~~~~~~~~

Problems with the interactive examples above:

- They operate only in a *single stack frame*, so...

- You can't see any variables in the function above.

The debugger:

- Allows you to move up/down in the stack frame.

- You can control program execution in much more detail.
  - Step through programs line-by-line




Post-mortem debugging on a program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Post-mortem debugging is starting the debugger after some fatal
  exception or error is reached.

  Example:

  .. pyinc:: ex-raises-exception.py

- We run ``pdb filename.py`` on our file

- We type ``cont`` to begin execution.

- When an exception happens, you can inspect the problem.

.. python::

    $ pdb ex-raises-exception.py
    > /home/richard/scicomp/tut/debugging/ex-raises-exception.py(1)<module>()
    -> import numpy
    (Pdb) cont
    Traceback (most recent call last):
      ...
      File "ex-raises-exception.py", line 1, in <module>
        import numpy
      File "ex-raises-exception.py", line 7, in main
        func(arr)
      File "ex-raises-exception.py", line 3, in func
        x + numpy.array([1, 2])
    ValueError: operands could not be broadcast together with shapes (3) (2) 
    Uncaught exception. Entering post mortem debugging
    Running 'cont' or 'step' will restart the program
    > /home/richard/scicomp/tut/debugging/ex-raises-exception.py(3)func()
    -> x + numpy.array([1, 2])
    (Pdb) print x
    [ 0  1 10]
    (Pdb) print x + numpy.array([1, 2])
    *** ValueError: operands could not be broadcast together with shapes (3) (2)


Debugger commands
~~~~~~~~~~~~~~~~~

The debugger has many commands:

cont, continue
    Run code until there is an exception.

l, list
    List lines of code around the exception, or at any other point.

bt, backtrace
    Print a bactrace of all stack frames, for example:

    .. python::

       /home/richard/scicomp/tut/debugging/ex-raises-exception.py(1)<module>()
       -> import numpy
         /home/richard/scicomp/tut/debugging/ex-raises-exception.py(7)main()
       -> func(arr)
       > /home/richard/scicomp/tut/debugging/ex-raises-exception.py(3)func()
       -> x + numpy.array([1, 2])


u, d, up, down
    Go up/down one stack frame.  This lets you see the variables 

p, print  <expression>
    Print a variable or an expression evaluation.

h, help
    Get help, list of commands or help on command

.. epigraph::
    (These commands are somewhat standard across debuggers)



Debugging a running program
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Above, we did *post-mortem* debugging: the debugger started when an
  exception happened.
- What if we don't have an error, and want to run and analyze each
  step?


  Invoke pdb on the file::

      pdb filename.py

..

    (gdb: if your program has command line arguments, use ``gdb --args
    arg1 arg2 ...``)

Let's say we want to skip ahead to a certain point.  We add a
**breakpoint**

- Typing ``cont`` runs until there is an exception, OR
- A breakpoint stops execution at that point
- Breakpoints can be specified by file name and line number or
  function names.

Add a breakpoint like this:

.. python::

    (pdb) break file:lineno
    (pdb) break functionName

.. epigraph::

   There are other things you can do, like make conditional
   breakpoints (only break if a certain condition is true), or
   breakpoints that just print something but don't stop.  A debugger
   can be an extremely powerful environment, but I generally don't use
   it that way.


You can use these commands to interact with the running program:

s, step:
    Run the current line and then stop again.  Step into any functions
    called on the next line.

n, next:
    Run the next line(s).  If there are functions called in the next
    line, do not debug inside of them.

r, return:
    Run until the function returns, then return to the debugger.

Example:

.. pyinc:: ex-breakpoints.py

Output:

.. code:: console

    $ pdb ex-breakpoints.py
    > /home/richard/scicomp/tut/debugging/ex-breakpoints.py(3)<module>()
    -> def A(x):
    (Pdb) break B
    Breakpoint 1 at
    /home/richard/scicomp/tut/debugging/ex-breakpoints.py:9
    (Pdb) cont
    begin A
    > /home/richard/scicomp/tut/debugging/ex-breakpoints.py(10)B()
    -> print 'begin B'
    (Pdb) l
      8  
      9 B   def B(y):
     10  ->     print 'begin B'
     11         c = y * 2
     12         print c
     13         print 'end B'

.. epigraph::

   A "normal" way of using this on a program would be to start the
   debugger, set a breakpoint before the problem, and step through the
   file, checking each line manually to see what the error is.

   With interactive languages like Python that have better error
   handling facilities, this is not as critical a development
   strategy, but is useful nonetheless.



Attaching to a running process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- In everything we have done so far, we have to decide we want to
  debug *before* we start the program.  What happens if it's already
  running?

- ``gdb`` (the GNU debugger) can attach to already running processes::

    gdb -p PID

- Then, you use ``bt`` to figure out where you are in the call stack,
  ``list`` to list the code, and ``print`` to show contents of
  variables, etc.

- You could even set future breakpoints and then ``cont``, and it will
  run until you get there.  Or just use ``step`` and ``next`` to
  continue through the program.

Example:

.. pyinc:: gdb-attaching.c

Output:

.. code:: console

    $ gcc -p PID
    ...
    main () at gdb-attaching.c:7
    7         }
    (gdb) print a
    $1 = 1503027589



Using gdb on a running python process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- I said that ``gdb -p`` only works on C programs.  That isn't exactly
  true.
- If you install the ``python-dbg`` package, you will get GCC
  extensions for Python that allow GCC to inspect and interact with
  the Python frames
- You have Python versions of the debugger commands:

  - py-list
  - py-up, py-down
  - py-print


Example:

.. pyinc:: gdb-attaching-python.py

Output:

.. code:: console

   $ gdb -p 17456

   <endless ugly stuff>

   (gdb) py-bt
   #0 Frame 0x12a7870, for file gdb-attaching-python.py, line 6, in
   <module> ()
   (gdb) py-list
   ...
   1
   2    a = 0
   3    while True:
  >4        a += 1
   ...
   (gdb) py-print a
   global 'a' = 52638676



Invoking debugger at a certain place
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- You can use ``code.interact`` on a single line to examine an
  execution frame, but this doesn't give you the debugger ``up`` or
  ``down`` commands.
- You can start a full debugger instead by using:

  .. python::

    import pdb ; pdb.set_trace()

  Then pdb will start exactly from that point.



Easy use of PDB from command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I wrote a module to invoke pdb automatically:

- You normally run your program with 

  .. code:: console

     $ python filename.py

- Change to run your program with

  .. code:: console

     $ python -m verkko.misc.pdbtb filename.py

  .. epigraph::

     This uses the standard ``python -m MODNAME ...`` mechanism.  It is
     the same as running ``python /path/to/MODNAME.py ...`` .

- Python will run normally and with no overhead.  You don't have to
  type ``cont`` to make it start or quit/restart the debugger.

- If (and only if) there is an exception, it will drop to pdb at that
  point.  Otherwise, the program terminates normally.



IPython debugger - from command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IPython includes its own debugger (in a separate package,
``python-ipdb``).  It is equivalent to the regular debugger in most
respects.

- Can be automatically invoked with

  .. code::

     ipython --pdb filename.py

  - Runs the Python debugger on an error.  Basically equivalent to
    ``python -m pdb filename.py``



IPython debugger - post-mortem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``%debug`` in the IPython shell.

  - When you are running IPython, if you get an exception, you can
    type ``%debug`` and it will invoke the debugger at that
    traceback.

  - You can combine this with a meaningless ``raise ValueError`` in
    the code to start the debugger at a certain point.



IPython debugger - interactive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To invoke ipython debugger at a certain place, do

.. code::

   import ipdb.set_trace()


.. epigraph::

   I have noticed that this sometimes, ``ipdb`` can't do things that
   ``pdb`` can.  If one method does't work, try the other.

   This probably relates to subtle implementation differences and
   the use of enclosing scopes.  I do *not* fully understand it, I
   figure out problems as I go.



Things to watch out for
~~~~~~~~~~~~~~~~~~~~~~~

- Sometimes, scopes can get mixed up and you can get to a point where
  a certain frame can't be debugged.  For example, generators can have
  problems:

  .. python::

     a = [1, 2, 3]
     print (x+b for x in a)``

  Inside this generator (where the ``NameError`` is raised), you can't
  print ``a``.  The scope gets messed up inside the generator and it
  doesn't know how to find the ``a`` variable.  If you type ``up`` in
  the debugger one or two times, it will work.


- ``pdb`` seems to have problems with lines in files that are *not*
  part of any function.  When you are running a file as a script and
  aren't in any function, it always looks like it is only on the first
  line of the file..




Conclusions
~~~~~~~~~~~

- If you ever get to a point where you are adding lots of prints to
  figure out something, stop and see if there's a better way to
  inspect the environment.
  - Printing and logging can still have use.

- Debugging is a fundamental concept of every language.

- With interpreted languages, there are *many* different ways to do
  similar things.
