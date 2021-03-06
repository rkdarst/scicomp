Gitlab and collaboration
************************

Our last talk discussed using ``git`` by yourself, on your own
project.  Sharing with version control systems is the other important
skill to learn.  That is what this talk is about.

This presentation talks about simple git collaboration.  First, it
goes through the user interface of Gitlab, which we use at BECS to
host our repositories.  Then, we discuss the git commit model, actual
git sharing, and branches.

Like the last talk, this is an introduction.  Only by using and
reading can you master this.



Before you come
===============

* Go to https://wiki.aalto.fi/display/becsintra/Gitlab and sign up for
  a BECS Gitlab account.  You need some time for the IT people to
  approve it.

* Try to set up either ssh keys or a ``~/.netrc`` file so that you can
  use git without a password


Set up your git config file.  You should have this from last time:

.. console::

   $ git config --global user.name "Your Name"
   $ git config --global user.email your.name@aalto.fi

These are important for this talk:

.. console::

   $ git config --global alias.log1 "log --oneline --graph --decorate"
   $ git config --global alias.log1a "log --oneline --graph --decorate --all"

Here are some extra aliases you might like:

.. console::

   $ git config --global alias.cm "commit -v"
   $ git config --global alias.di "diff"
   $ git config --global alias.st "status"
   $ git config --global alias.diw "diff --word-diff=color"
   $ git config --global core.editor nano            # You can set whatever editor you would like.




The Presentation
================

Outline
-------

* We'll see how teams use systems like Gitlab to coordinate
  development

* We'll see the git commit model (how they are stored and related)

* We'll see how git sends and receives changes from other repositories

* We'll discuss conflicts and resolving them

* We'll discuss branching




Gitlab
------

* It is collaboration groupware.

* It is like github, but open source so BECS can set up their own
  private copy.

* Gitlab is not git.  You can use git without gitlab or any other
  hosting site.

* BECS gitlab

  * Instructions at https://wiki.aalto.fi/display/becsintra/Gitlab

  * Accessible at https://git.becs.aalto.fi




Gitlab features
---------------

* Repository views

  * Tree view - list files, like ``git ls-tree``

  * Commit logs - history, like ``git log``

  * Diffs - differences between any two versions, like ``git diff
    v1..v2``

  * Graphs - different statistics

* Workgroup features

  * Project wiki - exactly what it says

  * Project pastebin - share bits of code

  * Project issue tracker - track things TODO and bugs

  * Pull requests - Way to keep track of changes individuals have made
    to be included in master

    * Some teams design their entire workflows around these things

* Users and groups

  * Repositories can be owned by both users and groups

  * I have made a "scicomp-class" group for our use

Project #0: everyone log into gitlab and look around.  Find the
"scicomp-class" group and the "git-demo" project.


Git commit model
----------------

* Each commit has

  - Files
  - Message and metadata
  - Pointer to parent commit(s)

* Concepts:

  - Linear history
  - Branch
  - Merge
  - Remote

.. epigraph::

   This slide and the next few are done on the markerboard.  You can
   find similar information in the git book.




Git references
--------------
* Git commits can have different "names".
* A name is a reference that points to a commit.

  - Branch
  - Tag
  - Remote branch
  - What does "checkout" do?
  - Unreferenced commits




Git vocabulary
--------------

* **commit**
* **commit hash**
* **parent**
* **branch**
* **tag**
* **merge**
* **remote**
* **pull**
* **push**




Manipulating git commits and branches
-------------------------------------
* ``git commit`` - adds a new commit, updates branch
* ``git checkout`` - updates working directory.
* ``git merge`` - merges *other* branch *to current* branch.
* This talk won't go into detail about branches.


Showing the commit graph
------------------------
* To understand what is happening, **you need to see the commit
  graph**.
* You could use a GUI
* From the shell:

  .. console::

     git log                                      # no information
     git log --oneline --graph --decorate
     git log --oneline --graph --decorate --all

* Make the aliases at the top of this talk, and use them often!



git remotes
-----------

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

  * **http** - using any web server,
    ``http://rkd.zgib.net/code/pcd.git``

  * **git** - special git server for efficiency,
    ``git://cod.zgib.net/pcd.git``

* Remotes are conceptually like branches.


