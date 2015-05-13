Introduction to SQL and relational databases
============================================

This talk provides an introduction to SQL and (relational) databases.
The purpose is not to provide a usable background in SQL, but instead
to explain *why* a scientist (whose field or group isn't currently
using databases) might want to use them to make their work better.
This talk is of the lowest level possible.  If you know what a
relational database is, this talk is probably too basic for you.  It
also focuses on the *why*\ s, not the *how*\ s, so if you want to
actually use databases it will require another tutorial or independent
study.

This talk isn't just about databases, but the philosophy of how our
group can better manage data.



Outline
-------
- Theory: What's a database?
- How does database operation differ from straight coding?
- Operation of several DB systems
- Integration of DBs into scientific research
- Discussion: what should our group do?
- Optional: Basic SQL tutorial

Databases and the relational model
----------------------------------
- ``database``: A collection of (usually) organized information in a
  regular structure, usually but not necessarily in a machine-readable
  format accessible by a computer.  (wiktionary)
- The equivalent of a filesystem, but for data
- The ``relational model``: a good way of organizing and querying
  data.

.. epigraph::

   Basically, a database is a place to store data, with a lot of good
   operations.  Let's compare it to a bunch of ``csv`` files.  With a
   ``csv`` file, you can read in the data and convert it to lists or
   arrays or dictionaries you can use.  With databases, there are a
   lot higher level operations: get all rows that match some
   condition.  Replace one row with another.  Replace one value in a
   row.  Allow multiple processes to access and change data
   simultaneously.  All of these can be indexed to allow :math:`O(1)` (very
   fast) operations.

   A lot like the rest of the tutorials, the is the same general
   pattern of "a bit more initial organization makes later work
   easier".

The relational model
--------------------
- Relations (tables)
- Tuples (rows)
- Operations on these tables and rows to slice and dice data
- Declarative language: say what you want, not how to do it
- A closed algebra representing operations.  Can be internally
  rearranged and optimized for efficiency.

.. epigraph::

   Relational Algebra is one of the standard things you would learn in
   a database course.  This isn't a database course, and discussing
   this is all more theoretical than scientists need (or probably
   want) to know.  Just realize that there is more than an arbitrary
   system here.  This talk will use the SQL terminology of ``rows``\ s
   and ``tables``\ s.  The other things mentioned here will be
   discussed in this talk.

Example: MIT reality mining data
--------------------------------
- ``ssh thor``
- ``sqlite3 /local/cache/darstr1/mit-reality.sqlite``

Components of a relational database (theoretical)
-------------------------------------------------
- Schema (types, constraints, foreign keys)
- SQL (de facto standard query language)
- Indexes: optimized data lookup methods (like hash tables for
  dictionaries)
- Views: shortcuts for data access
- Procedures: functions defined within DB itself.

.. epigraph::

   These are the conceptual parts of databases.  Later, we'll talk
   about the nuts and bolts of actual databases.

   The schema defines the tables and column names and data types.  In
   relational databases, the schema needs to defined before you put
   data in.

   SQL is the query language.  It looks like ``SELECT blah, blah2 FROM
   some-table JOIN other_table USING (id) WHERE x=5;``.  Perhaps this
   is the most well-known thing from databases, but it's just the
   interface language.  It is pretty standard, but modern databases
   get away from it.

   Indexes allow fast lookups by different columns.  They are the
   equivalent of Python dictionary keys, but also store data in a
   sorted order.  This provides the speed of databases.

   Views provide shortcuts for data access.  It's another way you can
   push calculations into the database to save work in your code.

   You can also define functions (procedures) directly in the
   database.  This pushes calculations to the data.

Structured vs unstructured data
-------------------------------
- Structured data: tightly constrained to a data model
- Unstructured data: No data model
- Databases are (mostly) structured records

  - It is necessary to impose structure when importing the data
  - This mostly corresponds to the "cleaning" stage in work

- The database structure provides easy ways of updating/changing data.

.. epigraph::

   An example of structured data would be a CSV file that is perfect.
   Unstructured would be plain text documents, or CSV files with
   missing data, incomplete rows, different datatypes.  You could even
   say that since data types (e.g. integers) don't have metadata
   specifying type is a small lack of structure.

   The rigid structure of the data allows the usefulness of the
   databases.  It's also the annoyance.  However, imposing structure
   on data is something you need to do anyway.

Declarative vs procedural access
--------------------------------
- **Procedural language**: Specify steps to produce a result
- **Declarative language**: Specify desired result
- SQL is a declarative language

  - Relational algebra allows internal optimization
  - *Huge* timesaver in terms of low-level programming

.. epigraph::

   One line of SQL can replace tens of lines of Python code.  You also
   don't have to worry about all of the data loading and other
   management talks (of course, someone had to have handled that
   already to get it into the database).  The database engine can
   internally optimize queries.

Concrete DB: SQLite operation
-----------------------------
- SQLite is a *library* for database file access
- Single file on disk (also in-memory operation)
- All operations are within the same process
- Good as a simple data storage format
- Downside: bad at high concurrency

.. epigraph::

   SQLite is a pretty nice package for basic work.  It has all the
   structure needed, but uses a "file" concept for storage, not
   "server".  This makes it very convenient for development or
   teaching purposes.  For most scientific tasks, it is probably the
   ideal tool.  The main case where it wouldn't be suitable is when
   you have many, many, simultaneous reads and writes, like for a
   high-traffic production website.

