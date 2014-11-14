Advanced git usage
==================


Purpose of this talk
~~~~~~~~~~~~~~~~~~~~


* We have already studied all the version control basics.
* This will review some of the tricky points, such as branches and
  merging.
* We will also cover different tips, tools, and use cases of git.


Important aliases
~~~~~~~~~~~~~~~~~
* Git has *many* configuration options that can make your life easier.
* I'll save you time by giving you my most important aliases.

.. code::

   git config --global alias.br branch
   git config --global alias.cm "commit -v"
   git config --global alias.co checkout
   git config --global alias.di diff
   git config --global alias.diw "diff --word-diff=color"
   git config --global alias.dis "!git --no-pager diff --stat"
   git config --global alias.fe fetch

   git config --global alias.log1 "log --oneline --graph --decorate"
   git config --global alias.log1a "log --oneline --graph --decorate --all"

   git config --global alias.rbu "rebase --interactive --autosquash HEAD@{upstream}"
   git config --global alias.rbi "rebase --interactive --autosquash"
   git config --global alias.rb "rebase --autosquash"

   git config --global alias.st status
   git config --global diff.wordregex "[a-zA-Z0-9_]+|[^[:space:]]"

   git config --global core.pager "less -RS"
   git config --global color.ui "auto"

   git config --global merge.conflictstyle diff3
   git config --global rebase.autosquash true

   git config --global "url.git@git.becs.aalto.fi:.insteadof" "becs:"
   git config --global "url.git@git.becs.aalto.fi:rkdarst/.insteadof" "becsrkd:"



