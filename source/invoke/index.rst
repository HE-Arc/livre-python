=======
.. _Invoke-tutorial:
======
invoke
======
Par Jonathan Guerne

Introduction
============
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

code source tiré de la documentation_  officielle de invoke



Installation
============
pour pouvoir utiliser les commandes propres à la librairie Invoke il faut d'abord
s'assurer de l'avoir installée dans son environnememt python.
Comme d'habitude on utilise pip pour installer des librairies externe.

::

  $ pip install invoke

Exemple
=======

lancer une tâche
----------------
Dans un projets simple il est préférable de stocker les tâches dans un fichier nommé ``tasks.py`` (le nom du fichier est important).
Il est cependant possible de stocker des tâches dans plusieurs fichiers en utilisant des namespaces

le fichier ``tasks.py`` doit commencer par importer les éléments invoke dont il va
avoir besoin. Cela est fait avec la ligne suivante :

.. code:: python3

  from invoke import task

task est l'élément essentiel à la création de tâche avec Invoke, il faudra pratiquememt toujours
l'importer.

On arrive à l'écriture de la tâche en elle-même. Sa sytaxe est très proche de
celle d'une simple fonction :

.. code-block:: python3

  @task
   def build(args)
      print("do stuff")

La seule nouveauté quand on a déjà codé des focntions en python est la ligne ``@task`` précédant
la focntion elle-même. Comme on peut le voir sur l'exemple il est tout a fait possible d'utiliser
des paramètres pour influencer le comportement de sa tâche.

une fois les tâches écrites on peut lancer un invite de commande afin de les tester.
Pour pouvoir savoir quelle tâches sont disponible pour notre projet on peut utiliser la commande suivante
pour les lister :

::

  $ invoke -l

Maintenant, si on veut lancer la tâche **build** il faut le faire de cette façon :

::

  $ invoke build

si on a envie d'obtenir de l'aide sur la commande **build** notamment ses paramtères on utilise
cette commande :

::

  $invoke --help build


finalement pour lancer une commande en lui spécifiant ses arguments il faut écrire ceci :

::

  $invoke build -args lalala

ici on passe comme paramètre args la valeur "lalala". Par défaut les paramètres sont interprétés
comme des chaînes de caractères.

Lancer une commande
-------------------
En guise d'exemple nous allons ici étudier comment utiliser Invoke pour pouvoir
faciliter l'utilisation de la librairie sphinx en générant des pages HTML avec des
fichiers écrits au format rst (comme celui-ci)

.. literalinclude:: ./examples/basic-sphinx.py

la permière ligne sert évidemment à importer les éléments de la librairies Invoke
avec lesquels on désir travailler. Ici en loccurence comme dans tous les programme utilisant
les ``@task`` de Invok on importe **task**, on va également importer **run** qui va nous permettre
de lancer nos commandes.

le code en lui-même est très simple est au final ne contient pas beaucoup plus de ligne
que le premier exemple présenter en haut de ce document. La seule subtilié est que
pour pouvoir lancer une commande on va devoir utiliser un contexte (ici appelé **ctx**)
qui sera placé en argument de la tâche. il suffit ensuite d'appelé la méthode run dans
le contexte et de passer en argument une chaîne de caractère pour lancer la commande.

.. Attention::
   Sous windows on peut rencontrer des problèmes au lancemement des commandes.
   En effet il est possible que Invoke ait besoin de connaître l'adresse de
   l'invite de commande à utiliser. Pour cela on va mettre en place un fichier de
   configuration contenant cette information (cf. WinError_3_)


on peut également mettre en place un système plus poussé qui va par exemple nettoyer
le dossier de destination avant de générer le contenu HTML

.. literalinclude:: ./examples/sphinx.py

pour qu'une tâche A appelle une tâche B avant son exécution il suffit d'utiliser la
syntaxe suivante.

.. code-block:: python3

  @task
   def B()
        print("task B")

  @task(B)
  def A()
      print("task A")

si un appel à la tâche A est fait, la sortie sera la suivante :

::

  $ invoke A
  task B
  task A

Autres cas concret
------------------
Dans le cadre de l'écriture de ce livre python il m'a été proposé pour expérimenter
**Invoke** d'automatiser la génération de la doc html (vu au chapitre précédent),
les checks du code et de la doc ainsi que le rebase du projet(importation du contenu
du git remote et ajout des modifications de la bracnhe locale).

les checks restent simple à mettre en place car il s'agit uniquement de commande à lancer
on ne cherche pas ici à avoir un coportement différent selon leur résultat

.. literalinclude:: ./examples/check.py

La mise en place de l'automatisation du rebase est elle plus poussée. Elle va en
effet demander l'analyse des résultats des commandes pour déterminer les actions
à suivre.


.. literalinclude:: ./examples/git.py



Conclusion
==========
Invoke_ est un outil très puissant, il est très utile par exemple pour automatisé
des processus fastidieux dans la réalisation d'un projet. Au delà de l'automatidation
utilisé **Invoke** permet de lancer n'importe quelle commande standard de l'invite de commande
ce qui offre des possibilités immenses en termes par exemple de partage d'informations
entre plusieurs applications.


.. _WinError_3: https://github.com/pyinvoke/invoke/issues/345
.. _Invoke: http://www.pyinvoke.org/
.. _documentation: http://docs.pyinvoke.org/en/latest/
