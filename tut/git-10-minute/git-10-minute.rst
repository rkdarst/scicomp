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


Part 1: Science without version control
---------------------------------------


Strategy: Just work, no backups
-------------------------------
* Not reproducible, you lose information
* Change something and everything breaks, you have no idea what
  happened

* **Version control tracks and lets you go backwards**



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



Diffs
-----
* **diff**: program to find differences between versions
* Example ``diff -u file1.v2.txt file1.txt``:

.. code:: diff

    --- file1.v2.txt        2015-01-11 15:23:37.336871222 +0200
    +++ file1.txt   2015-01-11 15:26:28.796446554 +0200
    @@ -1,5 +1,5 @@
     mbkidbbx
     kbudbuhu
     mmmmkb uuixdeui uiyd
    -uhxgu ih hhxmui uhighi
    +uhxgu ih rxwege uhighi
     umxcu umhiui muihuihmx



Strategy: Sending files back and forth
--------------------------------------
* Disadvantage: only one person can edit at a time
* Disadvantage: who made what change?
* **Version control lets you seamlessly share and merge changes**



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



Part 2: What information does version control store?
----------------------------------------------------

* Let's look at that data you can get out of a version controled
  project



Differences between versions
----------------------------

* You have a big coding project, and you realize it doesn't work
  anywhere.  You can't figure out why and don't remember what you
  changed.

* You type ``git diff`` at the terminal, and see every change since
  yesterday.

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

* `Github example (for this talk)
  <https://github.com/rkdarst/scicomp/commit/32484303269df229756aca2e288d4f8816c4b846>`_



.. epigraph::

   What is the point of diffs?  Let's say you have tens of thousands
   of lines of code, and you make a few changes.  In order to
   comprehend what has changed, looking at the files themselves is too
   much.  Instead, we have a tool, the **diff**, that can direct our
   attention *only* to the important parts.

   The terms **diff** and **patch** are mostly interchangeable.  They
   are one of the fundamental building blocks of programming, so you
   will see them often.

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



What are recent changes?
------------------------

* You can look at the **log** to see all past changes.

  * ``git log`` to see just descriptions, times, and who made the
    change.

  * ``git log -p`` also shows you diffs of every change.

* If multiple people are working on the same project, you need to
  be able to quickly see what others have done.

