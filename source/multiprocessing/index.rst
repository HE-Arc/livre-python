.. _multiprocessing-tutorial:

===============
Multiprocessing
===============

Par Gander Laurent

Introduction
------------

Le module :py:mod:`multiprocessing` utilise les processus plutôt que les threads. Il nous permet de créer plusieurs processus séparés.

Bien que la plupart des CPUs modernes comportent plusieurs coeurs, le code que l’on écrit doit aussi être formatté adéquatement afin d’en tirer pleinement avantage. [#Ref]_

Multiprocessing de python permet d'utiliser un ensemble de processus qui consumeront une liste de tâches contenues dans une :py:mod:`queue`.

:py:mod:`multiprocessing` évite d'être bloqué par le GIL (Global Interpreter Lock) en utilisant des sous-processus au lieu des threads et offre de la concurence local et distant. De ce fait, le module multiprocessing permet au programmeur d'exploiter pleinement plusieurs processeurs sur une machine donnée. Il fonctionne sur Unix et Windows.

Le Global Interpreter Lock est un algorithme qui gère l'exécution de plusieurs threads dans un programme Python. la connaissance du GIL est indispensable lorsque vous travaillez avec plusieurs threads , car la gestion de la mémoire de CPython n'est pas thread-safe .
Le GIL a été connu pour dégrader la performance des programmes.
Un exemple est que cela peut prendre plus de temps pour deux threads d'appeler la même fonction qu'un thread appelant deux fois la fonction.

Les classes
-----------

Process
^^^^^^^

:py:mod:`multiprocessing` contient plusieurs classes très utiles, je vais vous introduire à quelques unes.

Prenons tout d'abord la classe :py:class:`multiprocessing.Process`, la classe :py:class:`multiprocessing.Process` nous permet de créer des processus en créant un objets :py:class:`multiprocessing.Process`, en appelant sa méthode start().

Dans l'exemple suivant nous avons deux fonction en plus du main, dans la première fonction 'info' nous affichons le titre passé en paramètre ainsi que le nom du module, le numero du processus parent et le numero du processus. La deuxième fonction appelle la première fonction et ensuite écrit 'hello + le nom passé en paramètre'.
Dans le main, nous appelons la fonction info puis nous créons un objet Process avec comme arguments 'target = f' qui est la fonction que le processus éxecutera et les arguments de la fonction 'args=('bob')', ensuite nous lancons le processus avec p.start() et p.join().

.. literalinclude:: ./exemples/process.py

Pool
^^^^

Avec la classe Pool on peut avoir un objet pool qui contient une pool de processus qui est capable d'accomplir les tâches qui lui seront soumises.
Pool contient plusieurs méthodes

Queues
^^^^^^

La classe Queue permet la communication entre deux processus.

.. literalinclude:: ./exemples/queue.py

.. warning:: Si un processus est "tué", les données risquent d'être corrompu dans la queue, ce qui signifie qu'un autre processus qui tenterait d'acceder à la file queue risquerait de soulever une exception.

Pipe
^^^^

La classe Pipe permet aussi la communication entre deux processus. Le constructeur du pipe retourne deux objets de connection qui sont l'entrée et la sortie du pipe.

.. literalinclude:: ./exemples/pipe.py

.. warning:: la méthode recv() efface les données qu'elle recoit, ce qui peut être un problème de sécurité, c'est pourquoi vous devriez utiliser une authentification avant d'utiliser les métodes recv() et send(). Si un processus est tué alors qu'il essaie de lire ou d'écrire dans le pipe, il risquerait de corrompre les données dans le pipe.


Contexte et méthode de démarrage
--------------------------------

Il y a plusieurs façon de démarrer un processus, le multiprocessing en contient trois :
        :spawn:
            L'interpréteur Python sera démarré par le processus parent, son enfant n'héritera que des ressources nécessaire pour éxecuter le méthode run().

        :fork:
            os.fork() est utilisé par le processus parent pour forcer l'interpreteur Python. Quand le processus enfant est lancé est identique au processus parent. fork est disponible uniquement sur Linux

        :forkserver:
            Quand le programme est lancé et lance la méthode forkserver.start(), depuis ce moement, chaque fois qu'un processus est nécessaire, un processus est demandé au serveur par le processus parent. Fonctionne que sur Linux


Synchronisation entre les processus
-----------------------------------

:py:mod:`multiprocessing` contient les mêmes méthodes que la classe :py:mod:`threading`. Comme pour un thread, nous pouvons nous assurer qu'un processus accède à une ressource de manière atomique.

.. literalinclude:: ./exemples/synchro.py

Partage de ressources entre processus
-------------------------------------

En programmation multi-processus, il est souvent utile de pouvoir partager des ressources entre nos processus. Pour cela :py:mod:`multiprocessing` offre différentes manières de partager des ressources.

La mémoire :
    On peut partager de la mémoire en utilisant les classes Value ou Array.

    Exemple :

.. literalinclude:: ./exemples/sharedmemory.py

Serveur de processus :
    Un objet renvoyé par la classe Manager() contrôle un serveur de processus qui contient des objets Python et permet à d'autres processus de les manipuler à l'aide de proxies.

    Exemple :

.. literalinclude:: ./exemples/manager.py



Conclusion
----------

Pour conclure, le module de python sur le multiprocessing nous permet de contourner le problème des threads en python, effectivement l'interpreteur Python n'est pas thread safe. Le langage python n'a qu'un seul fil d'exécution, donc il n'est pas possible d'utiliser tout les coeurs en n'utilisant que des threads. C'est pourquoi, on utilise plutôt le module multiprocessing malgré le problème du partage de mémoire entre les processus qui malgré tout sont gérer par les classes Value, Array et Manager.


Pour de plus amples informations :

    Process          : :py:class:`multiprocessing.Process`

    Queues           : :py:class:`multiprocessing.Queue`

    Pipe             : https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe

    Pool             : :py:class:`multiprocessing.pool.Pool`

    Connexion        : :py:class:`multiprocessing.Connection`

    Synchronisation  : https://docs.python.org/3/library/multiprocessing.html#synchronization-primitives

Référence
---------

Les exemples sont repris de la documentation officielle de python : :py:mod:`multiprocessing`

.. [#Ref] http://bioinfo.iric.ca/fr/faites-travailler-vos-cpus/

.. [#gl]<laurent.gander@he-arc.ch>
