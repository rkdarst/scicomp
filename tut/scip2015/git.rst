===========================
Version control for science
===========================

Have you ever:

* Made a bunch of changes, and suddenly nothing works, and you have no
  idea what you did

* Found a bug, and wished you knew exactly when it occurred so you
  know what results are wrong?

* Wished you could collaborate better with people, without having to
  send new versions back and forth?

You aren't the first person to have these problems, in fact there is a
big set of tools to handle these issues.  Welcome: version control.

This is a 10 minute introduction to ``git``, one specific version
control system.  The tutorial has a very specific goal: to teach one
the general concepts of version control, and enough to use ``git`` on
their own, personal projects.  It doesn't go into the full power of
``git`` or version control systems (that's the next tutorial).

Keep in mind: I can't teach you git, but I can give you ideas and your
curiosity can teach you git.

Goals
-----

After completing this tutorial, you should be able to:

* Take one of your existing projects and create a git repository for it.

* Record changes in that project: for example, you might make a commit
  once per day, or a commit every time you add a new feature

* You will be able to find bugs or regressions by using that history
  to see changes.  You will be able to see exactly what your code
  lookd like on any given day, and find exactly what time a line was
  written.




Version control for Science
===========================

What is version control?
------------------------

* **Version**: Contents of files at one time
* **Control**: Tracking, storage, and analysis
* **VCS**: version control system
* Equivalent of a lab notebook for computer data
* Different programs: ``CVS``, ``subversion``, ``mercurial``, ``git``

Let's look at science *without* using VCS.

Science without version control
-------------------------------

* Just work, no backups

  - Oops, it broke and I have no idea why

* Copy files for backup

  - I have hundreds of versions but no idea what they mean

* Send files back and forth (multi-person)

  - One person works at a time, tons of versions, conflicts

.. epigraph::

   How often have you changed something and drastically changed
   results, and then you have to spend hours figuring out what you
   just did?

   With the copying system system, at least you have some backups.  But you have to
   copy it yourself, and you end up with ``code.v2.py``, ``code.v3.py``,
   ``code.final.py``, ``code.submitted.py``,
   ``code.submitted.final.py``, and so on.  And then, once you have
   all these files, you have to keep them organized, and getting any
   information out of them is a lot of work, too.  You probably won't
   make backups often enough, either.

   People often send files back and forth for papers (it could be used for code,
   but in that case it's probably easier to just work by yourself).
   You end up with the filename game again, and only one person can
   edit at once.



..
    What can you get out of version control?
    ----------------------------------------

    * Let's look at that data you can get out of a version controled
      project

    .. epigraph::

       This shows some ``git`` command line options that show you very
       useful information.  In the next part, we'll talk about how to
       actually put this information into ``git``.


    Differences between versions
    ----------------------------

    * You are working on a project, and it stopped working.  You changed
      something and broke it.
    * You can't figure out why and don't remember what you changed.
    * You type ``git diff`` at the terminal, and see every change since
      your last "commit".

    .. code:: diff

	diff --git a/support/algorithms.py b/support/algorithms.py
	index d96131b..6114c3b 100644
	--- a/support/algorithms.py
	+++ b/support/algorithms.py
	@@ -131,7 +131,7 @@
	     weighted = False
	-    def __init__(self, g, dir=None, basename=None, **kwargs):
	+    def __init__(self, g, dir=None, basename=None, cache=None, **kwargs):
		 """
		 Arguments:


    .. epigraph::

       What is the point of diffs?  Let's say you have tens of thousands
       of lines of code, and you make a few changes.  In order to
       comprehend what has changed, looking at the files themselves is too
       much.  Instead, we have a tool, the **diff**, that can direct our
       attention *only* to the important parts.

       The terms **diff** and **patch** are mostly interchangeable
       (Incidentally, ``diff`` is a program that makes diffs out of two
       files, ``patch`` is a program that takes a file and a diff and
       produces the other file).  They are one of the fundamental building
       blocks of programming, so you will see them often.

       Running ``git diff`` tells you the changes made since the last
       commit (save point), but you can get other diffs too.

       Here's how to read it:

       First two lines provide some general metadata - exactly what this
       part is about.  The details aren't important now.

       Next, we see ``--- FILENAME`` and ``+++ FILENAME``, saying what file
       this diff is of.

       Then, we see ``@@ -131,7 +131,7 @@``, which says what lines this
       diff relates to.

       Then, we see the diff itself.  Each line beginning with ``-`` is a
       line **removal**, and each line with beginning with ``+`` is a line
       **addition**.  For a line that is changed (like this example), you
       see both ``-`` and ``+`` together.

       Before and after the ``-`` and ``+``, you have **context**, which
       are unchanged lines.  You need a few lines before and after in
       order to properly understand what is changed.


       There are other diff formats.  There is a **word diff** that is
       based on words instead of lines.  It can be very useful sometimes
       (and what I look at more often than regular diffs).

       `Github example (for this talk).
       <https://github.com/rkdarst/scicomp/commit/32484303269df229756aca2e288d4f8816c4b846>`_



    What are recent changes?
    ------------------------

    * You can look at the **log** to see all past changes.

      * ``git log`` to see just descriptions, times, and who made the
	change.

    * If multiple people are working on the same project, you can check
      what others are doing.

    .. epigraph::

       The log also includes a *commit message*, which can explain to
       others (or yourself) what was going on at that time.  This is
       especially useful for multi-person projects.  There are many
       variations on these commands, including ``git log -p`` to show the
       diffs also, and ``git log --stat`` to show what files are changing.

       * `Github example (for this class itself).
	 <https://github.com/rkdarst/scicomp/commits/master>`_



    Where did a line come from?
    ---------------------------

    * Let's say you find a bug that happened a long time ago.

    * Exactly when did it happen?

    * ``git annotate FILENAME`` can answer this question

    .. code::

       114175ac        (Richard Darst  2014-01-08 15:04:10 +0200       804)        args = (_get_file(self._binary),
       114175ac        (Richard Darst  2014-01-08 15:04:10 +0200       805)                "-seed", str(self._randseed),
       e9a83ab3        (Richard Darst  2013-11-02 16:52:16 +0200       806)                "-w" if self.weighted else '-uw', #unweighted or weighted
       e9a83ab3        (Richard Darst  2013-11-02 16:52:16 +0200       807)                "-f", self.graphfile,
       8085f076        (Richard Darst  2014-01-23 19:07:45 +0200       808)                )

    * This shows , for every line, who wrote it and when.

    .. epigraph::

       This command is used less often, but when you need it, it's very
       helpful.

       Let's say that you just found a bug, a bad one.  You need to know
       immediately how many results are wrong: Are the plots you showed
       your boss one week ago wrong?  What about those from one month ago?
       If you are making lots of changes, or working with several people,
       this may not be obvious.

       If you can track down the bug to a few lines, the annotate command
       will tell you the change ID (more on this later), who made the
       change, , when the change  was made, the line number, and the
       actual code.  You can use the change ID to get further information
       on the change.

       This looks a bit ugly, but graphical user interfaces make it much
       more convenient (and there are many).

       Of course, you can view these older versions, too: ``git show
       COMMIT-ID:filename.py``

       * `Github example (this page).
	 <https://github.com/rkdarst/scicomp/blame/master/tut/git-10-minute/git-10-minute.rst>`_



What should version control be used for?
----------------------------------------

* Code
* Papers, books
* Websites
* Anything textual
* Miscellaneous data
* This course

.. epigraph::

    Pros use version control for everything: code, papers (LaTeX),
    websites, notes, etc.  All my papers are in version control, and I
    can even make PDFs showing what changed between revisions.  My
    website is in ``git``, I record changes and "push" to the server
    to automaticaly update it.  People have written ``git`` add-ons
    for distributed storage of large files (``git-annex``).  These
    tutorials are stored in a repository.



Usage of git
------------
* In this course, we will use the ``git`` version control system
* ``git`` is not just one program, it is a system.  There is:

  - command line program ``git``
  - Graphical user interfaces (``gitk``, ``git-cola``, and more)
  - Integrated support in your editor...
  - Many, many other tools

* This course will use the command line interface
* Your group may settle on a completely different VCS (Mercurial,
  Subversion, etc...)



Installation of git
-------------------

* ``git`` is already installed on Triton (and most computers these days)
* I won't cover installation, but it is available for almost any platform.

.. epigraph::

   This tutorial doesn't talk about how to install ``git``!  However, this
   is a very well documented thing, so you should have no problem
   doing it yourself.  If you have a shared computer, it probably
   already has ``git`` installed.  You can download it for almost any
   operating system here:

   - http://www.git-scm.com/downloads

   ``git`` is not just one program, there are also other graphical
   user interface (GUI) git clients, which can provide a nicer
   interface for certain tasks.  In this tutorial, I focus on the
   concepts of ``git`` and the command line.  At the end I will
   demonstrate some other programs.



Making a new repository
-----------------------

* Let's say you want to make a new git **repository** for your project.  The
  ``git init`` command does this.

  .. console::

     $ cd /path/to/your/project/
     $ git init

* Everything is stored in the ``.git`` directory within your project.

* Files are only updated when you run a ``git`` command.


.. epigraph::

   The specific git repository format is simple but complicated, and
   each VCS works differently.  We don't need to worry about it now.

   Once you run ``git init``, you won't notice any changes.  The only
   thing that will happen is the creation of a ``.git`` directory.

   No versions are saved, and your files are not touch, unless you run
   a ``git`` yourself.  This makes git relatively safe.  Nothing
   happens in the background without you knowing.  If you delete the
   ``.git`` directory, it's as if it was never made.

   Notice how easy this is.  You should be doing it for every project.


Adding initial files
--------------------

* Git doesn't automatically track anything.  You have to tell it which
  files are important (to track them).

* Use ``git add`` to make git see and track files.

  .. console::

     $ git add code1.py mod2.py README.txt

.. epigraph::

   You have to use ``git add`` here, but ``git add`` has another use
   that I am *not* going to discuss in this tutorial.  This is known
   as "staging" things to the "index".  It can be useful, but for now
   it's an unnecessary complication that you'll learn about when
   reading other things.

   You will usually run ``git status`` to check if you forgot anything
   (next section).



Check status
------------

* Check what is going on with ``git status``
* Provides a summary of modified files

  .. console::

     $ git status
     # On branch master
     # ...
     # Changes to be committed:
     #
     #       new file:   README.txt
     #       new file:   code1.py
     #       new file:   mod2.py

.. epigraph::

   ``git status`` shows what the current state is.  You will see a
   section for "files staged for commit", "modified files", and
   "untracked files".  "Untracked" is files you have not ``git
   add``ed yet.  "Modified" is tracked files which you have edited
   since the last commit.  "Staged" is files you run ``git add`` on
   but not yet committed.  If you do this, you can use ``git diff
   --cached`` to see the diff.

Check changes with diffs
------------------------
* Use ``git diff`` to see exact changes since your last commit
* This shows you exact changes, with context.


Make your first commit
----------------------

  .. console::

     $ git commit

* You will be prompted for a message in an editor.  "Initial commit"
  is traditional.


A short break: Terminology
--------------------------

* **Repository**: one directory

* **Revision** or **commit** (noun): One version of the files at one
    point in time.

    - Identified by a hexadecimal hash in ``git``, like ``526b2f9a``.

    - Commits are not per file, but for all files.

* **Commit** or **check in** (verb): The recording of one new point in history.

* **Patch** or **diff**: changes between one version and another.

* **Parent**: In git, the commit before the current one.


Regular work flow: edits and status
-----------------------------------

This is what you do on normal working days:

* Make changes to your project

* Use ``git status`` to see what is changed / what is added and waiting to be committed.

  .. console::

     $ git status

* Check ``git diff`` to see what is changed (new) since the last
  commit.

* Use ``git commit`` to make commits.

.. epigraph::

   Why should you look at diffs?  First, and most importantly, it lets
   you check yourself.  You can see all changes you have made since
   your last checkpoint (commit), to see if it makes sense when put
   together.  This may be a bit of extra work, but it is very
   important for good development practices.



Regular work flow: committing
-----------------------------

* Commit specific files

  .. console::

     $ git commit -a                         # commit all changes
     $ git commit file1.txt calculate.py     # commit specific files
     $ git commit -p                         # commit specific changes (it will ask you)
     $ git commit -p file1.txt               # commit specific changes in specific file

* You can commit in different ways

  - All changes to all files
  - Only specific files
  - Interactively review and confirm each change (``-p`` mode)

* You will be asked for a commit message.  (Advice later)

.. epigraph::

   This is the last step.  Before doing this, check status and diffs.
   After doing this, check status and make sure everything is clean.

   We'll talk about how to structure and group changes into commits
   later.



Viewing history
---------------

* The log shows history of past commits.

* Metadata about what you have done and when

  * Commit title, commit description, files changed, previous version

To view history in ``git``, run:

.. console::

   $ git log
   $ git log --oneline              # abbreviated format
   $ git log --patch                # also show patches
   $ git log --stat                 # also show stats
   $ git log --oneline --graph --decorate --all  # for later use



Getting information
-------------------

* You will have to try each of these yourself to see what they do

* COMMIT_HASH is the hexadecimal like ``86d026287189acd341e7fb2ee88063375e2e1e73`` or ``86d026`` (short).  It's a unique identifier for everything git knows.

* Show what changed since last commit

  .. console::

     $ git diff

* Show what changed in any one commit

  .. console::

     $ git show COMMIT_HASH

* Show what changed between any two commits

  .. console::

     $ git diff HASH1..HASH2

* Show old version of a file:

  .. console::

     $ git show COMMIT_HASH:file1.txt



Exercises
---------
* Next (and later in the talk) are some exercises which you will do
  yourself.
* They range from easy to hard.  Some people will just do the first
  few, and some will complete all of them.



Exercise Git-1.1: Connect to Triton
-----------------------------------
#. Everything today will be done via ``ssh`` on triton
#. To connect to triton, run:

   .. console::

      $ ssh USERNAME@triton.aalto.fi
      $ cd $WRKDIR

#. If a not your own account, make a subdirectory and change to it



Exercise Git-1.2: Standard configuration options
------------------------------------------------

#. Git has a configuration file stored in your home directory at
   ``~/.gitconfig``.  This has options that are shared among all of
   your repositories.  This can make your life easier.
#. You should at least set your name and email address wherever you
   work.
#. On triton, copy and paste the following commands into a shell. Don't
   forget to change the name/email to your own.

   .. console::

      $ git config --global user.name "Your Name"
      $ git config --global user.email your.name@domain.fi
      $ git config --global color.ui auto

      $ git config --global alias.log1a "log --oneline --graph --decorate --all"
      $ git config --global alias.st "status"
      $ git config --global alias.cm "commit"

#. You can also set your preferred editor if you don't want to use
   ``vim``

   .. console::

      $ git config --global core.editor "emacs"

#. Bonus: look at the ``git`` manual page for the config file and see
   the types of things that are available:

   .. console::

      $ man git config


Exercise Git-1.3: Making a new repository
-----------------------------------------

#. In this exercise, we will go to a directory with a simple project,
   make a new git repository, and go through the steps needed to make a
   commit.  Copy (``cp -r``) the prototype to your working directory.
   The base is in ``/triton/scip/git/git-1/``.

#. Change to the directory

    .. console::

       $ cd ~/scip/git/git-1/

#. Run ``git init`` to create a new repository in a directory.

   .. console::

     $ git init
     Initialized empty Git repository in /home/darstr1/scip/git-1/.git/

#. Everything is stored in the ``.git`` directory within your project.
   Your files are never modified unless you run a ``git`` command that
   is supposed to.

#. You need to add all the files you are working on.  ``git`` doesn't
   make any guesses: you could have temporary files, backups, and so
   on that you don't want tracked.

   .. console::

      $ git add code1.py mod2.py README.txt

#. Make your initial commit using ``git commit``.  This records all
   files that have previously been ``add``\ ed.  An editor will come
   up.  Add the commit message of "Initial commit" at the top of the
   file and save.  (Hint: to save in ``vim``, the default editor, use
   ``ESC : w q ENTER``)

   .. console::

      $ git commit

#. Check if your commit appears in the log

   .. console::

      $ git log



Exercise Git-1.4: Making edits and commits
-------------------------------------------

#. Edit ``README.txt`` and add some lines.

#. Preview your changes before committing.  This is good practice to
   make sure that you know what you are doing.  Run ``git diff`` to
   see the differences, and ``git status`` to see a summary showing that
   ``README.txt`` is modified.

#. Use ``git commit README.txt`` to record the file.

#. Repeat the above several times.  Make a) an edit to another file
   and commit, b) edits to two files at the same time and commit both,
   and c) add and commit a new file.  For each change, make the loop
   of edit, ``diff``, ``status``, ``commit``, ``log`` (to verify
   changes).  Commit different ways.  Try using ``commit -a``,
   ``commit [FILENAME]``, ``commit -p``, and so on.


Exercise Git-1.5 Check information from history
-----------------------------------------------

#. You can make changes, but how do you use them?  Eventually, you
   will wonder "what was I doing a week ago?".  ``git`` has lots of
   tools to use to answer these questions.  We will explore them now.

..
  #. Copy the OpenMP-Examples repository to your work directory.  It is
     in ``/triton/scip/OpenMP-Examples``

#. Get the OpenMP Examples repository.  We will cover the ``clone``
   command later, but for now just run this command in your working
   directory

   .. console::

      https://github.com/OpenMP/Examples.git

   You should now see a new ``Examples`` folder.  Change into it.

#. Run ``git log`` to see recent changes.  You should be able to see
   the description, author, and date.  Try adding on a ``-p`` or
   ``--stat`` options to get more details.

#. Run ``git log README`` to see recent changes to only the ``README``
   file.  You can limit to certain files this way, and even track them
   if they have been renamed.

#. What if you want to see an old version of a file?  You can see it
   using ``git show commit_id:filename``:

   .. console::

      $ git show 542c10d:README

Exercise Git-1.6: Bonus: Extra history information (annotate, diff)
-------------------------------------------------------------------
#. Often, you want to know more than just the changes.  What happens
   when you want to know *who* and *when* a particular line was
   created?  Well, there's a command for that (obviously).  ``git
   annotate`` takes a file, and for every line, shows you who
   committed it, when it was committed, and the commit hash.  You can
   use this to track down exactly when a bug was introduced, for
   example.

#. You should still be in the OpenMP-Examples directory from the
   previous exercise.

#. Run ``git annotate Title_Page.tex`` to see who has last changed each
   line.  Who is the main author of this file?  When was it last
   modified?

#. The long hexadecimal numbers are the version numbers.  Try to figure
   out what these ``git diff`` commands do:

   .. console::

      $ git diff be603ae            # same as git diff be603ae..HEAD
      $ git diff a17ad37..be603ae


Exercise Git-1.7: Bonus: ``.gitignore``
---------------------------------------
#) Make a file called ``.gitignore`` and put patterns of things you want to ignore.

   ::

     *.o
     *.pyc
     *~

#) This makes the "git status" output *more useful* and you generally
   want to keep your ignore file up to date.

.. epigraph::

   I should really emphasize how important the ``.gitignore`` file is!  It
   seems minor, but clean "status" output will really make ``git``
   much more usable.  ``.gitignore`` can be checked into version
   control itself.

#) Extra bonus: Create a ``.gitignore`` file in your home directory.
   To do this, find the configuration option for the global ignore
   file and set it to some common path, such as ``~/.gitignore``.




Sharing with others
-------------------
* Working by yourself is good, but you need to share!

* **The actual power of version control systems come from
  collaborating**

* Multiple people can work on the same project at the same time, and
  changes are merged together.

  - Even on the same *file*

* If two people edit the same lines at the same time, there is a
  **conflict**.


Branches and remotes
--------------------
* A branch is one independent line of work

  - Several people can work on the same project without interfering -
    until they are ready

* The git model considers everything a branch

  - ``git``\ 's most well known feature is easy and good branching

* Even a remote server is considered a branch
* To combine two people's work, you must **merge** the branches

Due to time constraints and practicality, we will *not* go into
branches and remotes in great detail.


``git`` remotes
---------------

* Git **remote**: a separate location for code that can be linked to
  your repository

  * This is the fundamental unit of sharing code

  * You can look at code in the remote, and pull and push code from
    them.

* Protocols for accessing remotes:

  * **local filesystem** - on same computer,
    ``/proj/networks/darst/pcd/``

  * **ssh** - anything accessable via ssh,
    ``darstr1@amor.becs.hut.fi/proj/networks/darst/pcd/``,

  * **http[s]** - using any web server,
    ``http://rkd.zgib.net/code/pcd.git``

  * **git** - special git server for efficiency,
    ``git://code.zgib.net/pcd.git``

* Remotes are conceptually like branches.


Commands for sending/receiving code
-----------------------------------

* Get a new repository

  .. console::

     % git clone [URL]

* Send your changes to server

  .. console::

     $ git push

* Get changes from server

  .. console::

     $ git pull

Conflicts
---------

* **Conflicts** are when you modify something at the same time someone
  else.

* They not common, but you will have to deal with them eventually.

* Conflicts happen when you *merge*, and you have to **resolve** them.

* When a conflict happens, the merge stops and
  you have to resolve, then finish the merge.

  - Git generally has pretty good messages - **read them** and
    follow instructions.  Don't forget or miss it, it will be bad for
    everyone.

Dealing with conflicts: meta-notes
----------------------------------
* Commit everything before trying a ``merge``!

* You have two things shown: Your version and "their" version.

  - You need to make *one* version out of these two.

* Read the instructions, ``git`` will tell you what to do.

  ::

     Auto-merging file.txt
     CONFLICT (content): Merge conflict in file.txt
     Automatic merge failed; fix conflicts and then commit the result.

* ``git diff`` and ``git status`` are your friends - still.

* If you forget to finish the resolve, you will have problems later.



Dealing with conflicts: resolution steps
----------------------------------------

* ``git`` puts markers put in the code on the exact lines of conflict::

   <<<<<<<
   <lines you have written>
   =======
   <lines they have written>
   >>>>>>>

* ``git diff`` shows the conflicting lines

  .. console::

     $ git status          # show the files that are unresolved and resolved.
     $ git diff            # show what is unresolved

* You need to combine the two versions into one.  Look
  and edit it.

* Run the command it says to continue.

  .. console::

     $ git add FILE
     $ git commit          # remembers where you left off

* Finish with ``git status`` and ``git log1a`` and ``git diff`` to make
  sure everything is there.


Exercise Git-2.1: Cloning
-------------------------
#. In this set of exercises, we will explore git pushing, pulling, and
   conflict resolution at a very high level.  We aren't going to try
   to cover everything here, but we will see some of the major
   points.  It is better to become familiar with the basics before
   going too deep into branches, remotes, and conflicts.

#. Go to http://github.com.  Use the search at the top to find a
   project related to your field.

#. Go to the project page.  Find the "HTTPS Clone URL" on the right
   side.

#. Clone the repository

   .. console::

      $ git clone https://github.com/igraph/igraph.git

#. Check out the log.  How many total commits are there in this
   repository?  (Hint: ``git log | grep ^commit | wc``)



Exercise Git-2.2: Pulling
-------------------------

#. Copy the directory ``/triton/scip/git/OpenMP-Examples-2/`` to your
   working directory.
#. View branches and remotes using ``git remote -v``.  You can see
   that it is set with the ``github.com`` server.  This is a common
   project hosting site.
#. View current commits using ``git log``.
#. Pull using ``git pull``.
#. Check current commits using ``git log``.  What is new?


Exercise Git-2.3: Resolving a conflict
--------------------------------------
FIXME: modify this exercise to have ``from numpy import ...`` as the
conflicting line to make the resolution a bit less trivial.

#. In this exercise, I have set up simple get repository, all ready to
   do a pull and make a conflict.
#. Change to the directory ``~/scip/git/git-conflict/``.
#. Run ``git log``, ``git diff`` and ``git status`` just to make sure that
   everything is clean and you know what's going on (no untracked
   changes, no surprises).
#. Pull changes from the default remote:

   .. console::

      $ git pull

   You will see a big note about a conflict::

     Auto-merging code1.py
     CONFLICT (content): Merge conflict in code1.py
     Automatic merge failed; fix conflicts and then commit the result.

#. We will now resolve the conflict.  Run ``git status`` to see the
   situation.  It should (again) say that ``code1.py`` is the file
   with conflicts::

     # Unmerged paths:
     #   (use "git add/rm <file>..." as appropriate to mark resolution)
     #
     #       both modified:      code1.py

#. Look at ``git diff``.  This is an advanced diff with two columns
   with ``+`` signs indicating what comes from each side.

#. Open ``code1.py`` in an editor.  You will see conflict marks::

       <<<<<<< HEAD
       from scipy.stats import gamma
       =======
       from scipy.stats import binom
       >>>>>>> 5de531032424ab6afe5576ee817e0ace9e9937d7

   Between ``<<<<<<<`` and ``=======`` is what you have done (in
   ``HEAD``).  Between ``=======`` and ``>>>>>>>`` is what is changed
   on the server (in commit ``5de5310``).

#. You see that one side imported ``numpy``, and the other imported
   ``scipy``.  There's no problem with doing both of these, but since
   they happened on the same line, ``git`` doesn't try to guess how to
   put them together.  A more complicated case would be edits to the
   same line.

   To resolve this conflict, we need to import both ``gamma`` and
   ``binom`` from ``scipy.stats``.  Remove the two parts, and the
   conflict markers, and make one line having all changes together.
   The top of the file should look like this after you do the
   resolution::

     ...
     import scipy
     from scipy.stats import binom, gamma
     import scipy.linalg
     import numpy

#. We will check status to make sure things are OK.  Run ``git diff``
   and see the added and changed lines.  This form of ``diff`` is
   particularly useful::

     - from scipy.stats import gamma
      -from scipy.stats import binom
     ++from scipy.stats import binom, gamma


#. Run ``git add code1.py`` to tell ``git`` that we are done resolving
   this conflict and prepare it for committing.  Run ``git status``
   before and after this to see what changes.  (Hint: it should change
   from ``Unmerged paths:`` to ``Changes to be committed:``.

#. Run ``git commit``.  An editor will open with a pre-filled commit
   message (it remembers that you were doing a merge) if you want.
   You can adjust this if needed, for example if you need to explain
   how you reconciled two opposing features.  Since there is nothing
   to add, just save and close.

#. Run ``git log`` and you should see that all changes are recorded,
   as well as the merge commit.


Exercise Git-2.4: Bonus: A full cycle of contribution
-----------------------------------------------------
#. In this exercise, you will clone a repository from github, add and
   edit some files, and send the change back.  This is a full cycle of
   what you would do if you are contributing to a real project.

#. First, clone the repository.  The repository you will be cloning is
   that of this lecture itself.  Clone using the ``git clone``
   command.  This makes a local copy of a repository on some server.

   .. console::

      git clone https://github.com/rkdarst/scicomp.git

   You will now find a new directory ``scicomp`` in your current
   directory.  Change into it.

   .. console::

      cd scicomp/

#. Now, you need to find some change to make.  There are several
   options here.  You can make a serious change that you would like to
   contribute to this talk, and I will probably actually use it.  Or,
   you can just make some random test edits for your own practice.  Go
   edit the files.  This talk is at ``tut/scip/git.rst``.

#. Commit the changes.  Use a good commit message, since someone else
   will be reading it to judge your commit!

#. Now, you have to get your commits from your computer to me.  Since
   you don't have rights to push directly to the repository, you will
   need to send me a patch.  You could open a pull request on github,
   but that is beyond the scope of this tutorial.  To do this, we will
   use ``git format-patch``.  We use do it with one argument of "the
   last upstream commit".  We can use the keyword ``origin/master``
   for this.

   .. console::

      $ git format-patch origin/master
      0001-COMMIT_TITLE.patch

   You can look at the ``.patch`` file to see the format.  It is
   formatted like a raw email.

#. Now, you need to get this file (the new ``.patch``) to me.  Command
   line email isn't set up on triton, so you should copy and attach
   this file to an email to me (``rkd@zgib.net``).  You could copy and
   paste it directly into an email, but certain mail programs can mess
   up whitespace and line wrapping, which will cause the patch to not
   apply cleanly which means it is hard to use.

#. Double-bonus: Research the "pull request" model of contributions.
   Github has good documentation on this.  Emailing patches is a
   little bit old-fashioned, but still always works.  Using the power
   of project hosting sites, you can more easily send changes, discuss
   them, and get them merged.




How does this work in practice?
-------------------------------

* How often should you commit?  **Early and often!**

* Daily model:

  * You do work for a day.  The evening before, or next morning, run commit

  * Probably more practical for chaotic research projects

  * You probably want to commit every time you make an important figure or output, to save the code version used.

* Patch model

  * You record once for each new feature you add

  * Best for things with more structure.

* Commit messages: Try to make something useful but don't think too much.

  * "Add support for filtering by degrees" 

  * "Daily work"

  * "Daily work, compare with power law model"

  * General format is: one line summary, blank line, then the notes (example from networkx)

    ::

           add dynamic Graph surport to gexf (1.2draft)

           1. can save dynamic Graph as gexf (1.2draft) format
           2. add timeformat(date/double/integer) attribute to graph
           3. add 'start' and 'end' attribute to edge


Conflict notes
--------------

* Generally, conflicts are rare and not that bad when they occur.

* They **can** be bad if two people are working on the exact same
  code, for example two people rewriting the same function.

  * But that's the case with any VCS, because you are literally doing
    the same thing two different ways.

* However you resolve the conflict, the full history is still there so
  someone can always go back and do it differently later.

* Semantic conflicts - two incompatible changes that don't touch the
  same code, like renaming a function.  VCS don't detect these.

* As long as you have committed code at one point in time, it is
  relatively safe and won't get lost.


Working to reduce conflicts
---------------------------

* All VCSs are line-based.

  - Write in a way to make each line logical.

  - Wrap LaTeX paragraphs into lines.

* Separate big changes into different commits.

* Pull and push often!  The less difference between people, the fewer
  conflicts.

Other conflict resolution options
---------------------------------
* ``git mergetool``


Project management systems (e.g. Gitlab and GitHub)
---------------------------------------------------

* Example: https://git.becs.aalto.fi/complex-networks/verkko

* Project management systems integrate with most aspects of projects

  - Version control
  - Bug tracking
  - Change requests
  - User management
  - Project hosting and release management
  - Continuous integration: unit testing and deployment

* Provide order to the project and its key resource: the code


Conclusion
----------

* Start using a version control system to collect history.

* You can answer questions like these (you'll have to search later
  though):

  * What was I doing yesterday?

  * My code just broke, what did I change?

  * I just found a bug, I need to know when it got written so I will
    know how much is invalid.

  * What code did I run one month and eight days ago to make this
    plot?

* **Collaboration** is an important part of VCSs, but we have not
  fully covered it.


The end
-------







Next steps
==========

Summary of commands: basic
--------------------------

The commands needed, as we know them now.

* Initialization

  - ``git init``  (create new repository)
  - ``git add``  (begin tracking file)

* Working and committing

  - ``git status``  (see summary of changed files)
  - ``git diff``  (see exact latest changes)
  - ``git commit``  (make new commit)

* Viewing history

  - ``git log``  (show commits and messages)
  - ``git show``  (show old commit diffs, also show old versions of files)
  - ``git diff  A..B`` (show differences between any two versions)
  - ``git annotate``  (show when files were last edited)

Summary of commands: sharing and collaborating
----------------------------------------------

These are the extra commands we have learned today.

* Getting information

  - ``git status``
  - ``git log1a`` (``git log --oneline --decorate --graph --all``)

* Branches

  - ``git checkout``
  - ``git branch <new name>``
  - ``git merge``

* Dealing with remotes

  - ``git clone``  (get a copy of a remote repository)
  - ``git remote``  (maniputate remotes)
  - ``git fetch``
  - ``git pull``  (this is the same as ``git fetch`` followed by ``git merge``)
  - ``git push``
  - ``git merge``


* Conflicts

  - ``git diff`` (show conflicts)
  - ``git add``  (mark file as resolved)
  - ``git commit``  (mark conflict as resolved)
  - ``git status``  (use before and *after* conflict to ensure it is resolved)



References
----------
* Git manual pages:

  - ``git COMMAND -h``: brief summary of major options (to help your
    memory).

  - ``man git-COMMAND`` or ``git COMMAND --help``: Full manual page
    for each command.  These are very long and detailed, but once you
    have a critical mass, these are *the* places to go for
    authoritative information.

* The git book (Pro Git): http://www.git-scm.com/book/

  - This is probably the best, and most detailed, reference there is.

  - Remember that I have purposely left out many things from this
    first talk.  The following are not discussed: branches, remotes,
    pushing, pulling, cloning, servers

  - At this point, only these chapters are relevant.

    + Chapter 1, for basic setup

    + Chapter 2, for working on your own project

    + Chapter 3, discusses branching, etc (very good diagrams and
      explinations here).

    + Section 3.5 discusses remotes, pushing, pulling, etc (notice it's
      in the branching chapter).  Chapter 4 is more useful if you are
      setting up a server, but 4.3 (ssh keys) and 4.8 (GitLab) may be
      useful.

    + Chapter 5 discusses practical points of running a distributed project.

* `Official git documentation <http://git-scm.com/documentation>`_.
  This is good for reference once you have the basics down.

  - Manual pages for each command, online

  - Videos

  - An `official tutorial <http://git-scm.com/docs/gittutorial>`_ but
    I think it's probably too theoretical.

* This tutorial from `Software Carpentry
  <http://software-carpentry.org/v5/novice/git/index.html>`_ targeted
  to scientists.

* This `interactive tutorial <http://try.github.io/>`_ from Github

* Brain and Mind Laboratory `git micromanual <https://git.becs.aalto.fi/bml/bramila/wikis/git-micromanual>`_

* Complex networks group `How to use git <https://wiki.aalto.fi/display/CompNet/How+to+use+git>`_

* This is a `cool cheat sheet
  <http://ndpsoftware.com/git-cheatsheet.html>`_, but it is too
  involved for what we know so far.  Next week, it will be more
  useful.



The "staging area" or "index"
-----------------------------
* For simplicity, I leave out one thing common in introductory
  tutorials: the "staging area" or "index"
* For "regular work flow", you can also do this:

  - ``git add [ filename OR -a OR -p ]``: add file to staging area

  - ``git commit``: Commits files previously staged with ``git add``.

* This extra step can be useful for large projects, but for us it's
  just extra work.

* By using ``git commit``  with a filename, ``-a`` (all changes), or
  ``-p`` (interactively select changes), it does the same job as ``git
  add`` followed by ``git commit``.

* Just be aware that you will see this in other tutorials.  You can
  replace ``add+commit`` with just ``commit`` if you want.



Other things to try
-------------------

Here are some ideas for independent study that you need to try
yourself:

* If you need to revert to a former version of the file:

  .. console::

     $ git checkout VERSION -- FILENAME(s)
     $ git checkout -p VERSION -- FILENAME(s)     # revert only certain parts
     $ git reset FILENAME(s)        # run this afterwards to reset the index - eliminate a complexity we haven't discussed

* If you want to go back to an old version and lose recent commits:

  .. console::

     $ git reset COMMIT_HASH            # doesn't lose file changes
     $ git reset COMMIT_HASH  --hard    # obliterates changes in working directory - dangerous!

* There are many git GUIs, including

  .. console::

     $ gitk
     $ git-cola


