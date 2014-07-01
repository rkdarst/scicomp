10 minute git
*************


This is a 10 minute introduction to git.  It has a very specific goal: to teach one enough to use git to store the revisions to their own projects.  It does not cover sharing repositories, using someone else's repository, branching, or any number of advanced features.  Furthermore, this is more of an introduction to version control rather than something specific to git.  It emphasizes operations that can be done with any version control system.

This is designed to be a part of an oral presentation, thus does not necessarily stand on its own.  It should serve as notes for after that presentation for further research and reading.  If you are reading this on your own, you will have to do more reading to understand things here.

Keep in mind: I can't teach you git, but I can give you ideas and your curiosity can teach you git.

Goals
-----

After completing this tutorial, you should be able to:

* Take one of your existing projects and create a git repository for it.

* Record changes in that project: for example, you might make a commit once per day, or a commit every time you add a new feature

* You will be able to use that history to see what changed on any given day, or how your project looked at any given point in time.



The tutorial
============

Before starting, run these commands

.. console::

   $ git config --global user.name "Your Name"
   $ git config --global user.email your.name@domain.fi
   $ git config --global color.ui auto

These set some standard global options for your user - your name, and making output colorful.

What is history?
----------------

* History shows you the state of your project at any time in the past

* Metadata about what you have done and when

  * *Commit title, commit description, files changed, previous version*

* Uses: debugging, reproducibility, sharing, collaborating.

* Useful for: code, papers, websites, anything textual.

  * *It can include binary files (images, pdfs, ...) but isn't the best for that*

To view history, run:

.. console::

   $ git log
   $ git log --oneline

Where is this history stored / what is a git repository?
--------------------------------------------------------

* Everything is stored in a ``.git`` directory within your project.

* Main project files are never touched unless you run a command, such as "revert to old version".

* Create the git directory with

  .. console::

     $ cd /path/to/your/project/
     $ git init

* *The specific format is simple but complicated, and each VCS works differently.  We don't need to worry about it now.*

Terminology
-----------

* **Repository**: one directory

* **Revision** or **commit** (noun): One version of the files at one point in time.

* **Commit** (verb): The recording of one new point in history

* **Patch** or **diff** or **hunk**: changes between one version and another.

* **Parent**: In git, the revision before the current one.

Adding initial files
--------------------

* Use ``git add`` to make git see and track files.

  .. console::

     $ git add *.py
     $ git add file1.txt dir/file2.txt

* *You have to use* ``git add`` *here, but* ``git add`` *has another use that I am* **not** *going to talk about, "staging"*

Making your first commit
------------------------

* Check what is going on by typing

  .. console::

     $ git status

* After you see everything, run

  .. console::

     $ git commit

* You will be prompted for a message.  Type "initial commit" or something similar. 

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

