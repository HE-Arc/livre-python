========================
unittest (doctest, mock)
========================

Introduction
============

Les tests unitaires permettent d'assurer le fonctionnement correct d'une unité de programme (fonctions, méthodes, classes, etc...). Un test unitaire vérifie, en fonction des entrées fournies à l'unité du module, que la sortie corresponde aux spécifications de l'unité. 


Python possède plusieurs modules de test unitaire dont :py:mod:`unittest` et :py:mod:`doctest` que nous allons décrire par la suite.

Unittest
========

Le framework :py:mod:`unittest` a été à l'origine inspiré par JUnit et le fonctionnement est similaire aux frameworks de tests unitaires dans d'autres langages de programmation.

Pour réaliser des tests unitaires, unittest s'appuie sur 4 concepts importants:

- test fixture : un 'test fixture' représente la préparation nécessaire pour réaliser un test. Tout comme par exemple la création temporaire de base de données, dossiers ou même le démarrage de services.
- test case : consiste à tester une fonctionnalité précise, et ainsi tester que la sortie corresponde bien à un résultat attendu.
- test suite : un est regroupement de 'test case', de 'test suite, voir les deux. Utilisé lorsque plusieurs tests doivent être éxécutés ensemble.
- test runner : un 'test runner' gère l'exécution des tests et fournit la sortie à l'utilisateur sous forme graphique ou textuelle.

Ce chapitre présentera ainsi l'utilisation de ce module et se basant sur ces concepts.


Création d'un test unitaire
---------------------------

Voici les étapes nécessaires pour créer un test unitaire:

1)  Importer le module 'unittest'

	.. code-block:: python

		import unittest
   
2)  Définir la fonction à tester ou l'importer depuis un module. Ici on prend l'exemple avec la fonction carre(x): 

	.. code-block:: python

		def carre(x):
			return x ** 2

3) Créer une classe en héritant de 'TestCase', puis écrire les tests sous forme de méthodes. Les noms des méthodes doivent impérativement commencer par 'test' afin d'indiquer au 'test runner' quelles sont les méthodes de tests. 

   De plus, chaque test doit appeller une fonction 'assert' de la classe TestCase. La classe TestCase possède plusieurs types de 'assert'. Ici nous utiliseront 'assertEquals()' qui permet de comparer deux valeurs (valeur retournée par la fonction et la valeur attendue).

   .. code-block:: python
   
	class Testeur(unittest.TestCase):
		testValues = {2: 4, 0: 0, -2: 4}

		def testCarre(self):
			for i, a in self.testValues.items():
				self.assertEqual(carre(i), a)
   
4) Éxécuter les tests soit:

   - en appelant la méthode main() du module unittest
	
   .. code-block:: python
   
		if __name__ == '__main__':
			unittest.main()
	
   - via la ligne de commande. La ligne de commande permet aussi de spécifier les modules, classes ou même des méthodes individuelles à tester.

   .. code-block:: bash
   
   	   python -m unittest test_module 
   	   python -m unittest test_module.TestClass
   	   python -m unittest test_module.TestClass.test_methode
	
   Il est aussi possible de laisser 'Unittest' rechercher tous les tests grâce à l'option 'discover'. Ainsi tout les modules qui contiennent des tests depuis le répertoire courant seront exécutés, de même que pour tous les sous-répertoires.

   .. code-block:: bash
	
	  python -m unittest discover
	
5) Analyser la sortie du test:

   .. code-block:: bash
   
   	   ----------------------------------------------------------------------
   	   Ran 1 test in 0.001s
   	   
   	   OK
       
   Il y a trois possibilités de sortie:

   - OK : Le test est passé sans erreurs
   - FAIL : Le test n'est pas passé et a levé une exception (AssertionError). 
   - ERROR : Le test n'est pas passé et a levé une exception autre que "AssertionError"
	
	
Classes & méthodes
------------------

Ce chapitre présentera les classes et méthodes définies dans le module unittest. Ici seront présentées les deux classes les plus utilisées.

TestCase Classe
////////////////

Une classe qui hérite de TestCase doit contenir toutes les méthodes nécessaires permettant de tester une seule et unique fonctionnalité.

Voici quelques méthodes utiles définies dans TestCase:

- setUp() : Méthode appelée avant d'effectuer chaque méthode de test. Si cette méthode lève une exception, la méthode de test n'est pas éxécutée.
- tearDown() : Méthode appelée après chaque méthode de test. Cette méthode est appellée même si la méthode de test lève une exception.
- setUpClass() : Méthode appelée en premier lieu une fois avant l'exécution des tests de la classe.
- tearDownClass() : Méthode appelée une fois l'exécution des tests de la classe terminée.
- run(result = None): Méthode qui récolte le résultat dans l'object result passé en paramètre.
- debug() : Exécute le test sans récolter le résultat.

Cette classe possède aussi beaucoup de méthodes "assert" qui testent une condition particulière. Voici quelques 'Asserts' souvent utiles:

+---------------------+----------------------+
|         Type        | vérifie que          |
+=====================+======================+
| assertEqual(a,b)    | a==b                 |
+---------------------+----------------------+
| assertNotequal(a,b) | a != b               |
+---------------------+----------------------+
| assertTrue(x)       | bool(x) vaut 'True'  |
+---------------------+----------------------+
| assertFalse(x)      | bool(x) vaut 'False' |
+---------------------+----------------------+

Depuis la version 3.1 de python il existe encore:

+---------------------+----------------------+
|         Type        | vérifie que          |
+=====================+======================+
| assertIs(a,b)       | a est b              |
+---------------------+----------------------+
| assertIsNot(a,b)    | a n'est pas b        |
+---------------------+----------------------+
| assertIsNone(x)     | x est 'None'         |
+---------------------+----------------------+
| assertIsNotNone(x)  | x n'est pas 'None'   |
+---------------------+----------------------+
| assertIn(a,b)       | a est dans b         |
+---------------------+----------------------+
| assertNotIn(a,b)    | a n'est pas dans b   |
+---------------------+----------------------+

et depuis la version 3.2 ils ont rajouté:

+--------------------------+-------------------------------+
|         Type             | vérifie que                   |
+==========================+===============================+
| assertIsInstance(a,b)    | a est une instance de b       |
+--------------------------+-------------------------------+
| assertNotIsInstance(a,b) | a n'est pas une instance de b |
+--------------------------+-------------------------------+


De plus, chaque méthode 'assert' peut accepter un message comme dernier argument. Si ce message est spécifié, alors il viendra affiché lors d'un échec de test.


TestSuite Class
///////////////

Chaque instance de 'testCase' peut être regroupée selon la fonctionnalité du programme qu'elle teste. Ce mécanisme est mis à disposition grâce à la classe 'TestSuite'.

voici les étapes pour regrouper un 'TestSuite':

1) Créer une instance de 'TestSuite'

.. code-block:: python

	suite = unittest.TestSuite()

2) Ajouter le 'testCase' avec la méthode addTest() ou  makeSuite():

.. code-block:: python

	suite.addTest(testcase class)
	suite = unittest.makeSuite(testcase class)

3) Créer une instance de la class TestTestRunner:

.. code-block:: python

	runner = unittest.TextTestRunner()

4) Appeller la méthode run() pour exécuter tous les tests

.. code-block:: python

	runner.run(suite)

Mock
====

#TODO

Doctest
=======

#TODO
	
	