* If you ever wonder what you were doing recently (for example, you
  haven't worked on a project lately but need to come back to it),
  this will help.

* `Github example (for this class)
  <https://github.com/rkdarst/scicomp/commits/master>`_


Where did a line come from?
---------------------------

* Let's say you find a bug that happened a long time ago: longer than
  you can remember.

* Exactly when did it happen?

* ``git annotate FILENAME`` can answer this question

.. code::

   114175ac        (Richard Darst  2014-01-08 15:04:10 +0200       804)        args = (_get_file(self._binary),
   114175ac        (Richard Darst  2014-01-08 15:04:10 +0200       805)                "-seed", str(self._randseed),
   e9a83ab3        (Richard Darst  2013-11-02 16:52:16 +0200       806)                "-w" if self.weighted else '-uw', #unweighted or weighted
   e9a83ab3        (Richard Darst  2013-11-02 16:52:16 +0200       807)                "-f", self.graphfile,
   8085f076        (Richard Darst  2014-01-23 19:07:45 +0200       808)                )

* `Github example (this page)
  <https://github.com/rkdarst/scicomp/blame/master/tut/git-10-minute/git-10-minute.rst>`_

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


Looking at an old version
-------------------------

You can see old versions easily:

* ``git show COMMIT-ID:filename.py``

* ``git show git show '@{one week ago}':support/algorithms.py``

* `Github example
  <https://github.com/rkdarst/scicomp/commits/master/tut/git-10-minute/git-10-minute.rst>`_
  (pick any version)


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
* Copy these into a shell and edit for your name/email

.. console::

   $ git config --global user.name "Your Name"
   $ git config --global user.email your.name@domain.fi
   $ git config --global color.ui auto


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
   but not yet committed.





Status
------

* Make some changes to your files.

* Use ``git status`` to see what is changed / what is added and waiting to be committed.

  .. console::

     $ git status

* Make a file called ``.gitignore`` and put patterns of things you want to ignore.

  ::

     *.o
     *.pyc
     *~

* This makes the "git status" output more useful and you generally want to keep your ignore file up to date.




Viewing history
---------------

* History shows you the state of your project at any time in the past

* Metadata about what you have done and when

  * Commit title, commit description, files changed, previous version

* Uses: debugging, reproducibility, sharing, collaborating.

* Can be considered either a series of snapshots in time, or a chain
  of differences between revisions.  They are equivalent.

To view history in ``git``, run:

.. console::

   $ git log
   $ git log --oneline
   $ git log --patch

.. epigraph::

   To run these git commands, first you need a repository.  All of
   these instructions use the command line - if you need to, ``ssh``
   to another server to play.  Let's practice using the repository of
   these tutorials themselves.  To get this repository, run this:

   .. console::

     $ git clone https://github.com/rkdarst/scicomp/

   You will see a ``scicomp`` folder created.  Change directory into
   it (``cd scicomp``).  You can then run the ``git log`` commands
   above.  We will learn more about the format of this repository soon.



Terminology
-----------

* **Repository**: one directory

* **Revision** or **commit** (noun): One version of the files at one point in time.

* **Commit** (verb): The recording of one new point in history

* **Patch** or **diff**: changes between one version and another.

* **Parent**: In git, the commit before the current one.






Regular work flow
-----------------

This is what you do on normal working days:

* Make changes to your project

* Run ``git status`` and ``git diff`` to see what you have done

* Commit specific files

  .. console::

     $ git commit file1.txt calculate.py     # commit specific files
     $ git commit -a                         # commit all changes
     $ git commit -p                         # commit specific changes (it will ask you)
     $ git commit -p file1.txt               # commit specific changes in specific file





Getting information
-------------------

* You will have to try each of these yourself to see what they do

* COMMIT_HASH is the hexadecimal like ``86d026287189acd341e7fb2ee88063375e2e1e73`` or ``86d026`` (short).  It's a unique identifier for everything git knows.

* Show your history of changes

  .. console::

     $ git log
     $ git log --oneline

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
* Remotes and dealing with servers (this includes Github and Gitlab)



Conclusion
----------

* You should now be able to begin collecting history for your own projects

* Start using this.  In the future, if you need to do something, ask or search.

* We have not covered:

  * branches

  * sharing and remotes (collaboration and publishing)

* You can answer questions like these (you'll have to search later though):

  * What was I doing yesterday?

  * My code just broke, what did I change?

  * I just found a bug, I need to know when it got written so I will know how much is invalid.

  * What code did I run one month and eight days ago to make this plot?

  * I am using this version of the code for my paper.  I want to never forget this point. (See ``git tag``).





Next steps
==========


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

* Official git documentation: http://git-scm.com/documentation

  - Manual pages for each command, online

  - Videos

* This tutorial from `Software Carpentry
  <http://software-carpentry.org/v5/novice/git/index.html>`_

* This `interactive tutorial <http://try.github.io/>`_ from Github

* Brain and Mind Laboratory `git micromanual <https://git.becs.aalto.fi/bml/bramila/wikis/git-micromanual>`_

* This is a `cool cheat sheet
  <http://ndpsoftware.com/git-cheatsheet.html>`_, but it is too
  involved for what we know so far.  Next week, it will be more
  useful.




Other things to try
-------------------

Here are some ideas for independent study that you need to try yourself:

* If you need to revert to a former version of the file:

  .. console::

     $ git checkout VERSION -- FILENAME(s)
     $ git checkout -p VERSION -- FILENAME(s)     # revert only certain parts
     $ git reset FILENAME(s)        # run this afterwards to reset the index - eliminate a complexity we haven't discussed

* If you want to go back to an old version and lose recent commits:

  .. console::

     $ git reset COMMIT_HASH            # doesn't lose file changes
     $ git reset COMMIT_HASH  --hard    # obliterates changes in working directory - dangerous!

* If you want to see the commit that added or edited a particular line in a file (for example, to figure out what commit introduced a bug):

  .. console::

     $ git annotate FILENAME

* There are many git GUIs, including

  .. console::

     $ gitk
     $ git-cola

Regarding ``git add``: I did **not** talk about **the index** (also known as **staging**).  This is everything related to the command ``git add``.  Most tutorial and example usages of git talk about this extensivly.  Basically, instead of running ``git commit FILENAME``, people will run

.. console::

   $ git add FILENAME
   $ git commit

so there is another step in there.  This is conceptually advantageous, but for now is an extra complication (and I hardly ever use it).  Just be aware that other tutorials will talk about ``git add``, and eventually knowing about "the index" will be a little bit useful.

