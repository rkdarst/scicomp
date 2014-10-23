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

* Record changes in that project: for example, you might make a commit once per day, or a commit every time you add a new feature

* You will be able to find bugs or regressions by using that history
  to see changes.  You will be able to see exactly what your code
  lookd like on any given day, and find exactly what time a line was
  written.


Before beginning
----------------

Install git.

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

There are some standard configuration options that everyone should set first:

.. console::

   $ git config --global user.name "Your Name"
   $ git config --global user.email your.name@domain.fi
   $ git config --global color.ui auto





The tutorial
============

Why version control?
--------------------

Have you ever:

* Made a bunch of changes, and suddenly nothing works, and you have no
  idea what you did

* Found a bug, and wished you knew exactly when it occurred so you
  know what results are wrong?

* Wished you could collaborate better with people, without having to
  send new versions back and forth?

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

    Pros use version control for everything: code, papers (LaTeX),
    websites, notes, etc.  All my papers are in version control, and I
    can even make PDFs showing what changed between revisions.  My
    website is in ``git``, I record changes and "push" to the server
    to automaticaly update it.  People have written ``git`` add-ons
    for distributed storage of large files (``git-annex``).  These
    tutorials are stored in a repository.





What is history?
----------------

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





Just what is this ``git`` repository?
-------------------------------------

* Everything is stored in a ``.git`` directory within your project.

* ``git`` doesn't automatically do anything.  You develop as normal,
  and ``git`` records or changes things when you tell it to (such as
  ``git revert`` to go to an older version).

Let's say you want to make a new git repository for your project.  The
``git init`` command does this.

  .. console::

     $ cd /path/to/your/project/
     $ git init


.. epigraph::

   The specific git repository format is simple but complicated, and
   each VCS works differently.  We don't need to worry about it now.

   Once you run ``git init``, you won't notice any changes.  The only
   thing that will happen is the creation of a ``.git`` directory.





Terminology
-----------

* **Repository**: one directory

* **Revision** or **commit** (noun): One version of the files at one point in time.

* **Commit** (verb): The recording of one new point in history

* **Patch** or **diff**: changes between one version and another.

* **Parent**: In git, the revision before the current one.





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

