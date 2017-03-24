.. _io-tutorial:

io
==

Par Dylan Santos de Pinho [#yb]_

Introduction
------------

:py:mod:`io` est un module qui permet de gérer des flux d'entrées et de sorties,
que ce soit pour écrire avec des données en byte(string) ou avec des
données en binaire. :py:mod:`io` est le module par défaut pour gérer les flux et les fichiers en
python 3.\*.

Ouverture de fichier
--------------------

On utilise ``open`` pour ouvrir un fichier. Il retourne le flux
correspondant si le fichier s'ouvre, sinon une exception ``OSError``
(anciennement ``IOError`` qui devient un alias de ``OSError``) est levée.


.. code-block:: python3

    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)


file : String, contenant le chemin absolu ou relatif pour accéder au fichier, ou un Integer, descripteur  de fichier (clé abstraite pour accéder à un fichier).

mode : Spécifie comment ouvrir le fichier, voir tous les modes possibles
dans le tableau ci-dessous:

+---------+----------------------------------------------------------------------------------------------+
| Modes   | Signification                                                                                |
+=========+==============================================================================================+
| ``r``   | Ouvre le fichier en lecture (par défaut).                                                    |
+---------+----------------------------------------------------------------------------------------------+
| ``w``   | Ouvre le fichier en écriture en effaçant le fichier s'il existe sinon le crée.               |
+---------+----------------------------------------------------------------------------------------------+
| ``x``   | Ouvre le fichier en création, échoue si le fichier existait déjà.                            |
+---------+----------------------------------------------------------------------------------------------+
| ``a``   | Ouvre le fichier en écriture et écrit à la fin du fichier si existant.                       |
+---------+----------------------------------------------------------------------------------------------+
| ``b``   | Mode binaire.                                                                                |
+---------+----------------------------------------------------------------------------------------------+
| ``t``   | Mode texte (par défaut).                                                                     |
+---------+----------------------------------------------------------------------------------------------+
| ``+``   | Ouvre le fichier en lecture et écriture.                                                     |
+---------+----------------------------------------------------------------------------------------------+
| ``U``   | Mode Universal newlines (pour la rétrocompatibilité, ne pas utiliser dans le nouveau code).  |
+---------+----------------------------------------------------------------------------------------------+


Les modes sont cumulables, par défaut le mode est 'rt'(lecture de
texte).

buffering: Permet de changer le fonctionnement du buffer:

    -  défaut:
        -  Pour les fichiers binaires, la taille du buffer est fixe en dépendant
           de ``DEFAULT\_BUFFER\_SIZE``.
        -  Pour les fichiers qui retourne True avec isatty()(si c'est connecté à
           un terminal), ils ont un buffer de ligne. Sinon comme ci-dessus avec
           les fichiers binaires.
    -  ``0``: Permet de désactiver le buffer, seulement en mode binaire.
    -  ``1``: Mets une ligne dans le buffer, seulement en mode texte.
    -  >1: Spécifie la taille du buffer.


encoding: Nom de l'encodage permettant de décoder le fichier(devrait
être utilisé qu'en mode texte). Par défaut utilise le décodage du
système, voir ce que retourne ``locale.getpreferredencoding()``.
Préciser l'encodage est une bonne pratique.

errors: Permet de spécifier comment traiter les erreurs (seulement en
mode texte):

    -  strict(None, par défaut): Lève une exception ValueError
    -  ignore: Ignore l'erreur(risque de perte de données).
    -  replace: Remplace les erreurs par des '?'.

newline: Spécifie comment les sauts de ligne fonctionnent. Valeurs
possible: None, '', '\\n', '\\r' ou '\\r\\n'.

closefd: Doit être à True(par défaut) si un nom de fichier a été donné.
Si il est à False et qu'un descripteur de fichier a été donné, le descripteur de fichier
restera ouvert quand le fichier sera fermé.

opener: On peut spécifier un opener à utiliser.

Méthode de io.IOBase
--------------------

Quelques méthodes parmi les plus utiles de :py:mod:`io` :

    -  ``read(n)``: Lis le fichier jusqu'à avoir n bit(mode binaire) ou n
       bytes(mode texte). Si n est négatif ou n'est pas spécifié, lis jusqu'à la fin
       du fichier.
    -  ``write(b)``: Ecrit b dans le fichier.
    -  ``close()``: Flush et ferme le flux. N'a aucun effet si le fichier est
       déjà fermé, seulement le premier appel à effet.
    -  ``closed``: Retourne True si le fichier est fermé.
    -  ``flush()``: Vide le flux d'écriture, ne fait rien en lecture.
    -  ``isatty()``: Retourne True si le flux est connecté à un terminal.
    -  ``readable()``: Retourne True si on peut lire depuis le flux. Si False,
       ``read()`` lève une exception ``OSError``.
    -  ``writable()``: Retourne True si on peut écrire depuis le flux. Si False,
       ``write()`` lève une exception ``OSError``.

Exemple
~~~~~~~

Exemple d'un programme utilisant les flux d'entrée et de sortie, en copiant les 10
premiers caractères d'un fichier dans un autre fichier:

.. literalinclude:: ./examples/stream.py
   :linenos:

io.StringIO
-----------

.. code-block:: python

    io.StringIO(initial_value='', newline='\n')

Permet d'ouvrir un flux textuel en mémoire. Le buffer est vidé lorsqu'on close() le flux.
io.StringIO hérite de io.BaseIO. Lorsque qu'on appelle open(mode='t'), python crée, de façon caché, un io.StringIO.

initial_bytes: Permets d'avoir des données à la création.

newline: Spécifie comment les sauts de ligne fonctionnent. Valeurs
possible: None, '', '\\n'(par défaut), '\\r' ou '\\r\\n'.

Exemple
~~~~~~~

Exemple d'un programme qui affiche deux lignes dans une console:

.. literalinclude:: ./examples/StringIO.py
   :linenos:


io.BytesIO
----------

.. code-block:: python3

    io.BytesIO([initial_bytes])


Permet d'ouvrir un flux binaire en mémoire avec buffer. Le buffer est vidé lorsqu'on close() le flux.
io.BytesIO hérite de io.BaseIO. Lorsque qu'on appelle open(mode='b'), python crée, de façon caché, un io.BytesIO.

initial_bytes: Permets d'avoir des données binaires à la création.

Exemple
~~~~~~~

Exemple d'un programme qui change des caractères se trouvant au milieu d'un BytesIO par d'autres caractères:

.. code-block:: pycon

    >>> b = io.BytesIO(b"abcdef")
    >>> view = b.getbuffer()
    >>> view[2:4] = b"56"
    >>> b.getvalue()
    b'ab56ef'


Conclusion
----------

:py:mod:`io` est un module simple à utiliser pour s'occuper des flux et pour
modifier les fichiers. Ce document ne cite que les méthodes les plus courantes, il ne faut
pas hésiter à aller voir la documentation officielle de :py:mod:`io`.

.. [#yb] <dylan.santosdepinho@he-arc.ch>

.. Bibliographie
.. https://docs.python.org/3/library/io.html
