.. _time-tutorial:

=======================
``time`` / ``datetime``
=======================

Par Nicolas Kaser [#nk]_

------------
Introduction
------------

Le module :py:mod:`time` en python est une des façons les plus simple de manipuler le temps dans un programme. Un temps en python est, par défaut, un nombre représentant des secondes. Ca permet par exemple d'attendre un certain nombre de secondes, d'afficher une date avec un format spécifique ou encore de connaître le nombre de secondes écoulées depuis le 1er Janvier 1970 à 00:00 ... Pas forcément utile mais possible.

Le module :py:mod:`datetime` affiche et formate des dates et heures avec une méthode un peu plus orientée objets (une date et une heure seront des objets).


--------
``time``
--------

Maintenant le module Time est disponible pour l'utilisation.
Il permet plusieurs choses. Notamment d'avoir des informations sur l'horloge du processeur. La ligne suivante retournera la valeur de l'horloge du CPU sous forme de nombre flottant.

.. code-block:: pycon

    >>> time.clock()


.. todo:: Ceci est faux. L'horloge du mur n'a rien à voir avec l'horloge du CPU.

D'autres fonction comme clock_gettres(clk_id), clock_gettime(clk_id), clock_settime(clk_id, time) permettent d'obtenir la résolution d'une horloge spécifique, le temps ou de setter le temps de cette horloge avec 'clk_id' l'id de l'horloge spécifique.

La commande Time.time() affichera le nombre de seconde écoulées depuis la date appellée "L'Epoch Unix" qui est le 1er Janvier 1970 à 00:00.
Pourquoi cette date ? L'année 1970 a été considérée comme un bon départ, compte tenu de l'essor qu'a pris l'informatique à partir de cette époque. D'autre part, un ordinateur est inévitablement limité quand il traite des entiers ; dans les langages de l'époque, il fallait tenir compte de ce fait tout simple : on ne pouvait pas compter un nombre de secondes trop important. La date de l'Epoch ne pouvait donc pas être trop reculée dans le temps. (Source : openclassroom).

.. URL?

Donc:

.. code-block:: pycon

    >>> time.time()
    1490354301.5397666


La fonction ctime([secs]), quand elle est appellée sans paramètre retourne la date d'aujourd'hui au format texte.


.. code-block:: pycon

    >>> time.ctime()
    'Thu Mar 23 12:34:03 2017'

En revanche avec un paramètre qui correspond à un nombre de secondes, ça affichera la date de l'Epoch après que ce nombre de secondes se soit écoulé.


.. code-block:: pycon

    >>> time.ctime(2000)
    'Thu Jan  1 01:33:20 1970'

    >>> time.ctime(400000000)
    'Sat Sep  4 17:06:40 1982'

    >>> time.ctime(22222222222)
    'Thu Mar 12 16:30:22 2674'

.. todo:: pourquoi 2000, 4e8 et 2222..2 ??

D'autres commandes peuvent retourner une date au format struct_time qui est une structure possédant les informations sur une date et ayant la forme suivante:

::

    Index-------Attribute----------------Values

    0 ----------> tm_year ----------> (for example, 1993)

    1 ----------> tm_mon ----------> range [1, 12]

    2 ----------> tm_mday ----------> range [1, 31]

    3 ----------> tm_hour ----------> range [0, 23]

    4 ----------> tm_min ----------> range [0, 59]

    5 ----------> tm_sec ----------> range [0, 61];

    6 ----------> tm_wday ----------> range [0, 6], Monday is 0

    7 ----------> tm_yday ----------> range [1, 366]

    8 ----------> tm_isdst ----------> 0, 1 or -1

    N/A ----------> tm_zone ----------> abbreviation of timezone name

    N/A ----------> tm_gmtoff ----------> offset east of UTC in seconds


Contrairement au langage C, la valeur du mois se donne en valeur entre 1 et 12 alors qu'en C c'est entre 0 et 11.

La fonction Time.localtime([secs]) retourne la même chose que Time.ctime([secs]) mais cette fois ci au format struct_time.


.. code-block:: pycon

    >>> time.localtime()


Affichera : time.struct_time(tm_year=2017, tm_mon=3, tm_mday=24, tm_hour=13, tm_min=30, tm_sec=4, tm_wday=4, tm_yday=83, tm_isdst=0)


.. code-block:: pycon

    >>> time.localtime(400000000)

Affichera : time.struct_time(tm_year=1982, tm_mon=9, tm_mday=4, tm_hour=17, tm_min=6, tm_sec=40, tm_wday=5, tm_yday=247, tm_isdst=1)


La fonction Time.mktime(t) fais l'inverse de localtime() en prenant une struct_time en argument et en retournant un nombre de secondes (par rapport à l'Epoch).