Appearance of remotes
---------------------

* Remotes are seen as branches in your repository.  Getting/pushing
  changes updates that branch.

* Remotes have some name, like ``origin``.

* You can have multiple remotes.

  * ``master`` - **your** branch

  * ``origin/master`` - **upstream's** branch




Reminder: common status commands
--------------------------------

Below are the most common status commands.

* ``git status`` - what has changed and what is your current status?

* ``git log`` - long history of current branch

* ``git log1 --all`` - short history of everything, including remotes
  (use my alias above)

* ``git diff`` - diffs what has changed and is waiting for commit

Before and after everything you do, run these commands.  It will
provide you with feedback, and help a lot!




Our actual task: contributing to a project
------------------------------------------

The rest of this presentation discusses one specific problem:

* Someone has an **upstream** repository that is hosted somewhere (like
  our team repository)

* You **clone** the repository to get a linked copy of it

* You make edits to your repository

* You push the changes back to the upstream




Cloning (getting) a repository
------------------------------

* Getting another repository is called **cloning** it.

  .. console::

     $ git clone https://git.becs.aalto.fi/complex-networks/tutorial.git

* This makes a copy for you, linked to the other one

* If you have a repository and want to copy it to the server, gitlab
  has instructions to follow:


Checking remotes
----------------

* Let's look at the remotes:

  .. console::

    $ git remote -v

* Let's look at your *branches*

  .. console::

     $ git branch -avv

* A branch is one line of development.  We will work on your branch
  ``master`` and then send the changes to the branch ``origin/master``

* When you clone, your ``master`` branch is automatically linked to
  the ``origin/master`` branch.




Commands for sending/receiving code
-----------------------------------

* Get changes from remote repository but don't merge changes:

  .. console::

     $ git fetch

* Combine your code in with upstream code (simple changes):

  .. console::

     $ git merge

* Send local changes to upstream

  .. console::

     $ git push

  Before you can send things upstream, you need to have all of
  upstream changes locally.  So, every time before you ``push``, run
  ``fetch`` and ``merge``.




Typical workflow
----------------

* Before you make any chances, make sure you are up to date:

  .. console::

     $ git fetch
     $ git merge

* You do some work, committing it as you go along.

  .. console::

     # work, edit files
     $ git commit

* Before you can push code, you want to make sure that you have the
  latest copy of upstream.  Otherwise, you can't push!

  * It never hurts to do these commands some extra times.

  .. console::

     $ git fetch
     $ git merge            # these two combined are the same as ``git pull``

* Send the code back

  .. console::

     $ git push

If someone else beats you to the ``push`` after your ``git fetch``,
then it'll fail again.  In this tutorial, with everyone doing this at
the same time, this may be a problem.  You have to be fast!

Do interactive project #1 (at the bottom)



Some notes on defaults, etc
---------------------------
* These are the same:

  .. console::

     $ git pull                = git pull origin master
     $ git merge               = git merge origin/master
     $ git push                = git push origin master

* There is a default upstream repository, and default branch to merge
* To view default branch/repository, use

  .. code::

     git branch -vv

* To set default:

  .. code::

     git branch --set-upstream <local-branch> origin/<remote-branch>



Conflicts
---------

* **Conflicts** are when you modify something at the same time someone
  else.

* They not common, but you will have to deal with them eventually.

* Conflicts happen when you *merge*, and you have to **resolve** them.

* When a conflict happens, the merge aborts and
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

* ``git`` puts markers put in the code on the exact lines of conflict:
  ``<<<<<<<``, ``=======``, and ``>>>>>>>``.

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

Do interactive project #2 (at the bottom)



Working to reduce conflicts
---------------------------

* All VCSs are line-based.

  - Write in a way to make each line logical.

  - Wrap LaTeX paragraphs into lines.

* Separate big changes into different commits.

* Pull and push often!  The less difference between people, the fewer
  conflicts.








Conclusion
----------

* Gitlab is a central platform for collaboration, but not a necessary
  one

* *remotes* represent another repository and *branches* represent a
  line of development

* The key commands ``git fetch``, ``git merge``, ``get push``

* Conflicts happen when people edit the same things, but there are
  well established procedures for dealing with them

Remember: **Commit early and commit often**

