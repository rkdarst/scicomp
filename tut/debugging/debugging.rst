Introduction to debugging
=========================

:author: Richard Darst
:date: 2014-06-24



What is debugging?
~~~~~~~~~~~~~~~~~~

- Debugging is a general process of making code work correctly, which
  can involve many different things.

- **Print debugging**: add print statements to figure out where you
   are and the value of variables.

- This talk will focus on interactive debugging tools: tools that
  allow you to *interact* with code as it's running in order to find
  bugs more *efficiently*.



Outline
~~~~~~~

- First, we will discuss the concept of interactive debugging

- Then, we will discuss the basic use of traditional debuggers

- Finally, will discuss advanced techniques for different languages.



..
  Types of debugging I will cover
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  There are two distinct concepts I will cover in this talk:
  
  - Dropping into an interactive environment in order to check out the
    variables and execute statements.  This is extremely useful for
    development and interactive work.
  
  - "Normal" debugging, using a separate debugging tool to control
    program execution.


Print debugging
~~~~~~~~~~~~~~~

1) Run code, see something wrong

2) Add in print statements to show values of variables

3) Re-run code

4) Repeat from (2) *many, many times*

.. epigraph::

   This tends to be the first way of debugging.  It works, but is
   usually slow since you have to re-run the program each time it
   goes.


Interactive development
~~~~~~~~~~~~~~~~~~~~~~~

- You have an interactive shell open (for example: ``ipython``)

- You type lines and the run right away

- You immediately see errors, and can

  - Print variables

  - Re-run lines until it works.

.. epigraph::

   This is a good system, but the things you type are temporary.  They
   can't be used as part of other functions or anything.  This makes
   it harder to use for big programs.


Debuggers
~~~~~~~~~

- Combine the two things above

  - A real program runs

  - When there is an error, *stop*

  - You can print variables, type lines, etc, to figure out the
    problem.

- This allows you to both have interactive development, and
  programs/functions, together.



Debuggers for different languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Debugging is a concept that exists across programming languages.
Creating a debugger is a necessary step of creating any programming
language, toolchain, or operating system.

- Python has a debugger named `pdb`_.

  .. _`pdb`: https://docs.python.org/2/library/pdb.html


- For C (and any language in the Gnu Compiler Collection), we have
  `gdb`_.  This would include C, C++, Fortran, and more.

  ..  _`gdb`: https://www.gnu.org/software/gdb/


- Other interpreted languages will have their own debuggers.


.. epigraph::

   - Debugging is actually an *interface*, so there can be more friendly
     front-ends available.  For example,

     - The "Data Display Debugger" (``ddd``) is a more graphical debugger
       for ``gcc``.
     - ``pudb`` is a console (ncurses) based Python debugger.
     - Most IDEs (e.g. emacs, spyder, ...) will integrate debuggers somehow.

  - Different C compilers *may* have different debuggers.  You may
    have to search some to find the right debugger for your language,
    compiler, and architecture.

  - Matlab:
    - http://se.mathworks.com/help/matlab/debugging-code.html
    - Tutorial: http://se.mathworks.com/help/matlab/matlab_prog/debugging-process-and-features.html#brqxeeu-177

  - Bash: http://sourceforge.net/projects/bashdb/

  - R: http://www.stats.uwo.ca/faculty/murdoch/software/debuggingR/


Some terminology
~~~~~~~~~~~~~~~~

* **Execution frame** or **scope**: Contents of all variables at a
  certain point in code

* **Call stack**: List of active subroutines called.  ``main``
  function, then first function called, next, and so on.

* **debugger**: Program that can monitor a running program.

.. epigraph::

   More formal definitions:


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
      Each variable is defined in a certain scope.  For example, a local
      variable is accessible within that function, but global variables
      are accessible anywhere in the file.




.. epigraph::

   Basically, whatever you do, you should be able to find a debugger for
   it.  Most of the operations I describe below should work with your
   environment.  The commands within the debuggers seem to be fairly
   standard.

   Debuggers exist not just for "normal" programs like we use here,
   but for operating system kernels (which have to operate at a very
   low level, maybe by external network connections since a kernel
   can't pause to debug itself), embedded devices (which may have to
   run over dedicated cables attached to the circuit board), as
   servers to run over network links, and so on.



Prerequisites
~~~~~~~~~~~~~~

- Python, being interpreted, always has the source code available, no
  nothing special is needed.

- In C, you must compile with **debugging symbols**.

  - Since C programs are basically raw machine code, the program
    doesn't include the source code for each machine instruction,
    variable names, or anything human-understandable.
  - Compile using the ``-g`` option:

    .. code:: console

      $ gcc -g filename.c

- Other languages or compiler options may vary.




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

- **Post-mortem debugging** is starting the debugger after some fatal
  exception or error.

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
    (Pdb) 


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
    Go up/down one stack frame.  This lets you see the variables/code in
    the calling functions using ``p`` and ``l``.

p, print <expression>
    Print a variable or an expression evaluation.

h, help
    Get help, list of commands or help on command

.. python::

    (Pdb) print x
    [ 0  1 10]
    (Pdb) print x + numpy.array([1, 2])
    *** ValueError: operands could not be broadcast together with shapes (3) (2)


.. epigraph::

    These commands are somewhat standard across debuggers



Breakpoints
~~~~~~~~~~~

- What if we want to stop and analyze program before we get an error?

- **Breakpoint**: Point to break execution and invoke debugger.

- (filename, line number) or function name.

Procedure:

