
SQL Database usage: by example
==============================






Outline
-------
After this presentation, you will be able to

- Open an SQLite database in the shell and Python
- Run queries to get basic information out, just like from CSV files.
- Know how to push basic calculations to the sqlite engine
- Be able to understand medium level operations: grouping, ordering,
  joining.
- Be aware of advanced possibilities

You won't:

- Be able to create and manage a sqlite database all by yourself.

Review of database concepts
---------------------------
- Relational databases have structured data
- **SQL**: Structured Query Language

  - You can say what you want, not the steps to calculate it

- Useful for data storage and rearrangements, but not ultra high
  performance numerical operations.
- SQLite database exist as a simple single file


Basic model of data
-------------------
- Everything is a table (rows and columns)
- SQL statements rearrange tables into different forms
- You get an iterator back over tables.

Simple example of rearrangement (aggregating by ``type``):

.. container:: cols

  .. container:: col1

    .. csv-table::
       :header-rows: 1

       type, data
       A, 1
       A, 5
       B, 2
       C, 1
       C, 2
       C, 3

  .. container:: col1 center

     ``GROUP BY type``

     ===>

  .. container:: col1

    .. csv-table::
       :header-rows: 1

       type, sum_data
       A, 6
       B, 2
       C, 6


Connecting to a database: Python
--------------------------------
- Python has the ``sqlite3`` module built-in.
- A database exists as a file on disk and connection is by filename
  only.
- Output is iterator over rows of values (think ``csv``).
- Also other methods for access like ``.fetchone()`` or ``.fetchall()``.

.. python:: pycon

   >>> import sqlite3
   >>> conn = sqlite3.connect('/scratch/networks/data/mit-reality.sqlite')
   >>> cursor = conn.cursor()
   >>> cursor.execute('SELECT ego_id, affil FROM subject LIMIT 5')
   <sqlite3.Cursor object at 0x7f62a00b57a0>
   >>> for row in cursor:
   ...     print row
   ... 
   (0, None)
   (1, None)
   (2, u'1styeargrad ')
   (3, u'mlgrad')
   (4, u'mlgrad')

Connecting to a database: command line
--------------------------------------
- You do *not* need a programming language to access data!
- The ``sqlite3`` command line utility is an excellent interface to
  databases

  - Good for exploration and initial analysis
  - Develop queries here then copy to code

- For the purposes of this talk, use we will use the command line to
  do the exercises.

.. console::

   $ sqlite3 /scratch/networks/data/mit-reality.sqlite

.. code:: sqlite3

   SQLite version 3.8.2 2013-12-06 14:53:30
   sqlite> SELECT ego_id, affil FROM subject LIMIT 5;
   0|
   1|
   2|1styeargrad 
   3|mlgrad
   4|mlgrad

Exercise: Open the MIT reality mining database
----------------------------------------------

#. Connect to any BECS computer via ssh

#. Open the MIT reality mining database by

   .. console::

      $ sqlite3 /scratch/networks/data/mit-reality.sqlite

#. Use the ``.schema`` command to get the schema (definition) of all
   tables.  This is everything needed to re-create the database.

   .. code:: sql

      .schema

#. Select the first 10 lines of the ``subject`` table:

   .. code:: sql

      SELECT * FROM subject LIMIT 10;

#. Count all lines in the ``subject`` and ``comm`` tables:

   .. code:: sql

      SELECT count(*) FROM subject;
      SELECT count(*) FROM comm;

.. epigraph::

   Other databases you may want to connect to

   * HSL data for one day: ``/local/cache/hsl_data/db-1day.sqlite``
     **on thor**
   * Mobile phone data in
     ``/scratch/networks/darst/datasets/MobilePhoneData/``
   * Oxford ego data in ``/scratch/networks/darst/oxford_egos.sqlite``
   * ISI web of science in ``/data/isi/isi.sqlite`` (requires ``isi`` group.)

Basic SQL commands
------------------
- Commands are given as a string and in in semicolon (``;``).
- SQL keywords are case-insensitive but traditionally capitalized.
- The order and general syntax must be pretty exact.
- Try to build up your queries incrementally, instead of typing them
  all at once.
- Use ``LIMIT 5`` to produce a smaller amount of data while
  developing.
- SQL is a standard, but different databases have slight differences.
- Consult `sqlite language reference <http://sqlite.org/lang.html>`_
  for concise but detailed descriptions.

Example of incremental query build-up:

.. code:: sql

   sqlite> SELECT * FROM subject LIMIT 5;
   sqlite> SELECT * FROM subject LEFT JOIN comm USING (ego_id)
           LIMIT 5;
   sqlite> SELECT ego_id, max(ts), min(ts) FROM subject
           LEFT JOIN comm USING (ego_id)
           GROUP BY ego_id LIMIT 5;
   sqlite> SELECT ego_id, max(ts), min(ts) FROM subject
           LEFT JOIN comm USING (ego_id)
           GROUP BY ego_id;


``SELECT``
----------
- Pick certain columns from a table
- The basic command which everything is built from.
- Also a ``SELECT DISTINCT`` which returns distinct rows only.

