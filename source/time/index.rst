.. _time-tutorial:

========
``time``
========

Par Kaser Nicolas


--------------
Introduction
--------------
Le module Time en python (et également en d'autres languages) est une des façons les plus simple de manipuler le temps dans un programme. Ca permet par exemple d'attendre un certain nombre de millisecondes, d'afficher une date avec un format spécifique ou encore de connaître le nombre de secondes écoulées depuis le 1er Janvier 1970 à 00:00 ... Pas forcément utile mais possible. 

Le module DateTime affiche et formate des dates et heures avec une méthode un peu plus orientée objets (une date sera un objet et une heure également).


---------
Time
---------
Avant tout il faut importer la librairie time comme ceci :


.. code:: python 
>>> import time


Maintenant le module Time est disponible pour l'utilisation. 
Il permet plusieurs choses. Notamment d'avoir des informations sur l'horloge du processeur. La ligne suivante retournera la valeur de l'horloge du CPU sous forme de nombre flottant.

.. code:: python 
>>> time.clock()


D'autres fonction comme clock_gettres(clk_id), clock_gettime(clk_id), clock_settime(clk_id, time) permettent d'obtenir la résolution d'une horloge spécifique, le temps ou de setter le temps de cette horloge avec 'clk_id' l'id de l'horloge spécifique.

La commande Time.time() affichera le nombre de seconde écoulées depuis la date appellée "L'Epoch Unix" qui est le 1er Janvier 1970 à 00:00. 
Pourquoi cette date ? L'année 1970 a été considérée comme un bon départ, compte tenu de l'essor qu'a pris l'informatique à partir de cette époque. D'autre part, un ordinateur est inévitablement limité quand il traite des entiers ; dans les langages de l'époque, il fallait tenir compte de ce fait tout simple : on ne pouvait pas compter un nombre de secondes trop important. La date de l'Epoch ne pouvait donc pas être trop reculée dans le temps. (Source : openclassromm).  

   
Donc:

.. code:: python 
>>> time.time()


Affichera : 1490354301.5397666


La fonction ctime([secs]), quand elle est appellée sans paramètre retourne la date d'ajourd'hui au format texte.


.. code:: python 
>>> time.ctime()


Affichera : 'Thu Mar 23 12:34:03 2017'


En revanche avec un paramètre qui correspond à un nombre de secondes, ça affichera la date de l'Epoch après que ce nombre de secondes se soit écoulé.



.. code:: python 
>>> time.ctime(2000)


Affichera : 'Thu Jan  1 01:33:20 1970'



.. code:: python 
>>> time.ctime(400000000)


Affichera : 'Sat Sep  4 17:06:40 1982'


.. code:: python 
>>> time.ctime(22222222222)


Affichera : 'Thu Mar 12 16:30:22 2674'


D'autres commandes peuvent retourner une date au format struct_time qui est une structure possédant les informations sur une date et ayant la forme suivante :  


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


.. code:: python 
>>> time.localtime()


Affichera : time.struct_time(tm_year=2017, tm_mon=3, tm_mday=24, tm_hour=13, tm_min=30, tm_sec=4, tm_wday=4, tm_yday=83, tm_isdst=0)


.. code:: python 
>>> time.localtime(400000000)


Affichera : time.struct_time(tm_year=1982, tm_mon=9, tm_mday=4, tm_hour=17, tm_min=6, tm_sec=40, tm_wday=5, tm_yday=247, tm_isdst=1)

