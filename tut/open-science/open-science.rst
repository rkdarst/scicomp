Open science
============




Science and Software development
--------------------------------

* Free software and science
* Software development strategies
* Project management and participation
* How to design software

These topics aren't for primary scientific purposes, but help you to
become better rounded.

.. epigraph::

   The things we cover today aren't direct, small tools that you can
   apply to your projects, like most other talks.  Instead, these are
   important for general education purposes.  On goal of this course
   is designed to help you transfer to a professional company doing
   software development, and today does that.

   - Free software: One should know how and why code should be
     released under a Free license, so that others can use it and
     build on your work.  Science isn't just algorithms in papers, but
     code can greatly increase the pace, too.  Of course, the code
     needs to be good for this to be useful.  That's what all the rest
     of the course is about.

   - Software development strategies: This isn't going to be
     immediately useful, since trying to impose structure on your work
     is hard.  Instead, you will learn about some development
     strategies so that in the future, you can join and work on larger
     teams.  Perhaps it will even help you to work with your
     colleagues better.  This is kind of academic/theoretical.

   - Project management and participation: This is the practical side
     of the previous topic.  It has concrete ideas that can even help
     your group to work together.

   - How to design software: This is a bit abstract.  It packages a
     lot of the tools we have learned so far, and provides some
     closing lessons on code modularity, reuse, and so on.

Free software and licenses
--------------------------


Free Software
~~~~~~~~~~~~~

* Movement started in 1980s
* Other names: "Open Source", "FLOSS" (free libre open source software)
* Started as reaction to closing nature of software in 1970s
* What science should be


Free software principles
~~~~~~~~~~~~~~~~~~~~~~~~
* Freedom to run program for any purpose
* Freedom to understand how the program works ("open source")
* Freedom to redistribute
* Freedom to modify and improve, and share your improvements.

**Not** the same as:

* "Freely distributed"
* "Open source"
* Source code on someone's web page


Contrasts to other ideas
~~~~~~~~~~~~~~~~~~~~~~~~
* Commercial software: FS can be a business strategy.
* "Freely distributed": Can't be adapted, improved, and re-shared.
* "Open source": sometimes a marketing term, can't be shared/modified.
* "Non-commercial": FS allows commercial use.

Why you need a license
~~~~~~~~~~~~~~~~~~~~~~
* Everything is copyright by default (thanks, big corporations)

  - No permission to re-share or modify and reshare.

* You probably want to disclaim warranty.

Types of licenses
~~~~~~~~~~~~~~~~~
* No license

  - Can not be re-shared.  Status questionable.

* BSD/MIT: most liberal

  - Do whatever you want, no warranty, attribute copyright.

* Gnu General Public License (GPL): "copyleft" (virulent)

  - Do whatever you want, but modifications must also be GPL.

* (Gnu) Affero General Public License (AGPL): "copyleft" for webapps

  - Like GPL, but closes the webapp loophole.

How to apply a license
~~~~~~~~~~~~~~~~~~~~~~
* Minimum: put the license file in your repository
* Best:

  - Headers in each file saying authors, license, and year.
  - Include full text of licenses in repository.

License compatibility
~~~~~~~~~~~~~~~~~~~~~
* You want to build on others, and you want others to build on you.
* Not every license can be mixed.
* GPL is "virulent": derivative works must also be GPL

  - **Keeps derivatives free**

Recommendations
~~~~~~~~~~~~~~~
* Simpler is better: stick to something standard
* BSD if proprietary use is OK
* GPL if derivatives should be kept "public"
* Join another free project: bigger audience for your work



Software development workflows
------------------------------


Software development workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* This section: "textbook" ways to develop software

  - As opposed to just writing code and hoping something good comes
    out.

* I don't expect you to go adopting these...

  - ... but they will help you think about what you do
  - ... and be useful for future jobs.


"Waterfall" method
~~~~~~~~~~~~~~~~~~
* Old textbook method
* Not very good for science (or anything really...)
* Lots of pre-planning: information flows from the plan to the code

  - Hence the name: flows down

* Assumes no change

.. epigraph::

   https://en.wikipedia.org/wiki/Waterfall_model

Waterfall method steps
~~~~~~~~~~~~~~~~~~~~~~
* Requirements gathering
* Design
* Coding
* Testing
* Maintenance

Agile development methods
~~~~~~~~~~~~~~~~~~~~~~~~~
* **Agile**: Having the faculty of quick motion, nimble (wiktionary)
* Agile methods designed to be incremental

  - React to change gracefully

* Broad category, many sub-methods
* Agile methods are quite similar to what scientists do

Agile principles
~~~~~~~~~~~~~~~~
* Iterative, incremental, and evolutionary design
* Very short loop: plan, write, test, make it work, repeat
* Regular adaption to changing circumstances
* Frequent, quick meetings instead of detailed plans

Main document: Agile Manifesto

.. epigraph::

   https://en.wikipedia.org/wiki/Agile_software_development#The_Agile_Manifesto

Agile Sub-strategies
~~~~~~~~~~~~~~~~~~~~
* Test-driven development
* Extreme programming
* Scurm
* Lean development
* .. and plenty more


How does this relate to science?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Our work is always changing
* Our goals are incremental



Running a project
-----------------

