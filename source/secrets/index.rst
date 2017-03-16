.. _secrets-tutorial:

``secrets``
===========

Par Maël Pedretti [#mp]_

Introduction
------------
:py:mod:`secrets` est un module python utilisé pour générer des nombres aléatoirs cryptographiquement forts. Ceux-ci sont utilisables pour gérer des données telles que des mots de passe, des authentifications, des jetons de sécurité et autres secrets associés.

:py:mod:`secrets` devrait en particulier être utilisé de préférence au générateur de nombres pseudo-aléatoires par défaut dans le module :py:mod:`random`, qui est conçu pour la modélisation et la simulation et non pas la sécurité ou la cryptographie.

.. [#mp] <mael.pedretti@he-arc.ch>