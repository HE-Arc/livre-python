.. _hug-tutorial:

=======
``hug``
=======

Par Charles Ombang Ndo [#co]_

Introduction
============

Une API (Application Programming Interface) est une façade regroupant des
services qu'une application, offre à d'autres. Ces services sont définis sous
forme de classes, de méthodes et généralement suivis d'une documentation
décrivant le rôle de chaque composant de l'interface, exposant les utilisations
possibles et les normes d'utilisation. La plupart des applications actuelles
offrent ces *web services* plus connues sous RESTful web service.

Dans l'univers Python, la bibliothèque hug_ est un outil assez puissant
permettant d'implémenter une API. L'utilisation de la technologie ``hug`` pour
créer des APIs en Python est motivée par de nombreux avantages qui seront
détaillés dans un chapitre dédié.

RESTful web service et ``hug``
------------------------------

A l'origine REST (Representational State Transfer) est l'idée de définir un
ensemble de règles qui mises ensemble, permettent de construire une API et
décrivent la manière, donc la communication se passe entre le client et le
serveur. Les dévéloppeurs n'ont plus à écrire leur propre méthode HTTP (GET,
POST..) pour récupérer des données, c'est REST qui va définir de manière unique
les méthodes à utiliser. La conséquence directe est que quelque soit la
technologie employée côté serveur, les règles ne changeront pas, elles seront
tout le temps les mêmes.

Le concept RESTful web service repose sur les ressources qui sont représentées
par les `URLs`. Le client envoie des requêtes via ces URLs au moyen des
méthodes du protocole HTTP, ce sont les verbes:
- GET: récupération de données,
- POST: ajout de données
- PUT: modifications de données
- DELETE: suppression de données.

Les formats d'échanges sont nombreux. Dans ce chapitre, nous resterons sur du
:ref:`JSON <json-tutorial>`.

Pourquoi choisir ``hug``
------------------------

Les très célèbres frameworks que sont Flask_ et Django_ sont bousculés par les
performances qu'apportent hug. hug permet d'écrire une API de manière
simplifiée. Les API implémentées dans d'autres frameworks peuvent l'être en
quelques lignes avec hug. hug supporte le versioning, il permet la
documentation par le code et hug intègre la validation des données.

Fonctionnement
==============

Supposons une simple fonction permettant de faire la somme de deux nombres passés en paramètre.

.. code-block:: python3

    """Simple application effectuant une somme de deux nombres"""

    def somme(val1, val2):
        """Retourne la somme des deux nombres passés en paramètre"""
        return val1 + val2

Pour transformer cette fonction en une simple API, il suffit d'importer la
bibliothèque hug_ et le tour est joué. Le code du fichier ``somme.py``.

.. code-block:: python3

    """Simple application effectuant une somme de deux nombres"""
    import hug

    @hug.get()
    def somme(val1, val2):
      """Retourne la somme des deux nombres passés en paramètre"""
      return val1 + val2


L'exécution du code ci-dessus via la commande.

.. code-block:: console

    $ hug -f somme.py

hug_ lance le serveur sur le port 8000. En entrant l'adresse
``http://localhost:8000`` on a une réponse au format JSON. Dans notre exemple
on obtient:

.. code-block:: json

    {
        "404": "The API call you tried to make was not defined. Here's a definition of the API to help you get going :)",
        "documentation": {
        "overview": "Simple API permettant la somme de deux nombres",
            "handlers": {
                "/somme": {
                    "GET": {
                        "usage": "La fonction retourne le résultat obtenu de la somme des deux nombres en param\u00e8tres",
                        "outputs": {
                            "format": "JSON (Javascript Serialized Object Notation)",
                            "content_type": "application/json"
                        },
                        "inputs": {
                            "val1": {
                                "type": "Basic text / string value"
                            },
                            "val2": {
                                "type": "Basic text / string value"
                            }
                        }
                    }
                }
            }
        }
    }

On peut remarquer que la documentation est très claire, la clé `overview` nous renseigne sur l'objectif de notre API, La clé usage renseigne sur le type de données renvoyées par l'API, dans notre cas, la ligne de code @hug.get() indique qu'il s'agit d'une requête GET. La suite du bloc JSON ci-dessus nous renseigne sur les paramètres des l'API, leurs types et le format de retour.

