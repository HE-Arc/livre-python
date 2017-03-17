======================
     ITERTOOLS
======================

Par Johnny Da Costa <johnny.dacosta@he-arc.ch>



Introduction
------------
------------

Les :py:mod:`itertools` sont des outils puissant pour itérer dans les listes/tableaux de manière
efficace et intelligente. Elles nous simplifient la vie par exemple si l'on veut appliquer une opération
sur chaque élément de notre tableau. On peut aussi très facilement concaténer deux, trois ou n liste avec une simple
fonction :py:func:`count() <itertools.count()>` ou par exemple créer un filtre sur nos tableau avec :py:func:`compress<itertools.compress>`. 


Iterateur infini
----------------

function :py:func:`count(start=0, step=1) <itertools.count>`
**************************************************
.. literalinclude:: use_itertools.py
   :start-after: # COUNT_BEGIN
   :end-before: # COUNT_END


Iterateur avec fin
-------------------

function chain()
****************

.. literalinclude:: use_itertools.py
   :start-after: # CHAIN_BEGIN
   :end-before: # CHAIN_END
   
   
.. literalinclude:: use_itertools.py
   :start-after: # COUNT_BEGIN
   :end-before: # COUNT_END

   
function Compress()
*********************
   
.. literalinclude:: use_itertools.py
   :start-after: # COMPRESS_BEGIN
   :end-before: # COMPRESS_END
   
   
   
function filter()  /filterfalse()
***********************************
        
.. literalinclude:: use_itertools.py
   :start-after: # FILTER_BEGIN
   :end-before: # FILTER_END

function Map()
**************
      
.. literalinclude:: use_itertools.py
   :start-after: # MAP_BEGIN
   :end-before: # MAP_END
   
   
function Dropwhile()
*********************

.. literalinclude:: use_itertools.py
   :start-after: # DROPWHILE_BEGIN
   :end-before: # DROPWHILE_END
   
function Takewhile()
********************
   
.. literalinclude:: use_itertools.py
   :start-after: # TAKEWHILE_BEGIN
   :end-before: # TAKEWHILE_END
