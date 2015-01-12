Practical programming tools for researchers
===========================================

Are you a scientist who programs for a living, but have never studied
how to write software well?

Professional software developers have many tools at their disposal to
program quickly, accurately, and in large groups.  These tools are
equally, if not more, important to scientists who most deliver correct
results on dynamic projects, yet many scientists have never been
introduced to tools to make their job easier.

This course is designed for practicing scientists who want quick
techniques to make their jobs easier.  Lectures are focused on
practicality, not purity, but students will get the necessary
background to consult professional resources available on the
Internet to learn more.


Topics which will be covered:

- Version control: reproducibility of results, collaboration, and debugging.

- Unit testing: maintaining accuracy and finding bugs early.

- Debugging: using debuggers and defensive coding.

- Speeding up code: profiling and optimization.

- Introduction to algorithms and data structures.

- How to best structure code for maintainability and extendability.

- How to efficiently use the UNIX environment and high performance
  computing resources.

- Project management: publishing, managing releases, accepting
  contributions, building a community.

- Open-source software and its role in science.  Why and how to
  free your code.

These techniques will not be taught as part of one particular language
or development model, but as techniques applicable to any project.



Prerequisites and target audience
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The target audience is new PhD students in computational (not
computer) sciences and above, who have not been exposed to these
topics before.

Students should already program in some language, and have serious
preexisting projects as part of other work or studies.  Most course
examples will be in Python or C, but these languages are not required.
Students will be expected to learn specifically how to apply these
techniques to whatever language and projects they have.

This course will be to basic for someone who has previously used or
has knowledge of most topics listed.


Vital information
~~~~~~~~~~~~~~~~~

- Two credits, Eleven 1-1.5 hour course meetings.

- Tuesdays, 15:00--16:30, excluding 06.01 holiday and 17.02 evaluation
  week.

- Terms III and IV, 13 January--31 March 2014.

- Location: BECS Coffee Room, F336.

- Registration: via `Oodi <https://oodi.aalto.fi/>`_.  Course number
  is ``BECS-114.Z``.  To find the course, search the course number in
  *Spring 2015*; it is listed under the generic course name
  *Postgraduate studies*.  Please register so that I can get an
  estimated attendance.  If you do not have the right to register in
  Oodi and do not want credit, just email me (RD).

- This course website will be updated as information becomes
  available.

- Instructor: Richard Darst <richard.darst aalto.fi>.  Responsible professor:
  Jari Saramäki <jari.saramaki aalto.fi>.

Course format
~~~~~~~~~~~~~

- This is a graduate special topics seminar


- Course meetings include both both lecture and hands-on practical
  work, please be prepared to bring a computer on some days.

- Homework is minimal and practical.  Students are expected to apply
  the techniques from this class to their preexisting projects, not
  complete exercises.

- No exams

- Course format and topics will be adapted to class size and interest

- Course reading material will consist of publicly available
  tutorials and reference material online.


Schedule
~~~~~~~~

This is a proposed schedule.  All classes on Tuesday at 15:00.  Links
go to *previous* versions of tutorials, presented to my group last
year.  Until the lecture, they won't be refined.

* Day 1  (13 Jan): (a) `Introduction <intro.html>`_ (b) `Version
  control intro (git) <../git-10-minute/git-10-minute.html>`_ (c)
  `Class notes <day01.html>`_
* Day 2  (20 Jan): `Git and collaboration <../git-collaboration/gitlab-and-collaboration.html>`_ (unrevised)
* Day 3  (27 Jan): `Debugging <../debugging/debugging.html>`_ (unrevised)
* Day 4  (03 Feb): `Profiling <../profiling/profiling.html>`_ (unrevised)
* Day 5  (10 Feb): `Software testing introduction <../testing/testing.html>`_ (unrevised)
* (17 Feb: evaluation week, no class) Use time to prepare code to be tested.
* Day 6  (24 Feb): `Software testing <../testing-2/testing-2.html>`_ (unrevised)
* Day 7  (03 Mar): `Advanced git <../git-advanced/git-advanced.html>`_ (unrevised)
* Day 8  (10 Mar): `Understanding algorithms and data structures <../algorithms-data-structures/algorithms-data-structures.html>`_ (unrevised)
* Day 9  (17 Mar): The UNIX system
* Day 10 (24 Mar): `Development, free software, and science <../open-science/open-science.html>`_ (unrevised)
* Day 11 (31 Mar): Wrap-up



Why should you take this course?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software is used everywhere in the modern world, especially in
science.  There are many "computational fields" where work is
purely making calculations in code, but also almost all fields
software is used for data processing and analysis.  Software is the
ultimate in reproduciability and verifiability.  And most importantly,
analysis is less often "off-the-shelf" and scientists must create new
tools themselves.

Despite the importance of good software, scientists are rarely trained
in its use.  Imagine a physicist building a machine without a training
in basic electronics: this is many scientists.  There are many
professionals whose life is managing software.  This is not what most
scientists want to do, but the fact remains that it is an important
part of what we do.

The software of science is not just a tangential thing.  Science must
be correct.  Science must be fast.  Science must be reproducible.
Science should be open and shared.  In science, there are specific,
time-tested techniques which people use to get their answers.  People
must plan before beginning, keep good records, ensure that results are
reproducible, try to generalize, and so on.  Likewise, there are
specific time-tested techniques of software development.  If people
add a small amount of structure to their practical work (similar to an
an experimentalist writing down parameters *before* running
experiments, there can be a huge improvement in productivity.

But what is this structure?  Here are a few examples.  Version control
tracks history of code.  With this, you can retrieve the exact version
at any time in the past.  You can find old versions or determine exactly
what results are affected by a bug.  Most importantly, you can
collaborate properly.  No longer is there multiple versions for each
student, or mailing paper revisions back and forth.  Everyone does
their work, and results can be merged automatically, even if two
people edit the same file.  Automated software testing can help you
find bugs early, and keep them from appearing as your project drags on
and on.  Debuggers can help you spend less time debugging and more
time running.  A modular design can help you reuse, instead of
recreate, code.  And it goes on and on.

The purpose of this course is to help scientists to learn these
concepts.  It is not designed to be a rigorous software development
course, since that would be far too abstract.  Instead, it assumes the
audience are experienced scientific programmers, and presents
techniques one at a time, in independent packages which can be
immediately applied to actual projects.  The course also isn't
designed to teach specific tools, since scientific workflows are
incredibly diverse.  Instead, it introduces important concepts, and
the student's task is to adapt this to their specific workflow.
To take a specific example, this course won't say "here is an code
editor to use".  There are just too many valid options.  It will say
"here is something your editor should be able to do".

Science is no longer just small codes and independent projects.
Science is large, science is interdependent, and science is
collaborative.  This course will give researches the tools needed to
work and contribute in this modern world.


Resources
~~~~~~~~~

This course is open-source, licensed under the GPLv3, and all materials
are available on github and contributions are welcome.

- Course website: http://rkd.zgib.net/scicomp/

- Course source repository: https://github.com/rkdarst/scicomp/

- My wiki notes on other resources: http://rkd.zgib.net/wiki/ScientificProgramming
