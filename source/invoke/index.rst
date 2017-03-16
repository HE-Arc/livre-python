=======
.. _Invoke-tutorial:

invoke
======
Par Jonathan Guerne

Introduction
------------
l'utilié de Invoke_ est de pouvoir très simplement lancer des tâches que vous
aurez déjà préparé au par avant et qui exécuteront par exemple des lignes de
commande.

Invoke se veut facile à prendre en main mais puissant à utiliser. Ce qui signife
que l'on peut l'utiliser dans le cas où l'on shouaite simplement lancer une commande simple :

.. code-block:: python3

  @task
    def ouverture(ctx):
        print("bonjour")

ou alors pour des groupes de tâches plus complexe pouvant également utiliser des
arguments.

.. code-block:: python3

 @task
  def clean(ctx, which=None):
    which = which or 'pyc'
    print("Cleaning {0}".format(which))

  @task(pre=[call(clean, which='all')]) # or call(clean, 'all')
  def build(ctx):
    print("Building")

*code source tiré de la documentation_  officielle de invoke*



Installation
------------
pour pouvoir utiliser les commandes propres à la librairie Invoke il faut d'abord
s'assurer de l'avoir installée dans son environnememt python.
Comme d'habitude on utilise pip pour installer des librairies externe.

::

  $ pip install invoke

On va ensuite mettre en place un fichier nommé ``tasks.py``.

Exemples
--------
.. literalinclude:: ./examples/tasks.py

.. _Invoke: http://www.pyinvoke.org/
.. _documentation: http://docs.pyinvoke.org/en/latest/