Syntax: ``SELECT <columns or expressions> FROM <table name>;``

``LIMIT``
---------
- Limit to only the first ``N`` columns
- Has options for offsets and other modifications
- ``ORDER BY`` is applied first (introduced soon)
- Use this when doing initial development: have a small limit for easy
  viewing and faster running, remove for production.

Syntax: ``SELECT ... FROM ... LIMIT N;``

``WHERE``
---------
- Select only rows matching a particular condition
- Condition can be any expression

  - Variables are the column names from the table

Syntax: ``SELECT ... FROM ... WHERE <condition>``

``ORDER BY``
------------
- Order rows in returned rows
- Usually a column name, but can be any expression


Syntax: ``SELECT ... FROM ... ORDER BY <expression>``


Ordering of clauses
-------------------
- As I said, SQL is picky about the order of clauses.
- Refer to the `sqlite language diagrams
  <http://sqlite.org/lang.html>`_ for a good summary of syntax

.. code:: sql

   SELECT ... FROM ... JOIN ... WHERE ...
   GROUP BY ... ORDER BY ... LIMIT ...;


Exercises 2: going a bit deeper
-------------------------------
#. Continue with the MIT reality mining data.
#. Use ``.schema`` to understand the table and column names.
#. Use ``SELECT ... LIMIT 5`` to study the type of data in each table.
#. Use ``SELECT count(*)`` and ``WHERE ego_id=N`` to get the total
   number of events of each ego.
#. Select the first and last event in the ``comm`` table.  To sort by
   time in reverse order, use ``ORDER BY <column name> DESC``.  To get
   only the first event in this order, use ``LIMIT 1``.


Aggregate functions
-------------------
- Group rows by some conditions.  All rows with the same condition are
  put in the same group.
- Some function is applied to reduce the rows to combine grouped rows
  to one.

- Example:

.. code:: sql

   SELECT type, sum(count) FROM table GROUP BY type;

.. container:: cols

  .. container:: col1

    .. csv-table::
       :header-rows: 1

       type, data
       A, 1
       A, 5
       B, 2
       C, 1
       C, 2
       C, 3

  .. container:: col1 center

     ===>

  .. container:: col1

    .. csv-table::
       :header-rows: 1

       type, sum(data)
       A, 1+5
       B, 2
       C, 1+2+3

- Available functions: ``count``, ``sum``, ``min``, ``max``,
  (``avg``, ``stdev``, ``median``, ...)


Example: Aggregating MIT reality mining
---------------------------------------
- Goal: find the first and last call of every ego
- Aggregate by ``ego_id`` to put all ego's events into the same group:
  ``GROUP BY ego_id``.
- Within the group, we take the first timestamp (``min(ts)``) and last
  timestamp (``max(ts)``) by using aggregate functions.

.. code:: sql

   SELECT ego_id, min(ts), max(ts)
      FROM comm
      WHERE desc='Voice call'
      GROUP BY ego_id;

   1|2005-01-27 19:05:37.000000|2005-01-27 22:36:59.000000
   3|2004-08-03 15:50:19.000000|2005-05-04 21:16:58.000000
   4|2004-08-01 00:05:52.000000|2004-12-24 05:54:03.000000
   ...

Exercise: Advanced queries on MIT reality mining
------------------------------------------------
On the MIT reality mining dataset, compute the following.  You will
have to use the ``.schema`` command to figure out what tables and
columns are relevant!

#. Number of events per user (of both ``comm`` and
   ``bluetooth`` types).  (Hint: ``GROUP BY ego_id`` and ``count(*)``)
#. Total number of communications of each type (``desc`` column)
#. Number of users per affiliation. (Hint: ``subject`` table)


Join
----
- Often, you need to combine information from more than one table
- One column provides a **join key** which correlates information
  about the columns.

Example:

.. container:: cols

  .. container:: col1

    .. csv-table::
       :header-rows: 1

       ego_id, ts
       0, 1.5
       0, 2.0
       1, 0.0
       2, 0.7
       2, 1.2

  .. container:: col1

    .. csv-table::
       :header-rows: 1

       ego_id, affil
       0, grad
       1, mlstaff
       2, professor

.. container:: center

   ``JOIN on (ego_id)``

   ===>

.. container:: cols center

  .. csv-table::
     :header-rows: 1

     ego_id, ts, affil
     0, 1.5, grad
     0, 2.0, grad
     1, 0.0, mlstaff
     2, 0.7, professor
     2, 1.2, professor

Join syntax
-----------

- There are different types of joins: ``JOIN``, ``LEFT JOIN``, ``RIGHT
  JOIN``, ``OUTER JOIN``.

  - Differ in how they handle data missing from one column or the other.

- This is a relatively basic concept, but will not be covered in this talk.

- Different syntaxes (``USING`` AND ``ON``) for matching rows.

Syntax 1: ``SELECT ... FROM <table name> JOIN <table name> USING
( <column name> )``

Syntax 1: ``SELECT ... FROM <table name> JOIN <table name> ON
( <condition> )``


Join examples
-------------
Explore these examples yourself

#. MIT reality, adding affil column