Maintenant pour voir le résultat de notre (petite) API, il suffit d'entrer dans le navigateur l'adresse suivante localhost:8000/somme?val1=..&val2= .. il suffit de passer les valeurs aux paramètres.


hug et le versioning
====================

Comme souligné auparavant, hug supporte et gère très bien le versioning. On peut avoir plusieurs versions de l'API dans la même application.


.. code-block:: python3

    """Simple Exemple du versioning avec hug"""
    import hug

    @hug.get('/echo', versions=1)
    def echo(text):
        return text


    @hug.get('/echo', versions=range(2, 5))
    def echo(text):
        return "Echo: {text}".format(**locals())


Le code ci-dessus montre la façon dont hug gère le versioning. Il suffit pour cela d'ajouter dans la méthode GET les versions que l'on veut. C'est une fois de plus assez claire, simple et compréhensible.

On peut déduire du code précédent que l'on a 4 versions. Pour le vérifier, il suffit de mettre dans le navigateur l'adresse http://localhost:8000, on a alors la documentation au format JSON suivante:

.. code-block:: json

    {
        "404": "The API call you tried to make was not defined. Here's a definition of the API to help you get going :)",
        "documentation": {
            "overview": "Simple Exemple du versioning avec hug",
            "version": 4,
            "versions": [
                1,
                2,
                3,
                4
            ],
            "handlers": {
                "/echo": {
                    "GET": {
                        "outputs": {
                            "format": "JSON (Javascript Serialized Object Notation)",
                            "content_type": "application/json"
                        },
                        "inputs": {
                            "text": {
                                "type": "Basic text / string value"
                            }
                        }
                    }
                }
            }
        }
    }

Si on compare ce rendu JSON au précédent, on remarque la présence du champ
``version``. La clé ``version`` de valeur 4 indique la version actuelle de l'API et
la clé ``versions`` prend en valeur un tableau listant les différentes versions
de notre API. Pour tester le bon fonctionnement du versioning, on peut écrire
<http://localhost:8000/v1/echo?text=toto>. Dans cette URL, on spécifie la version
que l'on souhaite utiliser, ici la version v1. En sortie on aura ``toto``, ce qui
correspond bien à la sortie attendue de la version 1. En changeant dans l'URL
juste la version en la remplaçant par v2, v2 ou v4, la sortie est naturellement
celle attendue suivant la version indiquée ``Echo:toto``.


*Type annotation* et validation
===============================

Il est possible d'ajouter des fonctions aux paramètres de nos méthodes, pour
expliciter comment ils sont validés et transcris en type python, on parle de
type annotation. ``argument:type``. L'avantage de l'utilisation d'une telle
spécification est de clairement indiquer au niveau de la documentation le type
de données attendues.

.. code-block:: python3

    """Test des types annotations"""
    import hug

    @hug.get()
    def annota(text:int):
        return text

Le code ci-dessus montre l'utilisation des annotations. l'argument de la
fonction ``annota(...)`` est suivi du type int soit text::int. On comprend
aisément que l'argument text est de type int. Vérifions la sortie suivant
l'adresse <http://localhost:8000>

.. code-block:: json

    {
        "404": "The API call you tried to make was not defined. Here's a definition of the API to help you get going :)",
        "documentation": {
            "overview": "Test des types annotations",
            "handlers": {
                "/annota": {
                    "GET": {
                        "outputs": {
                            "format": "JSON (Javascript Serialized Object Notation)",
                            "content_type": "application/json"
                        },
                        "inputs": {
                            "text": {
                                "type": "int(x=0) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or         return 0 if no arguments\nare given   If x is a number, return x __int__()   For floating point\nnumbers, this truncates towards zero \n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base   The literal can be preceded by '+' or '-' and be surrounded\nby whitespace   The base defaults to 10   Valid bases are 0 and 2-36 \nBase 0 means to interpret the base from the string as an integer literal \n>>> int('0b100', base=0)\n4"
                            }
                        }
                    }
                }
            }
        }
    }

On voit bien dans le bloc inputs la clé type, on peut clairement voir que
l'entrée est de type int.

Si on entre l'adresse <http://localhost:8000/annota?text=salut> on a en retour
une belle erreur comme celle ci-dessous:

.. code-block:: json

    {
        "errors": {
            "text": "invalid literal for int() with base 10: 'salut'"
        }
    }