Voici un exemple d'utilisation :

.. code-block:: python

    >>> t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
    >>> secs = time.mktime( t )
    >>> print "time.mktime(t) : %f" %  secs
    >>> print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))


Qui retournera le résultat suivant :

time.mktime(t) : 1234915418.000000

asctime(localtime(secs)): Tue Feb 17 17:03:38 2009


Il existe également un moyen de faire attendre le programme avec le module Time.
Il s'agit de Time.sleep(secs) avec secs = le nombre de secondes à attendre. Il bloquera ainsi le thread appellant pendant ce laps de temps. Attention. Contrairement à d'autres langages, l'argument est bien en secondes et pas en millisecondes.


.. code-block:: python

    >>> time.sleep(1000)

En c# par exemple cette ligne bloque le thread en question pendant une seconde. Ici en python il le bloque bien pendant 1000 secondes !!

.. et alors?

------------
``datetime``
------------

:py:mod:`datetime` permet également de manipuler des dates et des temps.

Ce module, plus orienté objet, possède plusieurs types :

date
^^^^

Représente une date du calendrier Grégorien. Ses attributs sont: year, month et day

.. code-block:: pycon

    >>> d = datetime.date.today()
    >>> d.day
    24
    >>> d.month
    3
    >>> d.year
    2017


Ainsi on voit qu'on peut afficher les attributs dans l'ordre qu'on veut et ou l'on veut


time
^^^^

Représente un temps. Ses attributs sont: hour, minute, second, microsecond et tzinfo.

.. code-block:: pycon

    >>> time(hour=12, minute=34, second=56, microsecond=123456).isoformat(timespec='minutes')
    '12:34'
    >>> dt = time(hour=12, minute=34, second=56, microsecond=0)
    >>> dt.isoformat(timespec='microseconds')
    '12:34:56.000000'
    >>> dt.isoformat(timespec='auto')
    '12:34:56'

datetime
^^^^^^^^

Une combinaison d'une date et d'un temps. Ses attributs sont: year, month, day, hour, minute, second, microsecond et tzinfo.

.. code-block:: pycon

    >>> datetime.now().isoformat(timespec='minutes')
    '2002-12-25T00:00'
    >>> dt = datetime(2015, 1, 1, 12, 30, 59, 0)
    >>> dt.isoformat(timespec='microseconds')
    '2015-01-01T12:30:59.000000'


timedelta
^^^^^^^^^

Une durée exprimant la différence entre deux date, time ou datetime.

.. code-block:: python

    >>> from datetime import timedelta
    >>> d = timedelta(microseconds=-1)
    >>> (d.days, d.seconds, d.microseconds)

Affichera :


(-1, 86399, 999999)

tzinfo
^^^^^^

Classe abstraite utilisée par datetime et time pour fournir une notion personnalisable de réglage de l'heure (par exemple, pour l'heure d'été).


timezone
^^^^^^^^

Classe qui implémente tzinfo


La méthode strftime(format) converti une date en string et permet le formatage de celle-ci. Strptime(format) permet,quand à elle, de convertir en datetime.


----------
Conclusion
----------

Pour conclure on peut dire que Time et DateTime sont des modules tout de même assez proches dans le cadre de leur utilisation. La principale différence est que DateTime est plus orienté objet et permet de faire des manipulations plus complexes et terme de traitement et d'affichage.

Time en revanche à accès à l'horloge, aux données CPU et également à son thread parent (Time.sleep(x) et l'équivalent d'un thread.sleep(x) dans d'autre languages).


.. [#nk] <nicolas.kaser@he-arc.ch>
