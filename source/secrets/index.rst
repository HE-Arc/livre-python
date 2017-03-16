.. _secrets-tutorial:

``secrets``
===========

Par Maël Pedretti [#mp]_

Introduction
------------
:py:mod:`secrets` est un module python utilisé pour générer des nombres aléatoirs cryptographiquement forts. Ceux-ci sont utilisables pour gérer des données telles que des mots de passe, des authentifications, des jetons de sécurité et autres secrets associés.

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
Ce module fournit également des fonctions pour générer des jetons sécurisés, adaptés à des applications telles que des réinitialisations de mots de passe, des URL difficiles à deviner et similaires.

- :py:func:`secrets.token_bytes(k) <secrets.token_bytes()>` retourne une chaine binaire composé de k bytes. 
- :py:func:`secrets.token_hex(l) <secrets.token_hex()>` retourne une chaine de texte héxadécimale composée de l bytes.
- :py:func:`secrets.token_urlsafe(m) <secrets.token_urlsafe()>` retourne une chaine de texte de m bytes utilisable dans une URL_.

Si k,l ou m ne sont pas renseignés, un nombre raisonnable sera utilisé par défaut.

Autre
*****

- :py:func:`secrets.compare_digest(a,b) <secrets.compare_digest()>` permet de comparer deux chaînes de texte.

Exemples
--------

.. [#mp] <mael.pedretti@he-arc.ch>
.. _URL: https://fr.wikipedia.org/wiki/Uniform_Resource_Locator