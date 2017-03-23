.. _datetime-tutorial:

============
``datetime``
============

Par Mohamed Jmaa 

Introduction
============

Le module :py:mod:`datetime` propose plusieurs classes pour représenter des dates et heures. Vous n'allez rien découvrir d'absolument 
spectaculaire dans cette section mais nous nous avançons petit à petit vers une façon de gérer les dates et heures qui est 
davantage orientée objet.

Encore et toujours, je ne prétends pas remplacer la documentation. Je me contente d'extraire de celle-ci les informations 
qui me semblent les plus importantes. Je vous encourage, là encore, à jeter un coup d'œil du côté de la documentation du module 
datetime.

Représenter une date
====================

c'est bien d'avoir accès au temps actuel avec une précision d'une seconde sinon plus… 
mais parfois, cette précision est inutile. Dans certains cas, on a juste besoin d'une date, c'est-à-dire un jour, un mois et une année.
Il est naturellement possible d'extraire cette information de notre timestamp. Le module :py:mod:`datetime` propose une classe :py:class:`~datetime.date`,
représentant une date, rien qu'une date.

L'objet possède trois attributs :
---------------------------------

year : l'année ;
month : le mois ;
day : le jour du mois.

Il y a plusieurs façons de procéder. Le constructeur de cette classe prend trois arguments qui sont, dans l'ordre, l'année, le mois et le jour du mois.

.. code-block:: python3

	>>> import datetime
	>>> date = datetime.date(2017, 3, 21)
	>>> print (date)
	2017-03-21
	>>> 

	
Il existe deux méthodes de classe qui peuvent etre intéresser :

	:py:meth:`datetime.date.today()` : renvoie la date d'aujourd'hui ;
	:py:meth:`datetime.date.fromtimestamp()` : renvoie la date correspondant au timestamp passé en argument.

Exemple	:

.. code-block:: python3

	>>> import time
	>>> import datetime
	>>> aujourdhui = datetime.date.today()
	>>> aujourdhui
	datetime.date(2017, 3, 23)
	>>> datetime.date.fromtimestamp(time.time()) 
	datetime.date(2017, 3, 23)
	>>>
	
Bien sur npus pouvons manipuler ces dates simplement et les comparer grâce aux opérateurs usuels.

Représenter une heure
---------------------

C'est moins courant mais on peut également être amené à manipuler une heure, indépendemment de toute date. La classe :py:class:`datetime.time` du module :py:mod:`datetime` est là pour cela.

On construit une heure avec non pas trois mais cinq paramètres, tous optionnels :

:py:obj:`datetime.time.hour` (0 par défaut) : les heures, valeur comprise entre 0 et 23 ;
:py:obj:`datetime.time.minute` (0 par défaut) : les minutes, valeur comprise entre 0 et 59 ;
:py:obj:`datetime.time.second` (0 par défaut) : les secondes, valeur comprise entre 0 et 59 ;
:py:obj:`datetime.time.microsecond` (0 par défaut) : la précision de l'heure en micro-secondes, entre 0 et 1.000.000 ;
:py:obj:`datetime.time.tzinfo` (None par défaut) : l'information de fuseau horaire (je ne détaillerai pas cette information ici).
Cette classe est moins utilisée que :py:class:`~datetime.date` mais elle peut se révéler utile dans certains cas.

Représenter des dates et heures
-------------------------------

On peut naturellement représenter une date et une heure dans le même objet, ce sera probablement la classe que nous utiliserons le plus souvent. Celle qui nous intéresse s'appelle :py:mod:`datetime`, comme son module.

Elle prend d'abord les paramètres de :py:class:`datetime.date` (année, mois, jour) et ensuite les paramètres de :py:class:`datetime.time` (heures, minutes, secondes, micro-secondes et fuseau horaire).

les deux méthodes de classe que nous utiliserons le plus souvent :

`datetime.date.now()` : renvoie l'objet datetime avec la date et l'heure actuelles ;
`datetime.date.fromtimestamp()` (timestamp) : renvoie la date et l'heure d'un timestamp précis.

.. code-block:: python3

	>>> import datetime
	>>> datetime.datetime.now()
	datetime.datetime(2017, 3, 21, 5, 8, 22, 359000)
	>>>
	
Conclusion
==========
Il y a bien d'autres choses à voir dans ce module :py:mod:`datetime` que je n'ai pas traiter dans ce document vous pouvez toujours vous y referer au documentation officielle du module.
