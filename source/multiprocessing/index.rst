.. _multiprocessing-tutorial:

===============
Multiprocessing
===============

Par Gander Laurent

Introduction
------------

Le `Multiprocessing <https://docs.python.org/3.6/library/multiprocessing.html>`_ est un module qui utilise les processus plutôt que les threads. Il nous permet de créer plusieurs processus séparés.

[Ref]_ Bien que la plupart des CPUs modernes comportent plusieurs coeurs, le code que l’on écrit doit aussi être formatté adéquatement afin d’en tirer pleinement avantage.

Multiprocessing de python permet d'utiliser un ensemble de processus qui consumeront une liste de tâche contenue dans une queue.

:py:mod:`Multiprocessing` met en place le verrouillage global de l'interpréteur en utilisant des sous-processus au lieu des threads. De ce fait, le module multiprocessing permet au programmeur d'exploiter pleinement plusieurs processeurs sur une machine donnée. Il fonctionne sur Unix et Windows.

Les classes
-----------

Process
^^^^^^^

:py:mod:`Multiprocessing` contient plusieurs classes très utiles, je vais vous introduire à quelques unes. 

Prenons tout d'abord la classe `Process <https://docs.python.org/3.6/library/multiprocessing.html#multiprocessing.Process>`_, la classe `Process <https://docs.python.org/3.6/library/multiprocessing.html#multiprocessing.Process>`_ nous permet de créer des processus en créant un objets `Process <https://docs.python.org/3.6/library/multiprocessing.html#multiprocessing.Process>`_, en appelant sa méthode start().

Dans l'exemple suivant nous avons deux fonction en plus du main, dans la première fonction 'info' nous affichons le titre passé en paramètre ainsi que le nom du module, le numero du processus parent et le numero du processus. La deuxième fonction appelle la première fonction et ensuite écrit 'hello + le nom passé en paramètre'.
Dans le main, nous appelonr la fonction info puis nous créons un objet Process avec comme arguments 'target = f' qui est la fonction que le processus éxecutera et les arguments de la fonction 'args=('bob')', ensuite nous lancons le processus avec p.start() et p.join(). 

.. literalinclude:: ./exemples/process.py

Queue
^^^^^


Pool
^^^^



Contexte et méthode de démarrage
--------------------------------

Il y a plusieurs façon de demarrer un processus, le multiprocessing en contient trois :
		spawn
			L'interpréteur Python sera demarrer par le processus parent, son enfant n'héritera que des ressources nécessaire pour éxecuter le méthode run().

		fork
			os.fork() est utilisé par le processus parent pour forcer l'interpreteur Python. Quand le processus enfant est lancé est identique au processus parent. fork est disponible uniquement sur Linux

		forkserver
			Quand le programme est lancé et lance la méthode forkserver.start(), depuis ce moement, chaque fois qu'un processus est nécessaire, un processus est demandé au serveur par le processus parent. Fonctionne que sur Linux


Echange de données
------------------

			

Conclusion
----------


.. [Ref] http://bioinfo.iric.ca/fr/faites-travailler-vos-cpus/
