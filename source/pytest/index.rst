.. _pytest-tutorial:

======
Pytest
======

.. image:: pytest.png
   :height: 300px
   :width: 486 px
   :scale: 50 %
   :alt: alternate text
   :align: center

Introduction
============

Pytest est un framework permettant de faire des tests et de vérifier si les différentes conditions sont juste ou fausse.
Il permet de tester les éléments un à un mais on peut aussi lui demander de faire une série de test.
Ces méthodes de test dépendent de comment l'on implémente dans notre code.
Dans ce document, je vais traiter plusieurs systèmes de test.

Exemple de base
===============

Vérification de la valeur d'une fonction
----------------------------------------

Cette méthode vérifie la valeur d'une fonction est égale à celle avec qui on test.

Code
~~~~

.. code-block:: pycon

	def func(x):
		return x + 1
	def test_answer():
		assert func(3) == 5

Fixture
=======

Le but des fixtures est de fournir une base pour les tests afin qu'ils puissent être exécuté de manière fiable et répétitives. Les fixtures ont des nom explicit et sont activable en les déclarants dans les fonctions de tests, les modules,...
Les fixtures sont implémenter de façon modulaire. Chaque fonction des fixtures peuvent être appelé depuis un autre.

Avec argument
-------------

Les fonctions de test peuvent recevoir des objets en les nommant comme argument d'entrée. Pour chaque argument de ce type, la fonction doit être enregistrer avec le @pytest.fixure, comme dans l'exemple ci-dessous.

Code
~~~~

.. code-block:: pycon

	# content of ./test_smtpsimple.py
	import pytest

	@pytest.fixture
	def smtp():
    	import smtplib
    	return smtplib.SMTP("smtp.gmail.com")

			def test_ehlo(smtp):
    	response, msg = smtp.ehlo()
    	assert response == 250
    	assert 0 # for demo purposes

Modulaire
---------

On peut aussi utiliser un fixture dans un autre fixture. Dans notre exemple, nous allons instancier un objet "app" dans lequel nous allons y ajouter la ressource "smtp" (la ressource est déjà définie).

Code
~~~~

.. code-block:: pycon

	import pytest

	class App:
  	def __init__(self, smtp):
    	self.smtp = smtp

	@pytest.fixture(scope="module")
	def app(smtp):
    return App(smtp)

	def test_smtp_exists(app):
    assert app.smtp

Exception
=========

Afin de gérer les exceptions, il faut utiliser "pytest.raises".
En utilisant pytest.raises, on peut délibérément tester nos exceptions.
Un autre system (pytest.mark.xfail), permet de tester aussi les exceptions.
Il est surtout utilisé pour trouver des bugs dans des dépendances.

Simple exception
----------------

Dans l'exemple si dessous, on va "définir" la division par 0.

Code
~~~~

.. code-block:: pycon

	import pytest
	def test_zero_division():
	with pytest.raises(ZeroDivisionError):
	1 / 0

Test expression régulière
-------------------------

Si on veut tester la correspondance d'une expression régulière qui représente un exception, on peut utiliser "ExceptionInfo.match".

Exemple
~~~~~~~

Dans l'exemple ci-dessous, on va regarder l'exception qui contient le 123.
Cela peut être utiliser dans une longue liste, et on en recherche qu'une seule.

.. code-block:: pycon

	import pytest
	def myfunc():
		raise ValueError("Exception 123 raised")
	def test_match():
		with pytest.raises(ValueError) as excinfo:
			myfunc()
		excinfo.match(r'.* 123 .*')

Temporary directories and files
===============================

Dans cette partie, nous allons voir l'utilisation des fichiers et des dossiers temporaires.

tmpdir
------

tmpdir permet de créer un répertoire temporaire unique. tmpdir est un objet de py.path.local.

Exemple
~~~~~~~

.. code-block:: pycon

	# content of test_tmpdir.py
	import os
	def test_create_file(tmpdir):
		p = tmpdir.mkdir("sub").join("hello.txt")
		p.write("content")
		assert p.read() == "content"
		assert len(tmpdir.listdir()) == 1
		assert 0

tmpdir_factory
--------------

Cette fonction permet de créer un autre répertoire pour n'importe quel autre fixture ou test.

Exemple
~~~~~~~

Dans cet exemple, on va imaginer que notre test demande une grande part du disque.
On va générer cette partie procéduralement. On va donc calculer et attribué l'espace à chaque session du test.

Code
~~~~

.. code-block:: pycon

	# contents of conftest.py
	import pytest
		@pytest.fixture(scope='session')
		def image_file(tmpdir_factory):
		img = compute_expensive_image()
		fn = tmpdir_factory.mktemp('data').join('img.png')
		img.save(str(fn))
		return fn
	# contents of test_image.py
	def test_histogram(image_file):
		img = load_image(image_file)
		# compute and test histogram

Explication
~~~~~~~~~~~

TempdirFactory.mktemp : Cela créer le sous-dossier à la base du dossier temporaire et le renvoie.

TempdirFactory.getbasetemp() : return la base du dossier temporaire.

The default base temporary directory
------------------------------------

Les répertoires temporaires sont créés par défaut comme sous-répertoire dans le répertoire temporaire du système.
Le nom de base sera "pytest-NUM". Le NUM est un nombre qui est incrémenter à chaque exécution.
De plus, les entrées plus vielles de 3 dossiers temporaires sont supprimées.

Modifier le dossier temporaire
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: pycon

	pytest --basetemp=mydir


Capture
=======

Pour réaliser une capture, il faut utiliser les fixtures capsys et capfd.
Ces deux fixtures permettent l'accès aux entrées-sorties durant la phase de test.

Simple exemple
--------------

.. code-block:: pycon

	def test_myoutput(capsys): # or use "capfd" for fd-level
		print ("hello")
		sys.stderr.write("world\n")
		out, err = capsys.readouterr()
		assert out == "hello\n"
		assert err == "world\n"
		print ("next")
		out, err = capsys.readouterr()
		assert out == "next\n"

readouterr()
~~~~~~~~~~~~

Cela permet de lancer le système de capture des outputs. Une fois le test des fonctions finis, les flux seront restaurés à leur état d'origine.

capsys
~~~~~~

Capsys est un moyen de réalisé les tests sans se soucier des paramètres et des réinitialisations des outputs.

capfd
~~~~~

Capfd est utilisé au niveau du descripteur de fichier. Cela nous permet de faire des captures des outputs des librairies ou des sous-processus.

Désactiver la capture
---------------------

On peut choisir de désactiver la capture afin de ne pas enregistrer certaines informations.

Exemple
~~~~~~~

Dans le morceau de code ci-dessous, l'avant-dernière ligne ne sera pas enregistrée, car elle fait partie du block du while.

.. code-block:: pycon

	def test_disabling_capturing(capsys):
		print('this output is captured')
		with capsys.disabled():
			print('output not captured, going directly to sys.stdout')
		print('this output is also captured')

Conclusion
==========

Pytest est un outil très puissant quand il s'agit de faire différents tests. De plus, il dispose d'un large panel de compléments, ce qui lui permet un plus grande maniabilité et adaptation en fonction de nos besoins.
