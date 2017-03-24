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
