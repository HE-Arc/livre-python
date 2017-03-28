.. _unittest-tutorial:

==========================
``unittest`` / ``doctest``
==========================

Introduction
============

Les tests unitaires permettent d'assurer le fonctionnement correct d'une unité de programme (fonctions, méthodes, classes, etc...). Un test unitaire vérifie, en fonction des entrées fournies à l'unité du module, que la sortie corresponde aux spécifications de l'unité.


Python possède plusieurs modules de test unitaire dont :py:mod:`unittest` et :py:mod:`doctest` que nous allons décrire par la suite.

Unittest
========

Le framework :py:mod:`unittest` a été à l'origine inspiré par JUnit_ et le fonctionnement est similaire aux frameworks de tests unitaires dans d'autres langages de programmation.

Pour réaliser des tests unitaires, unittest s'appuie sur quatres concepts importants:

- *test fixture* : un 'test fixture' représente la préparation nécessaire pour réaliser un test. Tout comme par exemple la création temporaire de base de données, dossiers ou même le démarrage de services.
- *test case* : consiste à tester une fonctionnalité précise, et ainsi tester que la sortie corresponde bien à un résultat attendu.
- *test suite* : un est regroupement de 'test case', de 'test suite, voir les deux. Utilisé lorsque plusieurs tests doivent être éxécutés ensemble.
- *test runner* : un 'test runner' gère l'exécution des tests et fournit la sortie à l'utilisateur sous forme graphique ou textuelle.

Ce chapitre présentera ainsi l'utilisation de ce module et se basant sur ces concepts.


Création d'un test unitaire
---------------------------

Voici les étapes nécessaires pour créer un test unitaire:

1.  Importer le module 'unittest'

    .. code-block:: python

        import unittest

2.  Définir la fonction à tester ou l'importer depuis un module. Ici on prend l'exemple avec la fonction carre(x):

    .. literalinclude:: examples/carre.py
       :start-after: func:carré
       :end-before: endfunc:carré

3.  Créer une classe en héritant de :py:class:`unittest.TestCase`, puis écrire les tests sous forme de méthodes. Les noms des méthodes doivent impérativement commencer par 'test' afin d'indiquer au 'test runner' quelles sont les méthodes de tests.

    De plus, chaque test doit appeller une fonction assertion de la classe TestCase. La classe TestCase possède plusieurs types de 'assert'. Ici nous utiliseront 'assertEquals()' qui permet de comparer deux valeurs (valeur retournée par la fonction et la valeur attendue).

    .. literalinclude:: examples/carre.py
       :start-after: class:TestCase
       :end-before: endclass:TestCase

4.  Exécuter les tests :

    - en appelant la fonction :py:func:`unittest.main`

    .. literalinclude:: examples/carre.py
        :start-after: main
        :end-before: endmain

    - via la ligne de commande. La ligne de commande permet aussi de spécifier les modules, classes ou même des méthodes individuelles à tester.

    .. code-block:: console

        $ python -m unittest test_module
        $ python -m unittest test_module.TestClass
        $ python -m unittest test_module.TestClass.test_methode

    Il est aussi possible de laisser 'Unittest' rechercher tous les tests grâce à l'option 'discover'. Ainsi tout les modules qui contiennent des tests depuis le répertoire courant seront exécutés, de même que pour tous les sous-répertoires.

    .. code-block:: console

        $ python -m unittest discover

5.  Analyser la sortie du test:

    .. code-block:: console

          ------------------------------------------------------------
          Ran 1 test in 0.001s

          OK

    Il y a trois possibilités de sortie:

   - OK : Le test est passé sans erreurs
   - FAIL : Le test n'est pas passé et a levé une exception (AssertionError).
   - ERROR : Le test n'est pas passé et a levé une exception autre que "AssertionError"

.. note::

    Les tests sont exécutés par ordre alphabétique et non par ordre dans lequel ils sont écrits dans le fichier.


Classes et méthodes
-------------------

Ce chapitre présentera les classes et méthodes définies dans le module unittest. Ici seront présentées les deux classes les plus utilisées.

TestCase Classe
////////////////

Une classe qui hérite de :py:class:`~unittest.TestCase` doit contenir toutes les méthodes nécessaires permettant de tester une seule et unique fonctionnalité.

Voici quelques méthodes utiles définies dans TestCase:

- ``setUp()`` : Méthode appelée avant d'effectuer chaque méthode de test. Si cette méthode lève une exception, la méthode de test n'est pas éxécutée.
- ``tearDown()`` : Méthode appelée après chaque méthode de test. Cette méthode est appellée même si la méthode de test lève une exception.
- ``setUpClass()`` : Méthode appelée en premier lieu une fois avant l'exécution des tests de la classe.
- ``tearDownClass()`` : Méthode appelée une fois l'exécution des tests de la classe terminée.
- ``run(result = None)``: Méthode qui récolte le résultat dans l'object result passé en paramètre.
- ``debug()`` : Exécute le test sans récolter le résultat.

Cette classe possède aussi beaucoup de méthodes "assert" qui testent une condition particulière. Voici quelques 'Asserts' souvent utiles:

