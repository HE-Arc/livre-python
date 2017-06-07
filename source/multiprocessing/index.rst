.. _multiprocessing-tutorial:

===================
``multiprocessing``
===================

Par Laurent Gander [#gl]_

Introduction
------------

Le module :py:mod:`multiprocessing` utilise les processus plutôt que les threads. Il nous permet de créer plusieurs processus séparés.

  Bien que la plupart des CPUs modernes comportent plusieurs coeurs, le code que l’on écrit doit aussi être formatté adéquatement afin d’en tirer pleinement avantage. [#Ref1]_

:py:mod:`multiprocessing` évite d'être bloqué par le GIL (Global Interpreter Lock) en utilisant des sous-processus au lieu des threads et offre de la concurrence locale et distante. De ce fait, le module multiprocessing permet au programmeur d'exploiter pleinement plusieurs processeurs sur une machine donnée. Il fonctionne sur Unix et Windows.

GIL?
^^^^

Le *Global Interpreter Lock* est un verrou (*lock*) que l'interpréteur demande afin d'être *thread-safe* sur le comptage des références du ramasse-miette. La connaissance du GIL est indispensable lorsque vous travaillez avec plusieurs threads. Le GIL a été connu pour dégrader la performance des programmes.
Un exemple est que cela peut prendre plus de temps pour deux threads d'appeler la même fonction qu'un thread appelant deux fois la fonction. [#Ref2]_

Les classes
-----------

Process
^^^^^^^

:py:mod:`multiprocessing` contient plusieurs classes très utiles, je vais vous en introduire quelques unes.

Prenons tout d'abord la classe :py:class:`multiprocessing.Process`, la classe :py:class:`multiprocessing.Process` nous permet de créer des processus en créant un objets :py:class:`multiprocessing.Process`, en appelant sa méthode start().

Dans l'exemple suivant nous avons deux fonctions en plus du main, dans la première fonction 'info' nous affichons le titre passé en paramètre ainsi que le nom du module, le numero du processus parent et le numero du processus. La deuxième fonction appelle la première fonction et ensuite écrit 'hello + le nom passé en paramètre'.
Dans le main, nous appelons la fonction info puis, nous créons un objet Process avec comme arguments 'target = f' qui est la fonction que le processus exécutera et les arguments de la fonction 'args=('bob')', ensuite nous lancons le processus avec p.start() et p.join().

.. literalinclude:: ./exemples/process.py

Résultat de l'exemple ci-dessus :

.. code-block:: console

  main line
  hello bob
  module name: __mp_main__
  parent process: 1664
  process id: 14628

.. manque d'exemple pour être utile.
   Pool
   ^^^^
   Avec la classe Pool on peut avoir un objet pool qui contient une pool de processus qui est capable d'accomplir les tâches qui lui seront soumises.

Queues
^^^^^^

La classe Queue permet de créer un canal de communication entre plusieurs processus.

.. literalinclude:: ./exemples/queue.py

L'exemple ci-dessus nous affiche :

.. code-block:: console

    [42, None, 'hello']

.. warning:: Si un processus est "tué" à l'aide des fonctions terminate() ou de os.kill(), les données risquent d'être corrompues dans la queue, en effet on ne sait pas si le processus est finit, des commandes risquent d'être encore à l'interieur. Ce qui signifie qu'un autre processus qui tenterait d'accéder à la queue risquerait de soulever une exception.

Pipe
^^^^

La classe Pipe permet aussi la création d'un canal bidirectionnel entre deux processus. Le constructeur du pipe retourne deux objets de connexion qui sont l'entrée et la sortie du canal.

.. literalinclude:: ./exemples/pipe.py

L'exemple ci-dessus nous affiche :
.. code-block:: console

    [42, None, 'hello']


Les objets de connexions ont deux méthodes : recv() et  send() qui leurs permet de lire et d'écrire dans un canal.
Les données dans un tuyau peuvent être corrompues si deux processus (ou threads) tentent de lire ou d'écrire à la même extrémité du tuyau en même temps.


Contexte et méthodes de démarrage
---------------------------------

Il y a plusieurs façons de démarrer un processus, le multiprocessing en contient trois :
        :spawn:
            L'interpréteur Python sera démarré par le processus parent, son enfant n'héritera que des ressources nécessaires pour executer la méthode ``run()``.

        :fork:
            ``os.fork()`` est utilisé par le processus parent pour fork l'interpreteur Python. Quand le processus enfant est lancé, ses ressources sont identiques au processus parent. **fork** est disponible uniquement sur Unix.

        :forkserver:
            Quand le programme est lancé et lance la méthode forkserver.start(), depuis ce moment, chaque fois qu'un processus est nécessaire, un processus est demandé au serveur par le processus parent. **forkserver** fonctionne que sur Unix.


Synchronisation entre les processus
-----------------------------------

:py:mod:`multiprocessing` contient les mêmes méthodes que la classe :py:mod:`threading`. Comme pour un thread, nous pouvons nous assurer qu'un processus accède à une ressource de manière atomique.

.. literalinclude:: ./exemples/synchro.py

Résultat de l'exemple :

.. code-block:: console

    hello world 1
    hello world 2
    hello world 0
    hello world 3
    hello world 5
    hello world 6
    hello world 7
    hello world 4
    hello world 8
    hello world 9

Partage de ressources entre processus
-------------------------------------

En programmation multi-processus, il est souvent utile de pouvoir partager des ressources entre nos processus. Pour cela :py:mod:`multiprocessing` offre différentes manières de partager des ressources.

La mémoire :
    On peut partager de la mémoire en utilisant les fonctions:

     :py:func:`multiprocessing.Value`

     :py:func:`multiprocessing.Array`

    Exemple :

.. literalinclude:: ./exemples/sharedmemory.py

Résultat :

.. code-block:: console

    3.1415927
    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]


Serveur de processus :

    Un objet renvoyé par Manager() contrôle un serveur de processus qui contient des objets Python et permet à d'autres processus de les manipuler à l'aide de proxies.

    Exemple :

.. literalinclude:: ./exemples/manager.py

Résultat :

.. code-block:: console

    {1: '1', '2': 2, 0.25: None}
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

Conclusion
----------

Pour conclure, le module de python sur le multiprocessing nous permet de contourner le problème des threads en python, effectivement l'interpreteur Python n'est pas fait pour le multi-threading à cause du GIL, vu qu'il impose en pratique qu'un seul coeur travaille en même temps. Le langage python n'a qu'un seul fil d'exécution, donc il n'est pas possible d'utiliser tous les coeurs en n'utilisant que des threads. C'est pourquoi, on utilise plutôt le module multiprocessing, en effet mettre chaque travail dans un thread séparé pourrait l'aider un peu parce que, lorsqu'une connexion est inactif, on peut obtenir un certain temps CPU, mais le traitement ne se fera pas en parallèle à cause du GIL. En mettant chaque travail dans un processus, chacun peut s'exécuter sur son propre processeur et s'exécuter à plein rendementm malgré le problème du partage de mémoire entre les processus qui malgré tout sont gérés par les fonctions Value, Array et Manager ou en faisant de l'asynchrome avec :py:mod:`asyncio`.


Pour de plus amples informations :

    Process          : :py:class:`multiprocessing.Process`

    Queues           : :py:class:`multiprocessing.Queue`

    Pipe             : :py:func:`multiprocessing.Pipe`

    Pool             : :py:class:`multiprocessing.pool.Pool`

    Connexion        : :py:class:`multiprocessing.Connection`

    Synchronisation  : [#Synchronisation]_

Références
----------

Les exemples sont repris de la documentation officielle de python : :py:mod:`multiprocessing`

.. [#Ref1] http://bioinfo.iric.ca/fr/faites-travailler-vos-cpus/

.. [#Ref2] http://www.ordinateur.cc/programmation/Programmation-Python/93447.html

.. [#Synchronisation] https://docs.python.org/3/library/multiprocessing.html#synchronization-primitives

.. [#gl] <laurent.gander@he-arc.ch>