Concrete DB: RDBMS server operation
-----------------------------------
- Data server running on a computer
- Network or socket access
- Pros: highly optimized, advanced data caching and distribution
- Cons: greater communication cost, bad for streaming large amounts of
  data, high maintenance cost

.. epigraph::

   This is more along the lines of what people think of when they hear
   "database".  A separate server running that is managing
   everything.  This has a lot of overhead from a system
   administration side, but allows maximal performance under huge
   loads.  This could be useful in some cases, but is too much extra
   work and lost flexibility for most scientific uses.

Database use cases: ideal and problematic
-----------------------------------------
* Ideal use cases

  - Data processing can be pushed to DB
  - Large body of static upstream data
  - Long-term usage
  - Separation of calculation and processing
  - Structured storage without calculations
  - Storing and updating dynamic data

* Problematic use cases

  - Intense numerical calculations
  - Non-fixed schema
  - Schema rapidly changing (scientific context)
  - Throw-away calculations

* Some problems solved by NoSQL databases.

Relation to pandas and other tools
----------------------------------
- ``pandas`` is a python package that has relational-algebra like
  operations.

Integration of databases into our research
------------------------------------------

Example: Urban Dictionary data
------------------------------
- ``sqlite3 /proj/networks/darst/urban_dictionary/ud.sqlite``
- Example of calculations in the DB

Example: HSL data
-----------------
- ``sqlite3 /local/cache/hsl_data/db-1day.sqlite``
- Example of indexing

Schemaless databaseses ("NoSQL")
--------------------------------
- Relax schema constraints of SQL databases
- More free-form data access methods
- Scale to larger datasets, "big data"
- Example: MongoDB, Hadoop, Neo4J

.. epigraph::

   These types of databases are what people consider modern "big data"
   databases.  Basically, the strong structure and consistency
   requirements of relational databases becomes too much, so these
   relax these requirements and allow you to store more data.  Most
   don't use SQL, but there are more declarative query languages being
   developed for them.  These will be useful for particular uses cases
   with either massive amounts of data or less structured data.

Conclusions
-----------
- Databases provide structured storage: easier processing and
  self-documenting.
- Data management can be much easier by using SQL: say what you want,
  not how to do it
- Fits in with Python model: separation of high-performance packages
  and glue part.

Discussion
----------
- These tools are important to data scientists
- Not all of our work can fits this model, but parts do




Part 2: A quick intro to querying SQL (optional)
------------------------------------------------


A quick intro to SQL
--------------------
- SQL is case-insensitive
- Statements end in a semicolon
- Statement is somewhat rigid in ordering of terms
- This is a non-rigorous introduction
- Comments are ``--``

Run ``ssh thor`` and ``sqlite3
/local/cache/darstr1/mit-reality.sqlite`` to open a database import of
the MIT reality mining data.


Selecting
---------
.. code:: sqlite3

   SELECT <columns> FROM <table name> [LIMIT <N>];

   -- Show all tables, turn on headers for convenience
   .schema
   .headers on

   -- Preview first lines in the "bluetooth" table
   select * from bluetooth limit 10;
   -- View information on subjects
   select ego_id, start_date, end_date, affil from subject limit 10;

Where
-----

.. code:: sql

   SELECT <columns> FROM <table name> WHERE <expression>;

   -- View all information about ego_id=25
   select * from subject where ego_id=25;
   -- View activity periods for all 'mlgrad' egos.
   select ego_id, start_date, end_date, affil from subject where affil='mlgrad';

Order by
--------

.. code:: sqlite3

   SELECT <columns> FROM <table> ORDER BY <expression>;

   -- View all subjects, ordered by start date.
   select ego_id, affil, start_date, end_date from subject order by start_date;

Group by
--------
- "Aggregate functions"

.. code:: sql

   SELECT <columns> FROM <table name> GROUP BY <expression>;
   SELECT col1, min(col2), max(col2) FROM <table name> GROUP BY col1;

   -- Count numbers of people with each affiliation
   select count(*), affil from subject group by affil;
   -- First/last bluetooth event for each person
   select ego_id, min(ts), max(ts) from bluetooth group by ego_id;
   -- Number of days each subject was active
   select ego_id, julianday(max(ts))-min(julianday(ts)) from bluetooth group by ego_id;


Join
----
- Join connects several tables on common values

.. code:: sql

   SELECT <columns> FROM <table1> JOIN <table2> [ON(col1=col2) | USING (<name>)] GROUP BY <expression>;


   -- Do the same as last example, but also include affilations
   select ego_id, affil, julianday(max(ts))-min(julianday(ts)) from bluetooth left join subject using (ego_id) group by ego_id;

Functions
---------
- Basic scalar functions and math operations:

  - http://sqlite.org/lang_corefunc.html
  - http://sqlite.org/lang_expr.html

- Aggregate functions: min/max/count,...

  - http://sqlite.org/lang_aggfunc.html


Advanced
--------
- Set operations (union, intersect, ...)
- Distinct
- Date/time operations
- Indexes: fast look-ups by any column
- Optimization: ``EXPLAIN QUERY PLAN``

SQL resources
-------------
- The sqlite language reference is compact but has very useful
  reference diagrams:

  - http://sqlite.org/lang.html

.. epigraph::

   Each SQL database has its own custom syntax, but overall it is
   pretty standard.  I think the SQLite documentation is pretty good:
   It is detailed, but also has good summary diagrams.