Il est important de noter que les annotations permettent implicitement de faire
la validation automatique des données.


Les directives
==============

Les directives sont globalement des arguments enregistrés pour fournir
automatiquement des valeurs. Un exemple serait meilleur pour expliquer le rôle
des directives. hug possède des directives prédéfinies, mais il donne la
possibilité de créer des directives personnalisées.

.. code-block:: python3

    import hug

    @hug.directive()
    def salutation_general(greeting='hi', **kwargs):
        return greeting + ' there!'
    @hug.get()
    def salut_anglais(greeting: salutation_general='hello'):
        return greeting
    @hug.get()
    def salut_americain(greeting: salutation_general):
        return greeting


Ci-dessus, on a créé une directive basée sur la fonction
``salutation_general(..)``. Cette fonction possède un paramètre avec une valeur
par défaut. Si on va à l'adresse http://localhost:8000/salut_anglais on aura en
retour ``hello there``, http://localhost:8000/salut_anglais retournera ``hi
there``. En effet, dans la fonction ``salut_anglais(..)``, on passe la
directive avec une nouvelle valeur par défaut qui est ``hello``. Cela a pour
effet d'écraser la valeur par défaut ``hi``. Par contre la fonction
``salut_americain(..)`` prend en argument la même directive, mais aucune valeur
n'est redéfinie, cela va conserver la valeur par défaut ``hi``.

Utilisation des directives
==========================

Pour utiliser les directives dans nos fonctions, il existe deux méthodes. La
première apparaît clairement, il s'agit de l'utilisation des types annotation
``greeting::directive``. On peut aussi utiliser le préfixe ``hug_`` ce qui
d'après notre exemple précédent deviendra avec la fonction
``salut_americain(...)`` :

.. code-block:: python3

    @hug.get()
    def salut_americain(hug_salutation_general='Yoo man'):
        pass


Il est aussi possible d'ajouter une valeur ``hug_salutation_general='Yoo man'``.

.. note:: il est important d'ajouter ``**kwargs``.

Format de sortie
================

hug_ utilise le JSON comme format par défaut. Heureusement, il offre
la possibilité de définir des formats autres que JSON. Il existe différentes
façons de spécifier le format que l'on veut utiliser

.. code-block:: python3

    hug.API(__name__).output_format = hug.output_format.html

    # Ou

    @hug.default_output_format()
    def my_output_formatter(data, request, response):
        """Format personnalisé."""

    # Ou encore

    @hug.get(output=hug.output_format.html)
    def my_endpoint():
        """Retourne du HTML."""


Il est possible de créer des formats de sortie personnalisés. Cela se passe
comme le montre le code ci-dessous

.. code-block:: python3

    @hug.format.content_type('file/text')
    def format_as_text(data, request=None, response=None):
        return str(content).encode('utf-8')


.. warning::

    le ``Content-Type`` nommé ``file/text`` n'existe pas. Ce n'est pas donc pas
    un exemple utilisable en l'état.

    .. Yoan

Le Routing
----------

C'est la notion qu'on retrouve dans la plupart des frameworks. Il s'agit de
définir des chemins, urls d'accès aux données. `La documentation officielle
<http://www.hug.rest/website/learn/routing>`_ détaille la notion de *Routing*
de façon plus élaborée et plus large.

.. oui, car vous n'en parlez pas.

Les APIs écrit avec ``hug`` peuvent être accédées depuis la ligne de commande, pour
cela, il suffit de rajouter ``@hug.cli()`` comme nous l'avons fait avec
``@hug.get()``.

.. quel rapport avec le routing?

Conclusion
==========

La bibliothèque hug_ offre un moyen très simplifié d'écrire des API REST.
La syntaxe est assez claire, la documentation bien élaborée depuis le code, le
*versioning* est réalisé en une seule ligne de code.


Bibliographie
-------------

- Site de ``hug``: http://www.hug.rest/
- *Réaliser une API avec Python 3*, par Rémi Alvergnat, http://toilal.github.io/talk-python3-hug/

.. [#co] <charles.ombangndo@he-arc.ch>

.. liens externes.

.. _hug: http://www.hug.rest/
.. _Flask: http://flask.pocoo.org/
.. _Django: https://www.djangoproject.com/
