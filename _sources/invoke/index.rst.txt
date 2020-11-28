.. _invoke-tutorial:


==========
``invoke``
==========

Par Jonathan Guerne [#email]_

Introduction
============

L'utilité de pyinvoke_ est de pouvoir très simplement lancer des tâches que vous
aurez déjà préparé au pare avant et qui exécuteront par exemple des lignes de
commande.

pyinvoke_ se veut facile à prendre en main mais puissant à utiliser. Ce qui signifie
que l'on peut l'utiliser dans le cas où l'on souhaite simplement lancer une commande simple :

.. code-block:: python3

    @task
    def ouverture(ctx):
        print("bonjour")

Ou alors pour des groupes de tâches plus complexe pouvant également utiliser des
arguments.

.. code-block:: python3

    @task
    def clean(ctx, which=None):
        which = which or 'pyc'
        print("Cleaning {0}".format(which))

    @task(pre=[call(clean, which='all')]) # or call(clean, 'all')
        def build(ctx):
        print("Building")

Code source tiré de la :ref:`documentation officielle <defining-and-running-task-functions>` de invoke.

Exemple
=======

lancer une tâche
----------------
Dans un projets simple il est préférable de stocker les tâches dans un fichier nommé ``tasks.py`` (le nom du fichier est important).
Il est cependant possible de stocker des tâches dans plusieurs fichiers en utilisant des namespaces

.. peut-on changer le nom du fichier?

Le fichier ``tasks.py`` doit commencer par importer les éléments invoke dont il va
avoir besoin. Cela est fait avec la ligne suivante :

.. code:: python3

  from invoke import task

:py:func:`~invoke.tasks.task` est l'élément essentiel à la création de tâche avec pyinvoke_, il faudra pratiquement toujours
l'importer.

On arrive à l'écriture de la tâche en elle-même. Sa sytaxe est très proche de
celle d'une simple fonction :

.. code-block:: python3

    @task
    def build(args):
        print("do stuff")

La seule nouveauté quand on a déjà codé des fonctions en python est la ligne ``@task`` précédant
la fonction elle-même. Comme on peut le voir sur l'exemple il est tout à fait possible d'utiliser
des paramètres pour influencer le comportement de sa tâche.

Une fois les tâches écrites on peut lancer un invite de commande afin de les tester.
Pour pouvoir savoir quelle tâches sont disponibles pour notre projet on peut utiliser la commande suivante
pour les lister :

.. code-block:: console

  $ invoke -l

Maintenant, si on veut lancer la tâche **build** il faut le faire de cette façon :

.. code-block:: console

  $ invoke build

Si on a envie d'obtenir de l'aide sur la commande **build** notamment ses paramètres on utilise
cette commande :

.. code-block:: console

  $ invoke --help build


Finalement pour lancer une commande en lui spécifiant ses arguments il faut écrire ceci :

.. code-block:: console

  $ invoke build -args lalala

Ici on passe comme paramètre args la valeur ``"lalala"``. Par défaut les
paramètres sont interprétés comme des chaînes de caractères.

.. todo::

    On meurt d'envie de savoir ce qui est affiché par chacune de ces commandes.

Lancer une commande
-------------------
En guise d'exemple nous allons ici étudier comment utiliser Invoke pour pouvoir
faciliter l'utilisation de la librairie sphinx en générant des pages HTML avec des
fichiers écrits au format rst (comme celui-ci)

.. literalinclude:: ./examples/basic-sphinx.py
   :linenos:

La première ligne sert évidemment à importer les éléments de la librairies Invoke
avec lesquels on désir travailler. Ici en l'occurence comme dans tous les programme utilisant
les ``@task`` de Invok on importe **task**, on va également importer **run** qui va nous permettre
de lancer nos commandes.

Le code en lui-même est très simple est au final ne contient pas beaucoup plus de ligne
que le premier exemple présenter en haut de ce document. La seule subtilité est que
pour pouvoir lancer une commande on va devoir utiliser un contexte (ici appelé **ctx**)
qui sera placé en argument de la tâche. Il suffit ensuite d'appelé la méthode run dans
le contexte et de passer en argument une chaîne de caractère pour lancer la commande.

.. attention::

   Sous windows on peut rencontrer des problèmes au lancement des commandes.
   En effet il est possible que Invoke ait besoin de connaître l'adresse de
   l'invite de commande à utiliser. Pour cela on va mettre en place un fichier de
   configuration contenant cette information (cf. WinError_3_)


On peut également mettre en place un système plus poussé qui va par exemple nettoyer
le dossier de destination avant de générer le contenu HTML

.. literalinclude:: ../../tasks.py
   :linenos:
   :start-after: # html start
   :end-before: # checks start

.. c'est bien, mais ce `hide=True` est dommage.

Pour qu'une tâche A appelle une tâche B avant son exécution il suffit d'utiliser la
syntaxe suivante.

.. code-block:: python3

    @task
    def B():
        print("task B")

    @task(B)
    def A():
        print("task A")

Si un appel à la tâche A est fait, la sortie sera la suivante :

.. code-block:: console

    $ invoke A
    task B
    task A

Finalement il peut être intéressant de savoir que l’on peut tester l’exécution
d’une commande. Son comportement sera le suivant :
Retourne ``True`` s’il n’y a pas eu d’erreur et ``False`` sinon.

.. code-block:: python3

    @task
    def A(ctx):
        if ctx.run("your command"):
            print("ok")

.. todo::

    Selon mes tests, si la première commande échoue, la tache est stoppée et
    invoke se termine. Aurais-je raté quelque chose?

Autres cas concrets
-------------------

Dans le cadre de l'écriture de ce livre python il m'a été proposé pour expérimenter
**invoke** d'automatiser la génération de la doc html (vu au chapitre précédent) et
les vérifications de la conformité du code et de la doc.

Les vérifications restent simple à mettre en place car il s'agit uniquement de commande à lancer
on ne cherche pas ici à avoir un comportement différent selon leur résultat

.. literalinclude:: ../../tasks.py
   :linenos:
   :language: python
   :start-after: # checks start

Exécuter une commande va retourner un objet :py:class:`~invoke.runners.Runner`
il possède différents attributs tel que par exemple le retour de la commande
(ainsi que l’erreur) qui peut permettre de choisir une action à réaliser en
fonction de son contenu.

Conclusion
==========

pyinvoke_ est un outil très puissant, il est très utile par exemple pour automatiser
des processus fastidieux dans la réalisation d'un projet. Au-delà de l'automatisation
utilisé **invoke** permet de lancer n'importe quelle commande standard de l'invite de commande
ce qui offre des possibilités immenses en termes par exemple de partage d'informations
entre plusieurs applications.

.. [#email] <jonathan.guerne@he-arc.ch>

.. _WinError_3: https://github.com/pyinvoke/invoke/issues/345
.. _pyinvoke: http://www.pyinvoke.org/
