.. _secrets-tutorial:

``secrets``
===========

.. image:: ./lock.png
	:scale: 30%
   	:align: right
   	:alt: lock logo

Par Maël Pedretti [#mp]_

Introduction
------------
:py:mod:`secrets` est un module python utilisé pour générer des nombres aléatoirs cryptographiquement forts. Ceux-ci sont utilisables pour gérer des données telles que des mots de passe, des authentifications, des jetons de sécurité et autres secrets associés. Ce module n'est disponible que depuis la version 3.6 de python (:pep:`506`).

:py:mod:`secrets` devrait en particulier être utilisé de préférence au générateur de nombres pseudo-aléatoires par défaut dans le module :py:mod:`random`, qui est conçu pour la modélisation et la simulation et non pas la sécurité ou la cryptographie.

Utilisations
------------

Nombres aléatoires
******************
Ce module donne accès à la source d'aléatoire la plus sécurisée que votre système d'exploitation fournit.

- Classe :py:class:`secrets.SystemRandom` permet de générer des nombres aléatoires, voir :py:class:`random.SystemRandom` pour plus de détails
- :py:func:`secrets.choice(sequence) <secrets.choice()>` retourne un élément aléatoire à partir de *sequence*
- :py:func:`secrets.randbelow(i) <secrets.randbelow()>` retourne un nombre entier aléatoire entre zéro et *i*
- :py:func:`secrets.randbits(j) <secrets.randbits()>` retourne un nombre entier aléatoire composé de *j* bits

Jetons
******
Ce module fournit également des fonctions pour générer des jetons sécurisés, adaptés à des applications telles que des réinitialisations de mots de passe via des URL_ difficiles à deviner, des authentifications via API_ tierces, et d'autres utilisations similaires.

- :py:func:`secrets.token_bytes(k) <secrets.token_bytes()>` retourne une chaine binaire composé de *k* bytes. 
- :py:func:`secrets.token_hex(l) <secrets.token_hex()>` retourne une chaine de texte hexadécimale composée de *l* bytes convertis chacun en deux digits hexadécimaux.
- :py:func:`secrets.token_urlsafe(m) <secrets.token_urlsafe()>` retourne une chaine de texte de *m* bytes utilisable dans une URL_. Le texte est encodé en base64_ donc chaque byte est représenté par environ 1.3 charactère.

Si *k*, *l* ou *m* ne sont pas renseignés, un nombre raisonnable sera utilisé par défaut.

Pour résister à une attaque de `force brute`_, les jetons doivent être suffisament longs pour être suffisament aléatoires. Cependant, cette notion de suffisance reste assez vague. Plus les ordinateurs deviennent puissants, plus les jetons devront être longs afin de ralonger le temps nécessaire à une machine pour le découvrir.
D'après la documentation python, des jetons de 32 bytes sont suffisament sécurisés.

Autre
*****

- :py:func:`secrets.compare_digest(a,b) <secrets.compare_digest()>` permet de comparer deux chaînes de texte.

Exemples
--------
Génération d'un mot de passe aléatoire de 10 charactères contenant au minimum une lettre majuscule, une lettre minuscule et un chiffre

.. code-block:: pycon
	
	>>> from secrets import choice

	>>> import string

	>>> alphabet = string.ascii_letters + string.digits

	>>> while True:
    		password = ''.join(choice(alphabet) for i in range(10))
    		if (any(c.islower() for c in password)
            	and any(c.isupper() for c in password)
            	and sum(c.isdigit() for c in password) >= 3):
        	break

	>>> print(password)
	cQjUuu02e5

Génération d'un jeton hexadécimal d'une longueur de 16 bytes.

.. code-block:: pycon

	>>> secrets.token_hex(16)
	7e5e31e55f5a878980bb230b7e5c7fbe

Génération d'un jeton d'une longueur de 16 bytes pouvant être utilisé dans une URL

.. code-block:: pycon

	>>> secrets.token_urlsafe(16)
	k84RkJMyMpX6e3qzVXRqcw


Conclusion
----------

Le module :py:mod:`secrets` est un module destiné aux utilisateurs avancés ayant des besoins de sécurité supérieurs à la normale.
Il offre différents outils permettant la création de différents mots de passe et jetons sécurisés.


Source de l'image : https://pixabay.com/p-1968247/?no_redirect

.. [#mp] <mael.pedretti@he-arc.ch>
.. _URL: https://fr.wikipedia.org/wiki/Uniform_Resource_Locator
.. _base64: https://fr.wikipedia.org/wiki/Base64
.. _force brute: https://fr.wikipedia.org/wiki/Attaque_par_force_brute
.. _API: https://fr.wikipedia.org/wiki/Interface_de_programmation