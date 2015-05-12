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

The relational model
--------------------
- Relations (tables)
- Tuples (rows)
- Operations on these tables and rows to slice and dice data
- Declarative language: say what you want, not how to do it
- A closed algebra representing operations.  Can be internally
  rearranged and optimized for efficiency.

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

Structured vs unstructured data
-------------------------------
- Structured data: tightly constrained to a data model
- Unstructured data: No data model
- Databases are (mostly) structured records

  - It is necessary to impose structure when importing the data
  - This mostly corresponds to the "cleaning" stage in work

- The database structure provides easy ways of updating/changing data.

Declarative vs procedural access
--------------------------------
- **Procedural language**: Specify steps to produce a result
- **Declarative language**: Specify desired result
- SQL is a declarative language

  - Relational algebra allows internal optimization
  - *Huge* timesaver in terms of low-level programming

Concrete DB: SQLite operation
-----------------------------
- SQLite is a *library* for database file access
- Single file on disk (also in-memory operation)
- All operations are within the same process
- Good as a simple data storage formtawi
- Downside: bad at high concurrency


Concrete DB: RDBMS server operation
-----------------------------------
- Data server running on a computer
- Network or socket access
- Pros: highly optimized, advanced data caching and distribution
- Cons: greater communication cost, bad for streaming large amounts of
  data, high maintenance cost

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