1) Start the debugger

2) Set breakpoints using ``break``

3) Type ``cont``, program stops at breakpoint.


.. epigraph::

   There are other things you can do, like make conditional
   breakpoints (only break if a certain condition is true), or
   breakpoints that just print something but don't stop.  A debugger
   can be an extremely powerful environment, but I generally don't use
   it that way.



Breakpoints example
~~~~~~~~~~~~~~~~~~~

Invoke pdb on the file::

  pdb filename.py

Add a breakpoint like this:

.. python::

    (pdb) break file:lineno
    (pdb) break functionName
    (pdb) cont


.. epigraph::

    For ``gdb``: if your program has command line arguments, use
    ``gdb --args arg1 arg2 ...``)


Debugger commands 2
~~~~~~~~~~~~~~~~~~~

If you don't type ``cont``, you can step through the program manually.

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






Another way to start debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The above slides are about **post-mortem** (after death, or error)
  debugging.

- Interactive languages give you more power

- You can insert a "enter interactive mode here" marker in code.





Python: ``code.interact``
~~~~~~~~~~~~~~~~~~~~~~~~~

- You can use ``code.interact`` on a single line to examine an
  execution frame, but this doesn't give you the debugger ``up`` or
  ``down`` commands.

- Add this to a line

  .. code::

     from code import interact ; interact.interact(local=locals())

- See ``ex1.py``


Python: Begin debugger at a certain place
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- You can start a full debugger instead by using:

  .. python::

    import pdb ; pdb.set_trace()

- ``pdb`` will start exactly from that point.

- Type ``cont`` to quit debugger and resume execution.

- This allows you to go up and down the call stack, unlike
  ``code.interact``.

















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



..
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








IPython debugger - from command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IPython includes its own debugger (in a separate package,
``python-ipdb``).  It is equivalent to the regular debugger in most
respects.

- Can be automatically invoked with

  .. code::

     ipython --pdb filename.py

..
  - Runs the Python debugger on an error.  Basically equivalent to
    ``python -m verkko.misc.pdbtb filename.py``


IPython shell - post-mortem debugger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Using ``ipython`` as a shell, running functions and stuff.

- Error occurs.  Type ``%debug`` in the IPython shell.

- Debugger invoked at the point of error.

- You can combine this with a meaningless ``raise ValueError`` in
  the code to start the debugger at a certain point.



IPython debugger - interactive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To invoke ipython debugger at a certain place, do

.. code::

   import ipdb ; ipdb.set_trace()


.. epigraph::

   I have noticed that this sometimes, ``ipdb`` can't do things that
   ``pdb`` can.  If one method does't work, try the other.

   This probably relates to subtle implementation differences and
   the use of enclosing scopes.  I do *not* fully understand it, I
   figure out problems as I go.



Conclusions
~~~~~~~~~~~

- If you ever get to a point where you are adding lots of prints to
  figure out something, stop and see if there's a better way to
  inspect the environment.
  - Printing and logging can still have use.

- Debugging is a fundamental concept of every language.

- With interpreted languages, there are *many* different ways to do
  similar things.




References
~~~~~~~~~~

  - Matlab:
    - http://se.mathworks.com/help/matlab/debugging-code.html
    - Tutorial: http://se.mathworks.com/help/matlab/matlab_prog/debugging-process-and-features.html#brqxeeu-177

  - Bash: http://sourceforge.net/projects/bashdb/

  - R: http://www.stats.uwo.ca/faculty/murdoch/software/debuggingR/




Advanced topics
~~~~~~~~~~~~~~~




Python: Things to watch out for: lines not in functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Current versions of ``pdb`` and ``ipdb`` have problems with module
  lines that are **not** in any function.

- If the exception is on a line that is **not** in any function, it
  will show the exception in the first line of the file (even though
  it probably isn't there.

- As a workaround, run using one of these methods:

.. code:: console

   $ ipython --pdb <filename>.py
   $ python -m verkko.misc.pdbtb <filename>.py

Example:

.. pyinc:: exception-not-in-function.py

.. code:: pycon

    $ pdb exception-not-in-function.py
    (Pdb) cont
    1
    Traceback (most recent call last):
      ...
      File "exception-not-in-function.py", line 1, in <module>
        print 1
    Exception: The bug is on this line.
    Uncaught exception. Entering post mortem debugging
    Running 'cont' or 'step' will restart the program
    > .../exception-not-in-function.py(1)<module>()
    -> print 1

Notice that lines 6-7 and 11-12 in the output say that the exception is on
line 1 in the code, ``print 1``, **not** line 2.


Python: Things to watch out for: nested contexts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Sometimes, scopes can get mixed up and you can get to a point where
  a certain frame can't be debugged.  

- This  mainly happens with generators

Example:

  .. python::

     a = [1, 2, 3]
     print (x+b for x in a)``

Inside this generator (where the ``NameError`` is raised), you can't
print ``a``.  The scope gets messed up inside the generator and it
doesn't know how to find the ``a`` variable.  If you type ``up`` in
the debugger one or two times, it will work.

.. epigraph::

   The technical explanation is that when python does the ``exec`` of
   your input in the debugger, it doesn't properly use the *enclosing*
   scope.


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


Core dump
~~~~~~~~~

- The term **core dump** refers to a dump (to disk) of core (memory of
  a process)

- This core can be used to debug the crash, after the program has
  already terminated.

- This could be useful, for example, on jobs submitted to a cluster

- Must be enabled using ``ulimit``::

    ulimit -c unlimited
