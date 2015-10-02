
Scientific Software Development tutorials
=========================================

This is the index of tutorials on software development for scientific
computing basics.  These are not specific to *high-performance*
computing (yet), but introduce the standard tools that professional
devolpers already have which solve the *practical* problems in writing
code: tracking revisions, debugging, making it correct, making it
fast, and so on.  Basically, the raw material that scientists need in
order to do their work the best.

The format is designed to be short packets of tools or ideas which can
be immediately used, not detailed theory.  If talks come in groups of
two, the first is a discussion about why and how we might want to use
some tool, and the second is a practical (and hands-on) introduction
to the topic.


This project is still new, so you still see the versions for each
specific audience (and partially incomplete or buggy, depending on the
state when it was presented).  This page has existed only a few weeks,
so is under active development.  Also, a new tutorial hopefully
appears every 2-3 weeks, or whenever I can present them.

Courses
~~~~~~~

These tutorials were transformed into an informal course at the Aalto
University Department of Biomedical Engineering and Computational
Science, during the Spring 2015 term.  Course information is available
at `the course page <course/>`_

In June 2015, the `git <scip2015/git.html>`_, `debugging
<scip2015/debugging.html>`_, and `profiling
<scip2015/profiling.html>`_ (and an `introduction
<scip2015/intro.html>`_ talks were given at `Scientific Computing in
Practice 2015 <http://science-it.aalto.fi/scip/kickstart2015/>`_.
These tutorials are made more concise and hands-on compared to the
ones below.

Tutorials
~~~~~~~~~

Tutorials are created to serve two purposes at the same time, a) a
presentation to be given in a lecture or workshop format, and b) a
notes format that can be read independently after the lecture.  To
save work and make the product most useful, both of these formats are
combined in the same documents.  In the presentation version, you see
a "slide version" (use left/right arrows to scroll) followed by a
hidden box of details.  In the normal version, the box of details is
larger and should roughly cover what should be said in a presentation
(but sometimes in more detail).

This project is new, and thus different tutorials have various phases
of completeness.  Some have just the presentation part completed, some
are in an older format.

.. tut-index::

   git-10-minute/git-10-minute          10 Minute Git
   git-collaboration/gitlab-and-collaboration  Gitlab and collaboration
   testing/testing                      Introduction to software testing
   testing-2/testing-2                  Software testing with Python
   debugging/debugging                  Debugging
   profiling/profiling                  Profiling
   git-advanced/git-advanced            Advanced git usage
   algorithms-data-structures/algorithms-data-structures Understanding algorithms and data structures
   linux-tips/linux-tips                Linux tips and tricks
   open-science/open-science            Open science and software development
   db-intro/db-intro                    Introduction to use of databases in research
   db-intro/db-examples                 SQL intro by examples
   git-practical/git-practical          Git: GUIs and practical issues.
   git-reference/git-reference          Git reference information


The following tutorials are "under development": they have some
content, but have not been presented yet and thus are not fully
structurally sound:

.. tut-index::

   practical/practical-correct-programs  Practical suggestions for writing good programs.  Putting all the other tutorials together.


Other information
~~~~~~~~~~~~~~~~~

Similar or other resources:

 - http://software-carpentry.org/lessons.html  Software Carpentry is
   an organization dedicated to teaching these same skills to
   scientists.
 - http://rkd.zgib.net/wiki/ScientificProgramming  My wiki page which
   I use to collect more resources.
 - https://github.com/rkdarst/scicomp/  Github project.

Future tutorials will include:

- Algorithms and data structures: computational complexity and writing efficient code.
- Optimization of Python
- Random useful science software
- Using Triton (and other HPC systems)
- Group library work
- Getting data: structured vs unstructured data, scraping, storage, parsing.