+--------------------------+-------------------------------+
|           Type           |          vérifie que          |
+==========================+===============================+
| assertEqual(a, b)        | a == b                        |
+--------------------------+-------------------------------+
| assertNotequal(a, b)     | a != b                        |
+--------------------------+-------------------------------+
| assertTrue(x)            | bool(x) vaut 'True'           |
+--------------------------+-------------------------------+
| assertFalse(x)           | bool(x) vaut 'False'          |
+--------------------------+-------------------------------+
| assertIs(a, b)           | a est b                       |
+--------------------------+-------------------------------+
| assertIsNot(a, b)        | a n'est pas b                 |
+--------------------------+-------------------------------+
| assertIsNone(x)          | x est 'None'                  |
+--------------------------+-------------------------------+
| assertIsNotNone(x)       | x n'est pas 'None'            |
+--------------------------+-------------------------------+
| assertIn(a, b)           | a est dans b                  |
+--------------------------+-------------------------------+
| assertNotIn(a, b)        | a n'est pas dans b            |
+--------------------------+-------------------------------+
| assertIsInstance(a,b)    | a est une instance de b       |
+--------------------------+-------------------------------+
| assertNotIsInstance(a,b) | a n'est pas une instance de b |
+--------------------------+-------------------------------+

De plus, chaque méthode 'assert' peut accepter un message comme dernier argument. Si ce message est spécifié, alors il viendra affiché lors d'un échec de test.

Voici un exemple de test qui échoue:

.. literalinclude:: examples/carre.py
        :start-after: class:CarreTestCaseFail
        :end-before: endclass:CarreTestCaseFail

ainsi que la sortie lorsque le test est exécuté :

.. code-block:: console

    .F
    ======================================================================
    FAIL: test_assert_fail (carre.CarreTestCaseFail)
    Affichage d'un message d'erreur spécifique.
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "FilePath\carre.py", line 36, in test_assert_fail
        self.assertEqual(2, carré(value), "Message d'erreur personnalisé")
    AssertionError: 2 != 4 : Message d'erreur personnalisé

    ----------------------------------------------------------------------
    Ran 1 tests in 0.010s

    FAILED (failures=1)

On constate bien que le message d'erreur spécifié au moment de l'assert, est affiché lors de l'échec du test.

TestSuite Class
///////////////

Chaque instance de ``TestCase`` peut être regroupée selon la fonctionnalité du programme qu'elle teste. Ce mécanisme est mis à disposition grâce à la classe :py:class:`unittest.TestSuite`.

Voici les étapes pour regrouper un 'TestSuite':

1. Créer une instance de 'TestSuite':

.. code-block:: python

    suite = unittest.TestSuite()

2. Ajouter le 'testCase' avec la méthode addTest(). Voici l'exemple avec   'class CarreTestCase(unittest.TestCase)':

.. code-block:: python

    suite.addTest(CarreTestCase())

3. Créer une instance de la class TestTestRunner:

.. code-block:: python

    runner = unittest.TextTestRunner()

4. Appeller la méthode :py:meth:`unittest.TextTestRunner.run` pour exécuter tous les tests:

.. code-block:: python

    runner.run(suite)

Doctest
=======

Un autre standard pour les tests unitaires en Python est: :py:mod:`doctest`. Ce concept de test passe par l'utilisation des docstrings tout comme l'écriture de documentation. L'idée des doctest est de mettre ses tests dans sa documentation afin de s'assurer que les exemples dans la documentation fonctionnent.

.. glossary::

Docstring:
    Les docstrings sont des chaînes de documentation qui doivent être placées en dessous des définitions de méthodes, fonctions, classe ou au début d'un module. De plus l'indentation d'une docstring est importante car elle dépend directement de l'indentation de la classe ou de la méthode qu'elle documente.



Création d'un test unitaire
---------------------------

Pour pouvoir créer des tests à l'intérieur d'une docstring il est nécessaire de respecter une syntaxe précise. On utilise un triple chevron >>> pour indiquer que l'on écrit un test, puis à la ligne suivante on écrit le résultat attendu.

Voici un exemple avec la fonction carré:

.. literalinclude:: examples/doctest_example.py
        :start-after: func:carré
        :end-before: endfunc:carrée

Ensuite pour exécuter le(s) test(s), il faut importer le module doctest (ici fait dans le 'main'). Ensuite il faut appeller la méthode testmod() du module doctest qui va parser le fichier entier à la recherche de docstrings. Une fois la recherche effectuée, il exécute tous les tests qu'il a trouvé.

.. literalinclude:: examples/doctest_example.py
        :start-after: main
        :end-before: endmain

Cependant si on éxécute le fichier en ligne de commande:

.. code-block:: console

    $ python doctest_example.py

On constate qu'aucune sortie est affichée si aucun test échoue. Cependant si on voulait avoir un retour des tests, il faudrait utiliser l'option -v (verbose):

.. code-block:: console

    $ python doctest_example.py -v

Ce qui produirait le résultat suivant:

.. code-block:: console

    Trying:
        carré(-2)
    Expecting:
        4
    ok
    Trying:
        carré(0)
    Expecting:
        0
    ok
    Trying:
        carré(2)
    Expecting:
        4
    ok
    1 items had no tests:
        __main__
    1 items passed all tests:
       3 tests in __main__.carré
    3 tests in 2 items.
    3 passed and 0 failed.
    Test passed.

Conclusion
==========

L'écriture des tests est une pratique primordiale afin d'apporter un gain en qualité du logiciel et en maintenance.
De plus l'écriture des tests n'est pas difficile en soi, ni même longue comme vous avez pu le constater dans ce tutoriel. Afin d'écrire efficacement des tests unitaires, il faut de la pratique, cependant mieux vaut des tests "peu efficaces" que de ne pas en écrire. Pour terminer, s'il y a bien une chose à retenir de ce tutoriel c'est qu'il n'y a pas de désavantages à en écrire, c'est pour cela que je vous invite à vous y mettre dès demain!



.. _Junit: http://junit.org/junit4/
