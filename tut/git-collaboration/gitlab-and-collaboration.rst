Gitlab and collaboration
************************

This presentation talks about simple git collaboration.  First, it goes through the user interface of Gitlab, which we use at BECS to host our master repositories.  We then talk a minimal process to clone (get a copy of) a repository there, edit it, and push changes back.

Remember, I can't teach you git.  I can give you some ideas, and your curiosity will teach you.  Also, there are a lot of other medium-advanced features which can really help you that I am not even talking about.

Before you come
===============

* Go to https://wiki.aalto.fi/display/becsintra/Gitlab and sign up for a BECS Gitlab account.  You need some time for the IT people to approve it.

* Email rkd to add you to the complex networks group.

* Try to set up your ``~/.netrc`` file, see the page above (ssh keys are better, if you have them).

  ::

     machine git.becs.aalto.fi login USERNAME password PASSWORD

Set up your git config file:

.. console::

   $ git config --global user.name "Your Name"
   $ git config --global user.email your.name@aalto.fi
   $ git config --global alias.log1 "log --oneline --graph --decorate"
   $ git config --global core.editor nano            # You can set whatever editor you would like.

Here are some personal aliases you might like:

.. console::

   $ git config --global alias.cm "commit -v"
   $ git config --global alias.di "diff"
   $ git config --global alias.st "status"
   $ git config --global alias.diw "diff --word-diff=color"

The Presentation
================

Outline
-------

* We'll see how teams use things like Gitlab to coordinate development

* We'll see how git sends and receives changes from other repositories

* We'll discuss how to contribute to a project, and do some examples 

Gitlab
------

* It is collaboration groupware.

* It is like github, but open source so BECS can set up their own private copy.

* Gitlab is not git.  You can use git without gitlab or any other hosting site.

* BECS gitlab

  * Instructions at https://wiki.aalto.fi/display/becsintra/Gitlab

  * Accessible at https://git.becs.aalto.fi

Gitlab features
---------------

* Repository views

  * Tree view - list files, like ``git ls-tree``

  * Commit logs - history, like ``git log``

  * Diffs - differences between any two versions, like ``git diff v1..v2``

  * Graphs - different statistics

* Workgroup features

  * Project wiki - exactly what it says

  * Project pastebin - share bits of code

  * Project issue tracker - track things TODO and bugs

  * Pull requests - Way to keep track of changes individuals have made to be included in master

    * Some teams design their entire workflows around these things

* Users and groups

  * Repositories can be owned by both users and groups

  * I have made a "complex networks" group for our use

Project #0: everyone log into gitlab and look around.  Find the "complex networks" group and the "drvo" project.

git remotes
-----------

* Git *remote*: a separate location for code that can be linked to your repository

  * This is the fundamental unit of sharing code

  * You can look at code in the remote, and pull and push code from them.

* Three ways of remote access: 

  * **local filesystem** - on same computer, ``/proj/networks/darst/pcd/``

  * **ssh** - anything accessable via ssh, ``darstr1@amor.becs.hut.fi/proj/networks/darst/pcd/``,

  * **http** - using any web server, ``http://rkd.zgib.net/code/pcd.git``

  * **git** - special git server for efficiency, ``git://cod.zgib.net/pcd.git``

* A *branch* is one independent line of development.  I won't discuss them more, but

  * Remotes are seen as branches in your repository.  Getting/pushing changes updates that branch.

  * I won't go into branches in any detail, but:

    * ``master`` - **your** branch

    * ``origin/master`` - **upstream's** branch

Reminder: common status commands
--------------------------------

Below are the most common status commands.

* ``git status`` - what has changed and what is your current status? 

* ``git log`` - long history of current branch

* ``git log1 --all`` - short history of everything, including remotes (use my alias above)

* ``git diff`` - diffs what has changed and is waiting for commit

Before and after everything you do, run these commands.  It will provide you with feedback, and help a lot!

Our actual task: contributing to a project
------------------------------------------

  The rest of this presentation discusses one specific problem:

* Someone has an *upstream* repository that is hosted somewhere (like our team repository)

* You *clone* the repository to get a linked copy of it

* You make edits to your repository

* You push the changes back to the upstream

Cloning (getting) a repository
------------------------------

* Getting another repository is called **cloning** it. 

  .. console::

     $ git clone https://git.becs.aalto.fi/complex-networks/tutorial.git

* This makes a new repository linked to the old one

* Let's look at the remotes:

  .. console::

    $ git remote -v

  *origin* is the conventional name for the upstream.

* Let's look at your *branches*

  .. console::

     $ git branch -avv

* A branch is one line of development.  We will work on your branch ``master`` and then send the changes to the branch ``origin/master``

* When you clone, your ``master`` branch is automatically linked to the ``origin/master`` branch.

Commands for sending/receiving code
-----------------------------------

* Get changes from remote repository but don't update local copies with them

  .. console::

     $ git fetch

* Combine your code in with upstream code (simple changes): 

  .. console::

     $ git rebase

* Send local changes to upstream

  .. console::

     $ git push

  Before you can send things upstream, you need to have all of upstream changes locally.  So, every time before you ``push``, run ``fetch`` and ``rebase``.

Note: we found that ``amor`` has an older git version.  On ``amor``, do ``git rebase origin/master``

Typical workflow
----------------

* Before you make any chances, make sure you are up to date:

  .. console::

     $ git fetch
     $ git rebase

* You do some work, committing it as you go along.

  .. console::

     $ git commit
     $ git commit

* Before you can push code, you want to make sure that you have the latest copy of upstream.  Otherwise, you can't push!

  * It never hurts to do these commands some extra times.

  .. console::

     $ git fetch
     $ git rebase

* Send the code back

  .. console::

     $ git push

