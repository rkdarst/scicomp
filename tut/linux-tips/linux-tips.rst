

Linux and Unix tips and tricks
==============================



Outline
~~~~~~~

- Structure of this talk

  - Big list of disconnected topics
  - Briefest intro

- General Linux tips
- NBE department related tips
- Other useful software

The ``bash`` shell
~~~~~~~~~~~~~~~~~~
- A "Bourne Shell"
- Enter command, see output
- Tab completion

  - Not just for commands!

- Used for interactive work and scripting: same language
- Other alternatives: ``tcsh``, ``ksh``, ``zsh``.

Filesystems
~~~~~~~~~~~
- Mapping from files and directories to linear array of bytes

  - Example: FAT, ext2/3/4, NTFL
  - Also network filesystems

- "What filesystem is this on" --> "How is this stored?"

  - What types of properties can be stored for a file?

- Types

  - Regular ()
  - Special (``proc``, ``sys``)
  - Network (``nfs``, ``afs``)
  - High-performance (``lustre``)

Users and groups
~~~~~~~~~~~~~~~~
- Every user has a user ID (number), and username
- ``whoami``
- Each user has a primary group and other group memberships
- ``groups``
- ``id``
- Groups are set only at initial login

Filesystem layout
~~~~~~~~~~~~~~~~~
- mounts: ``mount``, ``/proc/mounts``
- ``/``
- ``/home/USERNAME/``, ``/root/``
- ``/etc/``
- ``/bin``, ``/sbin/``, ``/usr/bin``, ``/usr/sbin/``
- ``/usr/``
- ``/usr/local/``
- ``/mnt/``
- ``/var/``
- ``/dev/``
- Conventions

  - ``/`` --> filesystem root
  - ``~/`` --> Your home directory
  - ``~NAME/`` --> ``NAME``\ s home directory

Files
~~~~~
- File types

  - regular files, directories, links (devices, pipes, sockets)
  - Make links using ``ln -s destination link-name``

- Ownership and permissions

  - File has owner/group
  - File has read/write/execute permission for user/group/other

- ``ls -l`` - basic file information
- ``stat`` program - lists detailed file properties


Environment variables
~~~~~~~~~~~~~~~~~~~~~
- All processes have an **environment**: key-value mappings of general
  configuration information
- Inherited to *child* processes only (and by default).
- Used for general configuration type things.
- *Shell variable different from environment variable*
- Listing environment variables.

  .. code:: shell

     $ env

- Using a variable in shell

  .. code:: shell

     $ echo $NAME

- Setting shell variable:

  .. code:: shell

     $ NAME=value

- Setting environment variables: use ``export`` keyword.

  .. code:: shell

     $ export NAME=value
     # or
     $ NAME=value
     $ export NAME

Shell paths
~~~~~~~~~~~
- You type ``ls`` and ``/usr/bin/ls`` runs.
- The ``PATH`` variable is the *search path* for running programs
- Format: colon separated

  - ``/usr/local/bin:/usr/bin:/bin:/home/richard/bin:/home/richard/bin/bin-u``

- Other similar: ``PYTHONPATH``, ``LD_LIBRARY_PATH``, ``MANPATH``
- Key concept: search paths for programs

Processes
~~~~~~~~~
- Name and arguments
- ``stdin``, ``stdout``, ``stderr``
- Return code (integer)

Pipes
~~~~~
- Most shell magic comes from connecting programs with pipes
- Pipe directs output of one program into another
- Example:

  - ``ls`` lists files in a directory
  - ``grep`` prints only lines matching a patten
  - ``ls | grep PATTERN`` - list files matching some pattern

Useful shell programs
~~~~~~~~~~~~~~~~~~~~~
- cat, sort, tac, grep, uniq, yes, wc, uniq, find, sed, diff, xargs,
  ... very many more.
- Lists of utilities:

  - Run ``dpkg -L coreutils | grep bin``
  - http://searchenterpriselinux.techtarget.com/tutorial/77-useful-Linux-commands-and-utilities