If there is time, try interactive projects #3 and #4.  These are
optional.




Next steps
==========

Summary of commands
-------------------

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

* Git manual pages (same as before)

* The git book (Pro Git): http://www.git-scm.com/book/

  + Chapter 3, discusses branching, etc (very good diagrams and
    explinations here).

  + Section 3.5 discusses remotes, pushing, pulling, etc (notice it's
    in the branching chapter).  Chapter 4 is more useful if you are
    setting up a server, but 4.3 (ssh keys) and 4.8 (GitLab) may be
    useful.

  + Chapter 5 discusses practical points of running a distributed project.

* Official git documentation: http://git-scm.com/documentation

* Brain and Mind Laboratory `git micromanual <https://git.becs.aalto.fi/bml/bramila/wikis/git-micromanual>`_

* This `cool cheat sheet
  <http://ndpsoftware.com/git-cheatsheet.html>`_, starts becoming a
  bit more relevant, but still has a lot that goes beyond what we know.



Optional: merge requests (pull requests)
----------------------------------------
* New features are added in a branch
* Branch is pushed to a server
* A "pull request" is made which is discussed and accepted/rejected.
* Gitlab, github, etc, provide features to handle this.



Optional: Merge vs rebase
-------------------------

* ``merge`` leaves the two branches separate.  For big changes, it is
  better.

* ``rebase`` keeps things more linear in history, and thus less
  confusing.

* To use rebase, simply do ``rebase`` instead of ``merge``

  .. console::

     $ git fetch
     $ git rebase

* If a rebase gets too complicated, you can ``git rebase --abort`` and
  ``git merge`` instead.  You'll still have to resolve the conflict
  but it will save more history and maybe be easier.

* If you do *rebase* and there is a conflict, finalize with ``git
  rebase --continue``, for a *merge* finalize with ``git commit``


Optional: stashing uncommitted changes
--------------------------------------

* Lets say you

  * made some local changes, but are not ready to commit

  * Want to fetch or push some code.

* You can use ``git stash`` to hide changes out of the way.

* Example usage:

  * See what current changes are ``git diff``

  * Stash the code:

    .. console::

       $ git stash

  * See current changes: ``git diff```

  * Do whatever else you want to do: ``git fetch``, ``git merge``,
    ``git push``

  * *Reapply* your stashed changes:

    .. console::

       $ git stash pop

  * Look at current status: ``git diff``



Projects
========

We'll do these projects together.  Form groups of two (both people
with computers).  I made a sample ``demo.git`` project for us to
play with.

* Gitlab is at https://git.becs.aalto.fi.

* Project page: https://git.becs.aalto.fi/scicomp/demo

* git URL for cloning:
  https://git.becs.aalto.fi/scicomp/demo.git




Interactive project #1: basic usage
-----------------------------------

* Clone ``demo.git`` (git clone)

* Add a new file with your name.  Have at least 20 lines in the
  file. (edit, git commit)

* send the file upstream. (git fetch, git merge, git push)

* Verify that you see the file in gitlab.

* Fetch everyone else's file (git fetch, git merge)

* Edit a few lines in someone else's file.  Ask permission first.  No
  more than one person should edit the same file at the same time
  (that's the next project).

* Send that edit upstream.




Interactive project #2: conflicts
---------------------------------

* Find a partner.  We are going to simulate a conflict.

* You and your partner agree on one file to edit.  Make sure that only
  you two are editing it.  (In a real case, git could handle this, but
  since the files are so small and we are so many people working at
  the same time, let's keep it simple.)

* Both of you edit the same area of the file at the same time.  Don't
  make too radical changes, but have at least one line that you both
  edit.

* Both of you commit the changes at the same time.

* Both push at the same time.  Whose push succeeded?

* The person whose push was unsuccessful, fetch and try to merge.
  Resolve the conflict and send the resolution upstream.




Interactive project #3: partial commit and stashing
---------------------------------------------------

* Make two different edits in the same file

* Commit only one of the edits using ``git commit -p``

* Wait for someone else to update upstream

* Try to push and see it fails

* Try to ``git fetch`` and ``git merge`` - see that it warns you of
  local uncommited changes

* ``git stash`` the uncommited changes

* Now ``git merge`` and ``git push``

* Now ``git stash pop``