* Much more than just code to a healthy project

  - Human factors and synchronization

* A project used by others must have

  - documentation
  - releases
  - communication among participants
  - bug and issue tracking
  - distribution of responsibility, line of succession
  - procedures for changes

* This section is useful if you lead a project
* Equally important if you want to contribute to a project


Example project: ``networkx``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``networkx`` is a graph library for Python
* We will use it as an example for a open source project.
* http://networkx.github.io/

Documentation
~~~~~~~~~~~~~
* Usually last thing you do, but most important
* Types of documentation

  - tutorials
  - reference/API
  - docstrings (function docs)
  - developer: how someone should contribute

How to write documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~
* Writing is docs is hard
* Use this recipe to make it faster

  - Summary: why would you want to use this?
  - Details on workings
  - Inputs: formats, meanings, uses
  - Outputs: formats, meaning, uses
  - Optional items: description of algorithms

(this applies to programs, packages, functions, modules, etc)

Project communication strategies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* IRC

  - Fast but ephemeral communication
* Mailing lists
* Wikis

  - Long-term planning, documentation

Tracking issues
~~~~~~~~~~~~~~~
* In large project, you can't rely on memory to remember issues
* Issue trackers

  - submit a bug or issue
  - triage (set priority, category)
  - discussion
  - resolution (closing)

* Many implementations: gitlab, github, sourceforge, etc

Making changes
~~~~~~~~~~~~~~
* Making commits isn't open to the public
* Core committers: can directly make changes to VCS
* Others: make a request (patch), discussed (issue tracker or mailing
  list)

  - Then a core committer applies, with attribution

* Communicating changes

  - "patch" is the standard format
  - Alternative, git pull requests can be used (gitlab/github)
  - Some projects want an issue for each request

* **Treat every patch or contribution as a gift**

Releases
~~~~~~~~
* Rolling release

  - Commits go straight to "consumer" version

* Fixed releases
* Fixed releases can be important

  - Milestone to fix bugs, documentation
  - Comparisons of features/bugs
  - Longer-term stability (stable updates)

* Making a release

  - Tag in VCS
  - Changelog

* Define backwards compatibility goals

..

   If you make releases, it's a good idea to have documentation on how
   to make a release.  Otherwise, each time you want to release you'll
   be figuring out the process all over again.

Distribution of responsibility and succession
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Not an open source project without other contributions.
* Try not to have single points of failure.
* Plan for the project to be handed over eventually.
* One study: most scientific software projects that survive have a
  permanent position leading them.
* Encourage contributions!


Release tools
~~~~~~~~~~~~~
* Understand your language's tools for distribution.

  - e.g. Python ``distutils`` and ``setup.py``

* Most "normal" and easiest to use for everyone.
* Handles most special cases.


Designing software
------------------
* This is the "think before you code" part
* Designing software is more art that science

  - I don't know how to teach it

* What follows is general advice

Software reuse
~~~~~~~~~~~~~~
* Software can be reused at zero cost
* Types of reuse

  - Large-reuse: general programs, frameworks
  - Small-reuse: building blocks to make other programs

* Design to be reusable

Modularity
~~~~~~~~~~
* Each function should have one concern
* Example: if a function both does calculation and reads in data, it
  is

  - harder to expand
  - harder to test
  - harder to read and maintain

Layers
~~~~~~
* Think in terms of layers, for example

  - Input/reading layer (different input formats)
  - Calculation layer
  - Storage layer
  - Writing layer

Know your tools
~~~~~~~~~~~~~~~
* Language features and paradigms
* Libraries

The Zen of Python
~~~~~~~~~~~~~~~~~
* Python has this manifesto
* Good summary of software best practices
* The simplicity Python is its power

The Zen of Python (1/2)
~~~~~~~~~~~~~~~~~~~~~~~
* Beautiful is better than ugly.
* Explicit is better than implicit.
* Simple is better than complex.
* Complex is better than complicated.
* Flat is better than nested.
* Sparse is better than dense.
* Readability counts.
* Special cases aren't special enough to break the rules.
* Although practicality beats purity.
* Errors should never pass silently.
* Unless explicitly silenced.

The Zen of Python (1/2)
~~~~~~~~~~~~~~~~~~~~~~~
* In the face of ambiguity, refuse the temptation to guess.
* There should be one-- and preferably only one --obvious way to do it.
* Although that way may not be obvious at first unless you're Dutch.
* Now is better than never.
* Although never is often better than *right* now.
* If the implementation is hard to explain, it's a bad idea.
* If the implementation is easy to explain, it may be a good idea.
* Namespaces are one honking great idea -- let's do more of those!

Projects vs libraries
~~~~~~~~~~~~~~~~~~~~~
* Separate general code from research code
* General code (library)

  - Clean, documented, tested, general

* Project code

  - "Research code": messy, fast moving
  - Eventually promoted to a library


Interactive vs production systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Interactive system (e.g. ``ipython``) are great for development
* ... but they don't have permanence



Conclusions
-----------
* There is no single lesson for day-to-day research work here.
* This should help you in the transition to more formal project
  management.
* **Free software and licenses** allow a wide audience.
* **Software development workflows** coordinate people.
* Lots of **project management** tools are available.
* **Software design** is hard.
