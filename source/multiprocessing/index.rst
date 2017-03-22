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

:py:mod:`multiprocessing` evite de bloquer le GIL (Global Interpreter Lock) en utilisant des sous-processus au lieu des threads et offre de la concurence local et distant. De ce fait, le module multiprocessing permet au programmeur d'exploiter pleinement plusieurs processeurs sur une machine donnée. Il fonctionne sur Unix et Windows.

Les classes
-----------

Process
^^^^^^^

:py:mod:`multiprocessing` contient plusieurs classes très utiles, je vais vous introduire à quelques unes. 

Prenons tout d'abord la classe :py:class:`multiprocessing.Process`, la classe :py:class:`multiprocessing.Process` nous permet de créer des processus en créant un objets :py:class:`multiprocessing.Process`, en appelant sa méthode start().

Dans l'exemple suivant nous avons deux fonction en plus du main, dans la première fonction 'info' nous affichons le titre passé en paramètre ainsi que le nom du module, le numero du processus parent et le numero du processus. La deuxième fonction appelle la première fonction et ensuite écrit 'hello + le nom passé en paramètre'.
Dans le main, nous appelonr la fonction info puis nous créons un objet Process avec comme arguments 'target = f' qui est la fonction que le processus éxecutera et les arguments de la fonction 'args=('bob')', ensuite nous lancons le processus avec p.start() et p.join(). 

.. literalinclude:: ./exemples/process.py

Pool
^^^^

Avec la classe Pool on peut avoir un objet pool qui contient une pool de processus qui est capable d'accomplir les tâches qui lui seront soumises.
Pool contient plusieurs méthodes

Queues
^^^^^^

La classe Queue permet la communication entre deux processus.

.. literalinclude:: ./exemples/queue.py

Warning : Si un processus est "tué", les données risquent d'être corrompu dans la queue, ce qui signifie qu'un autre processus qui tenterait d'acceder à la file queue risquerait de soulever une exception.

Pipe
^^^^

La classe Pipe permet aussi la communication entre deux processus. Le constructeur du pipe retourne deux objet de connection qui sont l'entrée et la sortie du pipe.

.. literalinclude:: ./exemples/pipe.py

Warning : la méthode recv() efface les données qu'elle recoit, ce qui peut être un problème de sécurité, c'est pourquoi vous devriez utiliser une authentification avant d'utiliser les métodes recv() et send(). Si un processus est tué alors qu'il essaie de lire ou d'écrire dans le pipe, il risquerait de corrompre les données dans le pipe.


Contexte et méthode de démarrage
--------------------------------

Il y a plusieurs façon de demarrer un processus, le multiprocessing en contient trois :
		spawn
			L'interpréteur Python sera demarrer par le processus parent, son enfant n'héritera que des ressources nécessaire pour éxecuter le méthode run().

		fork
			os.fork() est utilisé par le processus parent pour forcer l'interpreteur Python. Quand le processus enfant est lancé est identique au processus parent. fork est disponible uniquement sur Linux

		forkserver
			Quand le programme est lancé et lance la méthode forkserver.start(), depuis ce moement, chaque fois qu'un processus est nécessaire, un processus est demandé au serveur par le processus parent. Fonctionne que sur Linux


Synchronisation entre les processus
-----------------------------------

:py:mod:`multiprocessing` contient les mêmes méthodes équivalente que la classe :py:mod:`threading`. Comme pour un thread, nous pouvons s'assurer qu'un processus accède à une ressource de manière atomique.

.. literalinclude:: ./exemples/synchro.py

Partage de ressources entre processus
-------------------------------------

En programmation multi-processus, il est souvent utile de pouvoir partager des ressources entre nos processus. Pour cela :py:mod:`multiprocessing` offre différentes manière de partager des ressources.

La mémoire : 
	on peut partage de la mémoire en utilisant les classes Value ou Array.

	Exemple :

.. literalinclude:: ./exemples/sharedmemory.py

Serveur de processus :
	Un objet renvoyé par la classe Manager() contrôle un serveur de processus qui contient des objets Python et permet à d'autres processus de les manipuler à l'aide de proxies.

	Exemple :

.. literalinclude:: ./exemples/manager.py



Conclusion
----------

Le module :py:mod:`multiprocessing` nous permet de gérer nos processeurs.

Reference
---------

.. [Ref] http://bioinfo.iric.ca/fr/faites-travailler-vos-cpus/
