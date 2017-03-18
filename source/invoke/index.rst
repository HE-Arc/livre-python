.. _invoke-tutorial:

``invoke``
==========

Par Jonathan Guerne

Introduction
------------

L'utilié de Invoke_ est de pouvoir très simplement lancer des tâches que vous
aurez déjà préparées auparavant et qui exécuteront par exemple des lignes de
commande.

:py:mod:`invoke` se veut facile à prendre en main mais puissant à utiliser. Ce
qui signifie que l'on peut l'utiliser dans le cas où l'on souhaite simplement
lancer une commande simple.

Exemples
--------

On va ensuite mettre en place un fichier nommé ``tasks.py``.

.. literalinclude:: ./examples/tasks.py

.. code-block:: console

    $ invoke ouverture
    bonjour


.. Bibliographie:

.. _Invoke: http://www.pyinvoke.org/
