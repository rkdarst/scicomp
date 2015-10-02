Git reference
=============


Summary
~~~~~~~
- The purpose of this is to be a single reference for all git
  commands needed, sorted by purpose.
- This isn't a normal tutorial.


Aliases
~~~~~~~

Basic configuration
~~~~~~~~~~~~~~~~~~~

.. code::

   git config --global user.name "Your Name"
   git config --global user.email your.name@domain.fi


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



.. code::

   git config --global core.excludesfile ~/.gitignore

   git config --global alias.new "log HEAD..HEAD@{upstream}"
   git config --global alias.news "log --stat HEAD..HEAD@{upstream}"
   git config --global alias.newd "log --patch HEAD..HEAD@{upstream}"
   git config --global alias.newdi '!git diff "$(git merge-base HEAD HEAD@{upstream})..HEAD@{upstream}'

   git config --global alias.rec  "!git --no-pager log --oneline --graph --decorate -n5"
   git config --global alias.reca "!git --no-pager log --oneline --graph --decorate -n10 --all"
   git config --global alias.recd "log --decorate --patch"
   git config --global alias.recs "!git --no-pager log --oneline --graph --decorate -n5 --stat"
   git config --global alias.recu "!git --no-pager log --oneline --graph --decorate @{upstream}^..HEAD"


   git config --global difftool.latexdiff.cmd '/proj/networks/darst/bin/git-latexdiff-helper "$LOCAL" "$REMOTE"'
   git config --global alias.latexdiff "difftool -t latexdiff"

   git config --global difftool.diffpdf.cmd 'diffpdf "$LOCAL" "$REMOTE"'
   git config --global alias.diffpdf "difftool -t diffpdf"