Graphical user interfaces (GUIs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* I always use the git command line...
* ... but there are some GUIs that provide a simpler interface.
* Can use for (almost) anything you can do from command line

GUIs include:

* git gui
* gitk
* gitg
* git-cola


.. epigraph::

   Unfortunately, I don't use the GUIs that much, so I can't compare
   them too much.

   I will try to go show the GUI use for each thing we do in this
   talk.



Git manual pages
~~~~~~~~~~~~~~~~

* ``git <command> --help``
* ``man git-<COMMAND>``
* These have a lot of good ideas and explanation
* and are well written.




Git commit model
~~~~~~~~~~~~~~~~
Let's review how git commits work.

* A commit stores the (full) current version of all files.
* Commits one parent commit that is the previous version.
* Branches and tags are pointers to a particular version.

All git commits form a giant *directed acyclic graph*.

.. epigraph::

   This is done on the board.



Git merges vs rebases
~~~~~~~~~~~~~~~~~~~~~
Merges

* Form (acyclic) loops when two branches come together.

Rebases

* "rebase" is "move commits from one branch to another"

.. epigraph::

   This is done on the board.



Getting information
~~~~~~~~~~~~~~~~~~~
* I didn't learn git right away
* I learned the most by running commands and seeing the outcome
* You have to have the tools to see what is going on!



``git status``
~~~~~~~~~~~~~~
``git st``

Shows you:

* What files have been modified
* If you have a merge in progress, or changes staged for commit.
* You want this to be clean-looking!

.. epigraph::

   Use your .gitignore file well!



Global ``.gitignore``
~~~~~~~~~~~~~~~~~~~~~

Config:

.. code::

   git config --global core.excludesfile ~/.gitignore

* Use ``~/.gitignore`` (in your home directory) to ignore common things

  * Editor temporary files
  * Compiled files, pdfs, etc.

* My ``.gitignore`` file is this::

    *~
    .#*#
    *.pyc
    *.pyo



``git log1a``: Viewing the git graph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``git log1a``

This visually shows:

* All commits in a directed acyclic graph
* Parentage of all commits
* All branches and tags

.. epigraph::

   This uses one of my aliases, and is equivalent to ``git
   log --oneline --graph --decorate --all``.

   **Use git log1a**.  This single command has taught me more about
   git than anything else.



Showing diffs with the log
~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``git log -p``
* ``git log1a -p``
* Useful for a quick summary of what is going on.

.. epigraph::
   * ``git log --stat``



Looking at a specific commit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``git show <commit-id>`` - shows a diff
* ``git show <commit-id>:filename.txt`` - shows a file
* ``git show <commit-id>:`` - lists files at that time



``git annotate``: From where did a line come?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``git annotate <filename>`` shows the commit that introduced every
  line in a file
* Answers questions like

  * Where did this bug come from?
  * Who wrote this line?

.. epigraph::

   If you want to see the annotation of a file at some point in the
   past, use ``git annotate <filename> <commit-id>``.



Making commits
~~~~~~~~~~~~~~


What is the best commit model?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Daily work approach
* Feature approach

  * Possibly with branches?


Branches
~~~~~~~~


Branches and remotes
~~~~~~~~~~~~~~~~~~~~

* There is no logical difference between your branches and other
  people's branches.
* The server looks like a branch ``origin/master``, as seen in ``git log1a``

* ``git remote``
* ``git push``
* ``git fetch``



Tags
~~~~
* ``git tag <tag-name>``
* Use tags to make a permanent mark on a commit
* Example: published versions, submitted versions of papers.



Merge vs rebase
~~~~~~~~~~~~~~~
When do you merge and when do you rebase?

Merging

* Less risky because it doesn't change history
* Appears in history forever

Rebasing

* Changes history by rewriting commits to apply to another branch
* Should *only* be done locally



Fetch vs pull vs merge
~~~~~~~~~~~~~~~~~~~~~~
* ``git fetch``: shows you what is in remote
* ``git merge``: connects other branch to your branch
* ``git pull``: ``fetch`` + ``merge``



Advantages of fetching
~~~~~~~~~~~~~~~~~~~~~~
* I always fetch before I rebase
* This lets me see changes before I merge.
* I use the two commands to see

.. epigraph::

   The rec and new commands require the upstream brranch (tracking
   branch) to be set right.  ``git branch --set-upstream``

   .. code:: shell

     git config --global alias.new "log HEAD..HEAD@{upstream}"
     git config --global alias.news "log --stat HEAD..HEAD@{upstream}"
     git config --global alias.newd "log --patch HEAD..HEAD@{upstream}"
     git config --global alias.newdi "diff $(git merge-base HEAD HEAD@{upstream})..HEAD@{upstream}"

     git config --global alias.rec "!git --no-pager log --oneline --graph --decorate -n5"
     git config --global alias.reca "!git --no-pager log --oneline --graph --decorate -n10 --all"
     git config --global alias.recu "!git --no-pager log --oneline --graph --decorate @{upstream}^..HEAD"



Exercise 1: pushing and pulling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Go to directory ``exercise-1``
* Run ``git log1a`` to understand the current situation
* Run ``git fe`` to fetch from the server (``git fetch``)

  * Observe the appearance of the ``origin/master`` branch
  * ``git log1a -p`` to see what is new.

* Run ``git co master`` and then ``git merge origin/master``

  * This merges in ``origin/master`` to ``master``
  * Examine the situation before and after every command!


.. epigraph::

   Try using the ``recu`` command (above) to see what is new.

   Files are here:

   http://rkd.zgib.net/scicomp/git-advanced-exercises.tar.gz

Resolving conflicts
~~~~~~~~~~~~~~~~~~~
Conflicts are one of the most confusing things for people.

* Conflicts come from two people (or branches) editing the same
  thing at the same time.

  * Non-VCS handling: only one person edits at once!

* What do the edits mean?  Look at them individually.



Practical conflict handling ideas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Level 0: One person edits at a time (git just has
  history+synchronization)
* Level 1: People communicate to work on alternative areas
* Level 2: Communicate before big changes in one area.
* Level 3: Commit often enough to figure out.



Conflict workflow
~~~~~~~~~~~~~~~~~
* Make sure everything is committed
* Run ``git log1a`` and ``git st``
* Run ``git merge``.  Read output.

  * Run ``git st`` and ``git di`` to see the problem.
  * Edit files that need merging.
  * Run ``git commit`` to finalize merge.

* Run ``git log1a`` and ``git st`` to see final result.

.. epigraph::

   Notice that half of these commands are "carefully examine the
   situation".  This is for a reason!





Exercise 2: merge a conflict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Change to directory ``exercise-2``
* Exercise: Merge ``branch-2`` into master:

  * ``git co master``
  * ``git st``, ``git log1a``, etc.
  * ``git merge branch-2``: pulls ``branch-2`` into master.

* Examine the situation before and after every command!

.. epigraph::

   Files are here:

   http://rkd.zgib.net/scicomp/git-advanced-exercises.tar.gz



``git-latexdiff``
~~~~~~~~~~~~~~~~~
Config options:

.. code:: shell

  git config --global difftool.latexdiff.cmd '/proj/networks/darst/bin/git-latexdiff-helper "$LOCAL" "$REMOTE"'
  git config --global alias.latexdiff "difftool -t latexdiff"

Usage: ``git latexdiff filename.tex``

* I use this when looking at whole changes in a paper

.. epigraph::

   You *must* use the ``filename.tex`` argument or it won't work.

   Normal diff specification options work, such as ``git diff
   <commit-id-1>..<commit-id-2> filename.tex``

   The path ``/proj/networks/darst/bin/git-latexdiff-helper`` works on
   BECS computers.  I found the prototype of this script online, and
   modified it to work better for papers with figures, bibtex, etc.
   If something doesn't work right (which will happen sometimes), let
   me know.



``diffpdf``: View changes to one PDF figure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Config options:

.. code:: shell

  git config --global difftool.diffpdf.cmd 'diffpdf "$LOCAL" "$REMOTE"'
  git config --global alias.diffpdf "difftool -t diffpdf"

* I use this when updating one figure in a paper




