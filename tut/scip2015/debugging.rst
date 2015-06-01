===================================
Debuggers and interactive debugging
===================================


Outline
~~~~~~~

- First, we will discuss the concept of debugging beyond print
  statements.

- Then, we will discuss the basic use of traditional debuggers.

- Finally, will discuss advanced techniques for different languages.

Everyone knows that debugging is twice as hard as writing a program in
the first place. So if you're as clever as you can be when you write
it, how will you ever debug it?

| Brian Kernighan, 1974


What is debugging?
~~~~~~~~~~~~~~~~~~

- Debugging is a general process of making code work correctly, which
  can involve many different things.

- **Print debugging**: add print statements to figure out where you
   are and the value of variables.

- This talk will focus on interactive debugging tools: tools that
  allow you to *interact* with code as it's running in order to find
  bugs more *efficiently*.



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


Assertions
~~~~~~~~~~

Data display debugger
~~~~~~~~~~~~~~~~~~~~~

Other notes
~~~~~~~~~~~
* Optimization changes compiled code!

  - Compiled code is no longer one-for-one with source code

* Heisenbugs

* Memory allocation debugging:::

    - ``-lefence``

* Are you debugging crashes or wrong results?

Writing your code to be debuggable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Minimize interactions and side-effects
* Have good structure
* If code seems hard to understand, it is hard to debug

  - Make good, clean code first
  - Test that it is correct
  - *Then* profile and optimize


How to debug
~~~~~~~~~~~~

Use the scientific method

* Make the bug reproducible

  - Create some minimal example of reproducing it
  - Put it in a unit test!

* Observe the area in detail


Debuggers
~~~~~~~~~

- Combine the two things above

  - A real program runs

  - When there is an error, *stop*

  - You can print variables, type lines, etc, to figure out the
    problem

  - You can even step through, stopping when you choose to

- This allows you to both have interactive development, and
  programs/functions, together



Debuggers for different languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Debugging is a concept that exists across programming languages.
Creating a debugger is a necessary step of creating any programming
language, toolchain, or operating system.

- For C (and any language in the Gnu Compiler Collection), we have
  `gdb`_.  This would include C, C++, Fortran, and more.

  ..  _`gdb`: https://www.gnu.org/software/gdb/

- Python has a debugger named `pdb`_.

  .. _`pdb`: https://docs.python.org/2/library/pdb.html

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


Some terminology
~~~~~~~~~~~~~~~~

* **Execution frame** or **scope**: Contents of all variables at a
  certain point in code

* **Call stack**: List of active subroutines called.  ``main``
  function, then first function called, next, and so on.

.. epigraph::

   More formal definitions:

   execution frame:
      All the context within a function.  In C, it is all variables
      available for use at a certain line.  In Python, this is
      basically the local variables (``locals()``), global variables
      of the module (``globals()``).

   call stack:
       A data structure that stores active subroutines in a computer
       program.  On the stack is the ``main`` function, then the first
       function called, then the second function called, and so on.  The
       python exception tracebacks are a listing of the stack.


Prerequisites
~~~~~~~~~~~~~~

- In C, you must compile with **debugging symbols**.

  - Since C programs are basically raw machine code, the program
    doesn't include the source code for each machine instruction,
    variable names, or anything human-understandable.
  - Compile using the ``-g`` option:

    .. code:: console

      $ gcc -g filename.c

- Python, being interpreted, always has the source code available, no
  nothing special is needed.

- Other languages or compiler options may vary.



Exercise Debug-1.1: Compiling with debugging symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. In this set of exercises, we will compile a C code with debugging
   symbols and run it through the debugger in different ways.

#. In ``scip/debugging``, there is a program ``error.c`` that has an
   error in it.  Change to that directory, compile, and run it.

   .. console::

      $ gcc error.c
      $ ./a.out
      ...
      Segmentation fault

#. We see that there is a fatal error (by design).  How can we see
   where it is?  First, recompile with debugging symbols enabled.
   This is needed so that debuggers are able to see what line
   corresponds with each compiled instruction.  In ``gcc``, this is
   done with the ``-g`` flag.

   .. console::

      $ gcc -g error.c


Exercise Debug-1.2: Running with the debugger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. If you run the code normally, nothing appears different.  We have
   to start the program under control of the debugger.  For ``gcc``,
   the debugger is ``gdb``.

   .. code:: c

      $ gdb a.out
      GNU gdb (GDB) Red Hat Enterprise Linux (7.2-75.el6)
      ...
      Reading symbols from
      /home/darstr1/scip2015/debugging/a.out...done.
      (gdb)

   We end up in an interactive ``gdb`` shell.  The program doesn't
   start running until we say to.