.. code:: sql

   sqlite> SELECT ego_id, affil, count(*) FROM subject LEFT JOIN comm
           USING (ego_id) GROUP BY ego_id LIMIT 10;
   0||1
   1||20
   2|1styeargrad |1



Date and time functions
-----------------------
- Handling date and time information is necessary, and can be pushed
  to the database
- Standard SQL representation of date/time is text timestamp::

    2004-11-29 23:21:31

- sqlite core functions:

  - ``datetime``: convert time data to datetime string
  - ``date``: convert time data to date string
  - ``time``: convert time data to time string
  - ``juliandate``: time data --> julian date number
  - ``strftime``: convert a time data using string formatting,
    e.g. ``%Y-%m``

Date and time operations
------------------------
Examples of operations you can do:

- Convert to unixtime: ``strftime('%s', ts)``
- Convert from unixtime: ``datetime(ts, 'unixtime')``
- Group data into hourly bins: ``GROUP BY strftime('%h', ts)``
- Convert from local to UTC: ``datetime(ts, 'utc')`` (uses ``TZ``
  environment variable)
- Number of seconds between two timestamps: ``strftime('%s', ts2) -
  strftime('%s', ts1)``
- Number of days between two timestamps: ``julianday(ts2) -
  julianday(ts1)``

Exercise: day intervals
------------------------

#. Again use the MIT reality mining data, beginning from where you
   last left off.  You will work to add an extra column, the number of
   days between the first and last event.
#. Create a table with the following information for only events of
   description 'Voice call':

     ego_id, affil, #-events-total, first-event, last-event, #-of-days-of-events.


#. Sort your rows by #-of-days-of-events.


Miscellaneous other functions and expressions
---------------------------------------------
- Most mathematical operations are supported: ``2*col1+col2``
- Rename result columns: ``2*col1+col2 AS shifted_value``
- More advanced mathematical functions as an loadable extension.
- Name matching: ``GLOB``, ``LIKE``, ``REGEX``
- Definition of functions

Views
-----
- Views are *dynamic* tables defined by some other query

  - Use no extra space
  - Created as they are needed

- Queries on views are internally rearranged to an optimal form

Indexing
--------
- Wiktionary: **index**: An integer or other key indicating the
  location of data e.g. within an array
- Like Python dictionaries, they allow *fast* lookups based on *any*
  column
- A necessary part of databases for good performance, and really the
  whole point of databases
- Not automatically made, needs careful thought
- In SQL, they store data in sorted order

Using indexes
-------------
- Indexes have a unique name, like tables
- Creating an index

  .. code:: sql

     CREATE INDEX idx_<tablename>_<colnames>
         ON <tablename> (<col1>, <col2>, ...);

- How do you tell if an index is being used, or where one is needed?

  .. code:: sql

     EXPLAIN QUERY PLAN <select statement>;

  Should mention what indexes are being used.  ``SCAN`` indicates
  complete table scans, ``SEARCH`` indicates index usage.

- This talk does not go into the intricacies of indexing and
  optimization

Advanced query types
--------------------
- Subqueries

  - Multiple levels of processing

  .. code:: sql

     SELECT n_cite, count(*) FROM
         (select cited_pid, count(*) AS n_cite FROM citation GROUP BY cited_pid)
     GROUP BY n_cite ORDER BY n_cite;

- Union/intersect queries

  - Performing set operations on the returned rows
  - ``UNION``, ``INTERSECT``, ``UNION ALL`` (addition), ``EXCEPT``
    (subtraction)

  .. code:: sql

     SELECT ... UNIONS SELECT ...;



Inserting and updating
----------------------
- I have intentionally not talked about altering and creating a
  database

  - I am teaching you how to replace reading .csv files, not make a
    production system!

- Insert syntax: create a new row

  .. code:: sql

     INSERT INTO table-name (col1, col2, ...) VALUES (val1, val2)

- Update syntax: alter values of an existing row

  .. code:: sql

     UPDATE table-name SET col1=val1, col2=val2, ... WHERE <condition>;


Creating entire databases from scratch
--------------------------------------
- My strategy:

  - Single script which recreates DB from scratch
  - Future improvements done by adding new columns or tables

- The most difficult part is imposing structure on the data

  - This is, in essence, the core task in any data use: figure out
    what structure you can rely on and use

- Examples of creating scripts (most are messy!):

  - ``/proj/networks/darst/pymod/compnet_data/isi.py``

  - ``/proj/networks/darst/pymod/compnet_data/MobilePhoneData.sh``


Summary
-------
- A the simplest, a database replaces CSV files, but includes
  information on column definitions and data types
- With trivial extra knowledge, simple operations can be done within
  the database.
- At best, a large portion of data processing can be pushed to a
  database.
- You can say what you want, without having to debug the exact steps
  to get it.
- This is a different skill to learn, but it is considered standard
  among data scientists.  Why not us?


The end
-------



References
----------

* Wikipedia on SQL
  https://en.wikipedia.org/wiki/SQL

* SQLite language reference
  http://sqlite.org/lang.html

* OpenTechSchool SQL tutorial
  http://opentechschool.github.io/sql-tutorial/
