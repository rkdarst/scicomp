Information for day 1: version control system introduction
==========================================================

This page is the companion

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


"Homework"
~~~~~~~~~~
* You are expected to have to do some reading yourself!
* Explore the repository for this course on Github:
  https://github.com/rkdarst/scicomp/

  - Find the changelog (history)
  - Find how to view diffs of commits
  - Find how to view the "annotations" (who last edited each line) of files
  - When was the project started?

* Create a git repository for one of your own projects
* Use the repository for one week, making commits as you work.  Try to
  maintain good development practices

  - Commit often enough
  - Have good commit messages

* Try to use each of these commands (you may have to read some)

  - ``git status``
  - ``git log``
  - ``git log -p``
  - ``git log --stat``
  - ``git commit -p``
  - ``git commit --amend``


* Send me the commit log once you have been using the project for a
  week

  - You can get this log by ``git log > git-log.txt``