If someone else beats you to the ``push`` after your ``git fetch``, then it'll fail again.  In this tutorial, with everyone doing this at the same time, this may be a problem.  You have to be fast!

Do interactive project #1 (at the bottom)

Conflicts
---------

* Conflicts are when you modify something at the same time someone else does

* They are a infrequent but an issue in every shared workflow, and every VCS has tools to handle them.

* When a conflict happens (on merge or rebase), the process aborts and you have to *resolve* the conflict.

  * Git generally has pretty good error messages - **read them** and follow instructions.  Don't forget or miss it, it will be bad for everyone.

  * First, it shows an error message

    ::

       CONFLICT (content): Merge conflict in FILENAMES
       Failed to merge in the changes.
       Patch failed at 0001 PATCH_NAME

       When you have resolved this problem run "git rebase --continue".
       If you would prefer to skip this patch, instead run "git rebase --skip".
       To check out the original branch and stop rebasing run "git rebase --abort".

  * Note the explicit instructions at the bottom.

How to resolve conflicts
------------------------

* git puts markers put in the code on the exact lines of conflict

* ``git diff`` shows the conflicting lines

  .. console::

     $ git status          # show the files that are unresolved and resolved.
     $ git diff            # show what is unresolved

* You need to resolve the conflicts so that it is consistent.  Look and edit it.

* Run the command it says to continue.

  .. console::

     $ git add FILE
     $ git rebase --continue

  **Don't do** ``git commit`` **to finish things, use** ``git rebase --continue``

* Finish with ``git status`` and ``git log1`` and ``git diff`` to make sure everything is there.

Conflict notes
--------------

* Generally, conflicts are rare and not that bad when they occur.

* They **can** be bad if two people are working on the exact same code, for example two people rewriting the same function.

  * But that's the case with any VCS, because you are literally doing the same thing two different ways.

* However you resolve the conflict, the full history is still there so someone can always go back and do it differently later.

* Semantic conflicts - two incompatible changes that don't touch the same code, like renaming a function.  VCS don't detect these.

* If you forget to do ``rebase --continue`` then there will be big problems!

* As long as you have committed code at one point in time, it is relatively safe and won't get lost.  If you get into a bad situation, ask someone before it's too late and they can help.  **Commit before rebasing**.

Do interactive project #2 (at the bottom)

Optional: Merge vs rebase
-------------------------

* ``rebase`` keeps things more linear in history, and thus less confusing.

* ``merge`` leaves the two branches separate.  For big changes, it is better.

* To use merge, simply do ``merge`` instead of ``rebase``

  .. console::

     $ git fetch
     $ git merge

* If a rebase gets too complicated, you can ``git rebase --abort`` and ``git merge`` instead.  You'll still have to resolve the conflict but it will save more history and maybe be easier.

* If you do **rebase** and there is a conflict, finalize with ``git rebase --continue``, for a **merge** finalize with **git commit**

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

  * Do whatever else you want to do: ``git fetch``, ``git rebase``, ``git push``

  * *Reapply* your stashed changes:

    .. console::

       $ git stash pop

  * Look at current status: ``git diff``

Conclusion
----------

* Gitlab is a central platform for collaboration, but not a necessary one

* *remotes* represent another repository and *branches* represent a line of development

* The key commands ``git fetch``, ``git rebase``, ``get push``

* Conflicts happen when people edit the same things, but there are well established procedures for dealing with them

Remember: **Commit early and commit often**

If there is time, try interactive projects #3 and #4.  These are optional.

Next steps
==========

This section will have follow-up information later.

To discuss (eventually):

* What permissions and ownerships should we have on the repositories?

* How do we want to manage our own shared stuff?

*

Projects
========

We'll do these projects together.  Form groups of two (both people with computers).  I made a sample ``tutorial.git`` project for us to play with.

* Gitlab is at https://git.becs.aalto.fi.

* Project page: https://git.becs.aalto.fi/complex-networks/tutorial

* git URL for cloning: https://git.becs.aalto.fi/complex-networks/tutorial.git

Interactive project #1: basic usage
-----------------------------------

* Clone ``tutorial.git`` (git clone)

* Add a new file with your name.  Have at least 20 lines in the file. (edit, git commit)

* send the file upstream. (git fetch, git rebase, git push)

* Verify that you see the file in gitlab.

* Fetch everyone else's file (git fetch, git rebase)

* Edit a few lines in someone else's file.  Ask permission first.  No more than one person should edit the same file at the same time (that's the next project).

* Send that edit upstream.

Interactive project #2: conflicts
---------------------------------

* Find a partner.  We are going to simulate a conflict.

* You and your partner agree on one file to edit.  Make sure that only you two are editing it.  (In a real case, git could handle this, but since the files are so small and we are so many people working at the same time, let's keep it simple.)

* Both of you edit the same area of the file at the same time.  Don't make too radical changes, but have at least one line that you both edit.

* Both of you commit the changes at the same time.

* Both push at the same time.  Whose push succeeded?

* The person whose push was unsuccessful, fetch and try to rebase.  Resolve the conflict and send the resolution upstream.

* Do the same thing as the last step, but resolve the conflict using 'merge' instead of 'rebase'.

Interactive project #3: merging
-------------------------------

* Same as #2, but do a merge.

* Look and see how it looks different in the gitlab "network" view.

Interactive project #4: partial commit and stashing
---------------------------------------------------

* Make two different edits in the same file

* Commit only one of the edits using ``git commit -p``

* Wait for someone else to update upstream

* Try to push and see it fails

* Try to ``git fetch`` and ``git rebase`` - see that it warns you of local uncommited changes

* ``git stash`` the uncommited changes

* Now ``git rebase`` and ``git push``

* Now ``git stash pop``



