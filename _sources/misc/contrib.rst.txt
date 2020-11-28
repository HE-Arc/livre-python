Contribution
============

Toute *pull request* est la bienvenue. Mais avant ça, assurez-vous que tout fonctionne chez vous.

Compilation
-----------

.. code-block:: bash

    $ pip install -r requirements.txt
    $ ./build.sh

    # latex or epub
    $ sphinx-build -Wn -b latex source build/latex
    $ sphinx-build -Wn -b epub source build/epub

Compilations sous Windows
-------------------------

.. code-block:: ps1

    > pip install -r requirements.txt
    > invoke html

Édition en direct
-----------------

`Sphinx view <http://pythonhosted.org/sphinx-view/>`_ permet de recompiler automatiqument un fichier ou un projet *Sphinx*.

.. code-block:: bash

    $ pip install sphinx-view
    $ sphinx-view source