Shell scripts
~~~~~~~~~~~~~
- Begin with ``#!/bin/sh``

  - ``#!`` is a standard magic code that means "run with this program"

Shell scripting
~~~~~~~~~~~~~~~
- Shell is a "complete" programming language
- ``if`` ... ``then`` ... ``else`` ... ``fi``
- ``for VAR in LIST ; do`` ... ``; done``
- ``while COMMAND ; do`` ... ``done``
- Advanced bash scripting guide: http://tldp.org/LDP/abs/html/
- Arguments: ``$#``, ``$0``, ``$1``, etc.

Shell aliases and functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Aliases

  - ``alias word='command args'``
  - When you run ``word`` it translates into ``command args`` +
    whatever else you put
  - Dumb argument replacement

- Functions

  - Take arguments, run arbitrary code
    ``function fullpath () ( COMMANDS )``


Process control
~~~~~~~~~~~~~~~
- ``C-z`` (Control-z) suspends a process
- ``bg`` then makes it run in the background
- ``fg`` (``fg #``) then brings it to the foreground
- ``jobs`` lists running processes
- These jobs are tied to the specific shell

``bash`` history
~~~~~~~~~~~~~~~~
- Stored in ``~/.bash_history``
- Up/down arrows
- You should never be retyping commands that exist in history!
- ``history`` command to control it

Readline library (``bash`` hotkeys)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- ``readline`` handles history and hotkeys for bash and many other
  programs.
- up/down arrow keys: scroll through history
- Search: ``C-r``, then type
- Fast substitutions: ``!$``, and so on
- Config file: ``.inputrc``

More: http://www.catonmat.net/download/readline-emacs-editing-mode-cheat-sheet.pdf

Shell configuration
~~~~~~~~~~~~~~~~~~~
- Configured via files that are read *on shell start-up only*

  - ``/etc/bash.bashrc`` and ``~/.bashrc``
  - ``/etc/profile`` and ``~/.bash_profile``

- ``source FILENAME`` to re-read
- *Use these files well* - it will make your life much more
  enjoyable.


NBE computers
~~~~~~~~~~~~~
- We have a standard shared filesystem and login setup


Installing programs
~~~~~~~~~~~~~~~~~~~
- Programs can be installed globally
- Programs can be installed to local directories

  - Update ``$PATH``, etc, to find programs

- Install globally via ``module`` system

  - ``module`` is an elaborate system for updating PATHs
  - ``module avail``
  - ``module load NAME`` and ``module unload NAME``
  - ``module show NAME``

Tour of NBE filesystems
~~~~~~~~~~~~~~~~~~~~~~~
- ``/proj/``
- ``/scratch/``
- ``/local/``
- ``/home/``

Quotas and permission problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- ``quota`` program to display quotas
- ``/home`` quotas per user
- Other quotas are *per group*

  - If files do not have the right group, quota will be zero
  - Folders must be group-writable and *sticky* so that files are made
    with the right user.

Triton
~~~~~~
- Full (good) user guide: https://wiki.aalto.fi/display/Triton/Triton+User+Guide

Batch queuing systems
~~~~~~~~~~~~~~~~~~~~~
- You must request time on a node to run

  - ``sinteractive`` - get interactive job
  - ``sbatch`` - submit job
  - ``slurm q`` - list your queued jobs

- Queues: ``play``, ``batch``, ``short``, ``hugemem``, ``gpu``


Other useful programs
~~~~~~~~~~~~~~~~~~~~~

``ssh``
~~~~~~~
- Securely connect to other computers
- An absolute workhorse of almost anything
- Most people can use it more efficiently than they do
- Good sshing practices: ssh out, not in.

Standard arguments
~~~~~~~~~~~~~~~~~~

Configuration file
~~~~~~~~~~~~~~~~~~
- Configuration comes from three places: command line,
  ``~/.ssh/ssh_config``, and ``/etc/ssh/ssh_config``.
- Example:

  ::

     Host thor
             HostName thor.becs.hut.fi
             User darstr1

     Host *
             ControlMaster   auto
             ControlPath     /tmp/.ssh-richard-mux-ssh-%r@%h:%p
             ServerAliveInterval 3600



Passwordless authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Create a keyfile: ``ssh-keygen``

  - Key *should* have a password

- ``ssh-add`` to add to type password and cache key
- Copy key to other server: ``

Connection multiplexing
~~~~~~~~~~~~~~~~~~~~~~~
- One network connection can carry multiple sessions
- Much faster startup

::

   Host *
           ControlMaster   auto
           ControlPath     /tmp/.ssh-richard-mux-ssh-%r@%h:%p

Known hosts file
~~~~~~~~~~~~~~~~
- Security concern: someone intercepts your traffic, you type in
  password and they steal it
- On first connection, you accept a host key:

  ::

    The authenticity of host 'aoeu (95.142.168.120)' can't be established.
    ECDSA key fingerprint is 78:64:4c:15:c5:8b:24:39:ee:ab:e1:e5:94:6a:16:de.
    Are you sure you want to continue connecting (yes/no)? 

- If key changes, you get this message:

  ::

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
    Someone could be eavesdropping on you right now (man-in-the-middle attack)!
    It is also possible that a host key has just been changed.
    The fingerprint for the RSA key sent by the remote host is
    d4:e8:3c:74:c7:38:b2:3c:df:6a:b7:14:5e:9a:d3:2d.
    ...
    Offending RSA key in /home/richard/.ssh/known_hosts:43
    RSA host key for boltzmann has changed and you have requested strict checking.
    Host key verification failed.

- To solve the message, remove line #43 in the file stated.


Port forwarding
~~~~~~~~~~~~~~~
::

   ssh -L <port>:<hostname>:<other-port>
   ssh -R <port>:<hostname>:<other-port>


Proxy commands
~~~~~~~~~~~~~~

::

   Host triton
       HostName triton.aalto.fi
       User darstr1
       ProxyCommand ssh-nomux amor-clear nc %h 22

   Host amor-clear
       HostName        amor.becs.hut.fi
       User            darstr1
       HostKeyAlias    amor.becs.hut.fi
       ClearAllForwardings yes



``scp`` and ``sftp``
~~~~~~~~~~~~~~~~~~~~
- Tools for copying files
- Syntax::

    scp HOSTNAME:path/to/filename   local-file

    scp local-file HOSTNAME:path/to/filename

- You can tab complete with this!
- Similar syntax to ``cp``

``sshfs``
~~~~~~~~~
- Network filesystem, operating only over ``ssh``
- Any ``ssh`` server can be mounted

::

   sshfs host:path/to/dir  local-dir/
   fusermount -u local-dir/

``rsync``
~~~~~~~~~
- Like ``scp`` but can use less bandwidth
- Also can only transfer differences

``unison``
~~~~~~~~~~
- Syncs files on two different sides
- Two-way rsync

``screen`` and ``tmux``
~~~~~~~~~~~~~~~~~~~~~~~
- Leaves shell sessions running on a remote computer
- Disconnect and reconnect

``mosh``
~~~~~~~~
- Another shell protocol, uses UDP instead of TCP so is better for
  unreliable connections
- ``mosh HOSTNAME``
- ``ssh`` config file still in effect here!

Graphical programs (X11)
~~~~~~~~~~~~~~~~~~~~~~~~
- ``X11`` is the name of Linux graphical protocol - network protocol.
- ``$DISPLAY`` environment variable controls graphical programs
- Can be tunneled over SSH - automatic using ``-X`` or ``-Y`` options.


``nx``, ``x2go``, ``x11vnc``, etc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Like screen, but for X11 sessions

Other
~~~~~
- ``meld`` - graphical diff and merge utility
- ``units`` - powerful unit converter
- ``cron`` - run commands periodically
- ``lsof`` - list open files
- ``df``, ``du -sh path/to/* | sort -h``
- ``less``
- ``find``
- ``file`` - detect type of file based on contents
- ``man`` - command manual pages

