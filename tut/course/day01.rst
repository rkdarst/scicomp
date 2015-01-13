Information for day 1: version control system introduction
==========================================================

This page is the companion to day 1 lecture: before-class notes and
after-class assignments.

What version control system to use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In the class, I teach the basics of the ``git`` version control
system.  It is one of many different systems.  Perhaps it is not the
most simple to use, but it is the most common with a lot of support.
You should discuss with your group and see what people use, and adopt
that.

The most common systems are:

* `git <http://www.git-scm.com/>`_
* `Mercurial <http://mercurial.selenic.com/>`_ (hg)
* `Subversion <https://subversion.apache.org/>`_ (not a distributed
  version control system, so I wouldn't recommend this for personal
  projects)


Installation of git
~~~~~~~~~~~~~~~~~~~
Whatever system you choose, you will need to install it yourself.  It
is already installed on all BECS-managed Linux and Windows computers.

The git web page has information on downloading and installation.  One
advantage of git is that it is so common, there are many resources and
different packages.

The "official" distributions can be downloaded from
http://www.git-scm.com/downloads .

"Git" is a general concept.  There is more than one program that can
interact with the repositories.  So, for example, there is a GitHub
package, ``git-cola`` is a graphical user interface, and many editors
(integrated development environments) will directly interface with the
repository, so that you don't have to use the command line.

Post-lecture notes
~~~~~~~~~~~~~~~~~~
* I did not cover the "staging area", also known as the "index".  This
  is an intermediate area between ``git add`` and ``git commit``.  The
  way I taught the class, I just use ``git commit`` with filenames or
  ``-a`` and bypass the staging area.  For big complicated commits, I
  might use the staging area, but for the most part it is just extra
  work.


"Homework"
~~~~~~~~~~
* You are expected to have to do some reading yourself!  If you read
  any tutorial now, you will learn a lot.

* Explore the repository for this course on Github:
  https://github.com/rkdarst/scicomp/

  - Find the changelog (history)
  - Find how to view diffs of commits
  - Find how to view the "annotations" (who last edited each line) of files
  - When was the project started?
  - On what day did I make this particular file
    (``tut/course/day01.rst``)?

* Create a git repository for one of your own projects
* Use the repository for one week, making commits as you work.  Try to
  maintain good development practices

  - Commit often enough
  - Have good commit messages

* Consider making some aliases.  Read about it, but hint: ``git
  config --global alias.NAME "<command>"``.  Here are some of my most
  common aliases that are relevant to day 1:

  - ``git config --global alias.cm "commit -v"``
  - ``git config --global alias.cmp "commit -v -p"``
  - ``git config --global alias.co checkout``
  - ``git config --global alias.di diff``
  - ``git config --global alias.diw "diff --word-diff=color"``
  - ``git config --global alias.log1 "log --oneline --graph --decorate"``
  - ``git config --global alias.log1a "log --oneline --graph --decorate --all"``
  - ``git config --global alias.st status``
  - We will get more aliases later.  You should also start making up
    your own.

* Learn what each of these commands does, and try using it.  Some are
  from the class, some you will have to learn (Either web search or
  read the command manual pages).  Yes, it's kind of a lot.  Go slow
  and use them as you need them.

  - ``git status`` (What has changed)
  - ``git log`` (Basic log)
  - ``git log -p`` (Log with diffs)
  - ``git log --stat`` (Log with diffstat: what files changed)
  - ``git log --oneline`` (Log, short version)
  - ``git ls-files`` (List currently tracked files)
  - ``git commit``  (Basic commit)
  - ``git commit -p`` (Commit, manual selection of what to commit)
  - ``git commit --amend`` (Change most recent commit)
  - ``git commit -m "<commit message>"``  (Specify message on command line)
  - ``git annotate <filename>`` (View source commit of each line)
  - ``git show <commit hash>`` (Show old commit diffs)
  - ``git show <commit hash>:`` (Note the colon.  Show files present
    in that commit)
  - ``git show <commit hash>:filename`` (Show old versions of files)
  - ``git diff <commit hash>``  (Diff from that version to current version)
  - ``git diff <commit hash>..<commit hash>``  (diff between two
    arbitrary points)
  - ``git diff --word-diff=color``   (Word diff)
  - ``git checkout <filename>`` (Reverts changes.  Warning: changes your files)
  - ``git checkout -p <filename>``   (Reverts changes.  Warning: changes your files)
  - ``git checkout -p <commit hash> <filename>`` (Reverts changes to
    an older version.  Warning: changes your files)

* Remember to keep your ``git status`` clean by keeping a good
  ``.gitignore`` file!

* **Actual assignment:** Send me the commit log of one of your
  repositories once you have been using the project for a week.

  - You can get this log by ``git log > git-log.txt``