#. First, we tell the program to run using the ``run`` command:

   .. code:: c

      (gdb) run
      Starting program: /home/darstr1/scip2015/debugging/a.out 
      ...

      Program received signal SIGSEGV, Segmentation fault.
      0x000000000040055c in main () at error.c:14
      14          printf("%d, %d, %x\n", i, *pointers[i]);
      (gdb) 

   We see that it runs, and when the error occurs we drop back to the
   interactive shell for more work.

#. Explore the following commands: ``l`` or ``list``, ``bt`` or
   ``backtrace``.

   FIXME: the program should not be all in one function for ``bt`` to
   have a useful output.

#. Let's figure out what the problem is.  Use ``p`` or ``print`` to
   try to figure out what the problem is.

   .. code:: c

      (gdb) print pointers[i]
      $1 = (int *) 0x500000000
      (gdb) print i
      $2 = 5
      (gdb) print *pointers[i]
      Cannot access memory at address 0x500000000

   It turns out that ``pointers[5]`` is an invalid memory address.  We
   investigate the definition of pointers, and see that it is of size
   5 so valid indexes go only from 0--4.  Our loop counter has an
   off-by-one error.

Exercise Debug-1.3: Breakpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Sometimes there isn't a fatal error, but there is a notable bug.
   Or maybe we want to make the debugger stop a few lines *before* our
   error, so we can examine the lead-up.  We can do this using breakpoints

#. Start the debugger again on ``a.out`` from ``error.c`` from the
   previous exercise:

   .. console::

      $ gdb a.out

#. Set a breakpoint using the ``b`` command:

   .. code:: c

	(gdb) b 8
	Breakpoint 1 at 0x400517: file error.c, line 8.

#. Now run the program:

   .. code:: c

      (gdb) run
      Starting program: /home/darstr1/scip2015/debugging/a.out 

      Breakpoint 1, main () at error.c:9
      9         for (i=0 ; i<5 ; i++) {

   The program runs and stops at this line.  You can now do all of the
   normal commands as in the last exercise.


Exercise Debug-1.4: Stepping through the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. We continue from the previous exercise.  Once we are stopped on a
   non-fatal error, we can step through the program line-by-line and
   see what is going on.

#. The command ``next`` runs the current line and goes to the next.

   .. code:: c

      (gdb) next
      10          pointers[i] = &array[i];
      (gdb) print i
      $1 = 0
      (gdb) next
      9         for (i=0 ; i<5 ; i++) {
      (gdb) next
      10          pointers[i] = &array[i];
      (gdb) print i
      $1 = 1

   We see that each line executes in the loop, one by one.  We can
   print and interact which each line in sequence.

#. Once you are done, you can ``cont`` to continue until the next
   breakpoint or error occurs.

   .. code:: c

      (gdb) cont
      ...
      Program received signal SIGSEGV, Segmentation fault.
      0x000000000040055c in main () at error.c:14
      14          printf("%d, %d, %x\n", i, *pointers[i]);





Exercise Debug-1.4: Bonus: Attaching to a running process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Let's say you have started running a program, and you need to see
   what is going on inside of it?  What can you do?

#. In ``scip/debugging``, there is a program ``attaching.c``.  Compile
   it with debugging symbols.

   .. console::

      $ gcc -g attaching.c

#. Once this program starts, it will enter an infinite loop consuming
   CPU.  It will print its process ID.  We will open a separate shell
   on triton, and *attach* to this process using ``gdb -p PID``.

   In shell 1:

   .. console::

      $ ./a.out
      This process id is 4395

   In shell 2:

   .. console::

      $ gdb -p 4395

#. Now, you can do all of the normal things.  Do this at least:

   - Print a backtrace.

   - Print ``i`` in both this and the upper frame.

   - Explore the difference between the ``next`` and ``step`` commands.

#. Don't forget to kill the process (with ``Control-C``) once you
   detach the debugger, or else you'll keep occupying the processor on
   the frontend node - a big no-no.


Exercise Debug-1.5: Bonus: Debugging Python with gdb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FIXME: add this if desired.








..
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




Conclusions
~~~~~~~~~~~
- To solve bugs, you need to see inside of code, but...

  - ... print debugging is slow and frustrating.

- Debuggers allow control and inspection of running processes

- Debugging is a fundamental concept of every language.


The end
~~~~~~~




References
~~~~~~~~~~
  - C:

  - Python:

    - A good introduction to using ``pdb``: https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/

  - Matlab:
    - http://se.mathworks.com/help/matlab/debugging-code.html
    - Tutorial: http://se.mathworks.com/help/matlab/matlab_prog/debugging-process-and-features.html#brqxeeu-177

  - Bash: http://sourceforge.net/projects/bashdb/

  - R: http://www.stats.uwo.ca/faculty/murdoch/software/debuggingR/




Advanced topics
~~~~~~~~~~~~~~~




..
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
