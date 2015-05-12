10 minute git
*************

Introduction
============

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



The tutorial
============

What is version control?
------------------------

* **Version**: Contents of files at one time
* **Control**: Tracking, storage, and analysis
* **VCS**: version control system
* Equivalent of a lab notebook for computer data

Let's look at science *without* using VCS.



..
    Why version control?
    - -------------------

    Have you ever:

    * Made a bunch of changes, and suddenly nothing works, and you have no
      idea what you did

    * Found a bug, and wished you knew exactly when it occurred so you
      know what results are wrong?

    * Wished you could collaborate better with people?

    You aren't the first person to have these problems, in fact there is a
    big set of tools to handle these issues.  Welcome: version control.

    * Version control can be used for code, papers, websites, anything
      textual.

    .. epigraph::

        Basically, version control systems (VCSs) stores history and
        provides tools to manage and examine that.  It makes all of these
        things things easier, and solves many, many problems.  It is
        nothing exotic: it is a standard tool of software development,
        that everyone needs.  This talk introduces these concepts to
        scientists, who may not know about it.



Part 1: Science without version control
---------------------------------------



Strategy: Just work, no backups
-------------------------------
* Not reproducible, you lose information
* Change something and everything breaks, you have no idea what
  happened

* **Version control tracks and lets you go backwards**

.. epigraph::

   This is the most basic way of working.  Once you change something,
   the old version is gone and you can't get it back.



Strategy: Copying files
-----------------------
The strategy:

* You work in a directory
* Every so often, you make a backup.

Advantages:

* You have some backups

Disadvantages:

* Manual work, many files
* No metadata or analysis tools

.. epigraph::

   With this system, at least you have some backups.  But you have to
   copy it yourself, and you end up with ``code.v2.py``, ``code.v3.py``,
   ``code.final.py``, ``code.submitted.py``,
   ``code.submitted.final.py``, and so on.  And then, once you have
   all these files, you have to keep them organized, and getting any
   information out of them is a lot of work, too.  You probably won't
   make backups often enough, either.



Strategy: Sending files back and forth
--------------------------------------
* Disadvantage: only one person can edit at a time
* Disadvantage: who made what change?
* **Version control lets you seamlessly share and merge changes**

.. epigraph::

   I've seen this used for papers often (it could be used for code,
   but in that case it's probably easier to just work by yourself).
   You end up with the filename game again, and only one person can
   edit at once.



Part 2: What can you get out of version control?
------------------------------------------------

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



Part 3: Actual usage of git
---------------------------

* In this section, we get down to actually using ``git`` (finally!)
* Many options to choose from
  - command line program ``git``
  - Graphical user interfaces (``gitk``, ``git-cola``, and more)
  - Integrated support in your editor...
* Or, your group may settle on a completely different VCS (Mercurial,
  Subversion, etc...)



Installation of git
-------------------

* I do not cover this here
* See class notes for some more information.

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



Standard configuration options
------------------------------

* There are some standard configuration options that everyone should
  set first
* Run these in a shell and edit for your name/email

.. console::

   $ git config --global user.name "Your Name"
   $ git config --global user.email your.name@domain.fi
   $ git config --global color.ui auto

.. epigraph::

   These store some information in the file ``$HOME/.gitconfig``.
   Your name and email are used in the commit logs.  We'll be using
   the git config file more, later.



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

     $ git add *.py
     $ git add file1.txt dir/file2.txt

.. epigraph::

   You have to use ``git add`` here, but ``git add`` has another use
   that I am *not* going to discuss in this tutorial.  This is known
   as "staging" things to the "index".  It can be useful, but for now
   it's an unnecessary complication that you'll learn about when
   reading other things.

   You will usually run ``git status`` to check if you forgot anything
   (next section).



Making your first commit
------------------------

* Check what is going on by typing

  .. console::

     $ git status

* After you see everything, run

  .. console::

     $ git commit

* You will be prompted for a message.  "Initial commit" is
  traditional.

.. epigraph::

   ``git status`` shows what the current state is.  You will see a
   section for "files staged for commit", "modified files", and
   "untracked files".  "Untracked" is files you have not ``git
   add``ed yet.  "Modified" is tracked files which you have edited
   since the last commit.  "Staged" is files you run ``git add`` on
   but not yet committed.  If you do this, you can use ``git diff
   --cached`` to see the diff.



Terminology
-----------

* **Repository**: one directory

* **Revision** or **commit** (noun): One version of the files at one
    point in time.

    - Identified by a hexadecimal hash in ``git``, like ``526b2f9a``.

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

* Make a file called ``.gitignore`` and put patterns of things you want to ignore.

  ::

     *.o
     *.pyc
     *~

* This makes the "git status" output *more useful* and you generally
  want to keep your ignore file up to date.

.. epigraph::

   Status tells you what you have edited since the last commit.  If it
   shows nothing, then you can be happy: everything is committed.

   I should really emphasize how important the ``.gitignore`` file is!  It
   seems minor, but clean "status" output will really make ``git``
   much more usable.  ``.gitignore`` can be checked into version
   control itself.  You can also use a ``~/.gitignore`` file in your
   home directory.



Regular work flow: check diffs
------------------------------

* Check diffs to see the exact changes.

  .. console::

     $ git diff
     $ git diff --word-diff=color

* This shows you the exact edits you have made since the last commit.
* Gives you another chance to check yourself.

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



What you do **not** know yet
----------------------------
* Branching
* Sharing and collaborating
* Remotes and dealing with servers (this includes Github and Gitlab)
* Git config files ``.gitconfig`` and aliases
* Graphical user interfaces



Revisiting: what can version control be used for?
--------------------------------------------------
* Code
* Papers, books
* Websites
* Anything textual
* Miscellaneous data
* This course



Conclusion
----------

* You should now be able to begin collecting history for your own
  projects

* Start using this.  In the future, if you need to do something, ask
  or search.

* We have not covered:

  * branches

  * sharing and remotes (collaboration and publishing)

* You can answer questions like these (you'll have to search later
  though):

  * What was I doing yesterday?

  * My code just broke, what did I change?

  * I just found a bug, I need to know when it got written so I will
    know how much is invalid.

  * What code did I run one month and eight days ago to make this
    plot?

  * I am using this version of the code for my paper.  I want to never
    forget this point. (See ``git tag``).





Next steps
==========

Summary of commands
-------------------

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

