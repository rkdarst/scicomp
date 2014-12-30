

Use the short constants built into data structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``O(1)`` operations are great, but you usually have to loop over
things, sometime.

- Improve the innermost loop first.  That is probably all you need.

- If you have to do math, use numpy arrays, not lists.

- Using internal python operations better than doing it explicitly:

  .. python::

      [ (a+b) for a,b in zip(A, B) ]

  vs

  .. python::

     L = [ ]
     for a, b in zip(A, B):
         L.append(a+b)

.. epigraph::

   This is the realm of optimizing.  We will discuss this later.
