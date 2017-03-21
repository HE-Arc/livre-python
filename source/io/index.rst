-.. _io-tutorial:

io
==

Par Dylan Santos de Pinho [#yb]_

Introduction
------------

io_ est un module qui permet de gérer des flux d’entrées et de sorties,
que ce soit pour écrire avec des données en byte(string) ou avec des
données en binaire. io était un module alternatif à file en python 2.\*
mais est le module par défaut pour gérer les flux et les fichiers en
python 3.\*.

Ouverture de fichier
--------------------

On utilise io.open pour ouvrir un fichier. Il retourne le flux
correspondant si le fichier s’ouvre, sinon une exception OSError
(anciennement IOError qui devient un alias de OSError) est levée.


.. code-block:: python3

    io.open(file, mode=’r’, buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)


file : String, contenant le chemin absolu ou relatif pour accéder au fichier, ou un Integer, descripteur  de fichier (clé abstraite pour accéder à un fichier).

mode : Spécifie comment ouvrir le fichier, voir tous les modes possible
dans le tableau ci-dessous.

+---------+----------------------------------------------------------------------------------------------+
| Modes   | Signification                                                                                |
+=========+==============================================================================================+
| ‘r’     | Ouvre le fichier en lecture (par défaut).                                                    |
+---------+----------------------------------------------------------------------------------------------+
| ‘w’     | Ouvre le fichier en écriture en effaçant le fichier si existant.                             |
+---------+----------------------------------------------------------------------------------------------+
| ‘x’     | Ouvre le fichier en création, echoue si le fichier existait déjà.                            |
+---------+----------------------------------------------------------------------------------------------+
| ‘a’     | Ouvre le fichier en écriture et écrit à la fin du fichier si existant.                       |
+---------+----------------------------------------------------------------------------------------------+
| ‘b’     | Mode binaire.                                                                                |
+---------+----------------------------------------------------------------------------------------------+
| ‘t’     | Mode texte (par défaut).                                                                     |
+---------+----------------------------------------------------------------------------------------------+
| ‘+’     | Ouvre le fichier en lecture et écriture.                                                     |
+---------+----------------------------------------------------------------------------------------------+
| ‘U’     | Mode Universal newlines (pour la rétrocompatibilité, ne pas utiliser dans le nouveau code).  |
+---------+----------------------------------------------------------------------------------------------+


Les modes sont cumulables, par défaut le mode est ‘rt’(lecture de
texte).

buffering permet de changer le fonctionnement du buffer:

    -  défaut:
    -  0: Permet de désactiver le buffer, seulement en mode binaire.
    -  1: Mets une ligne dans le buffer, seulement en mode texte.
    -  >1:
        -  Pour les fichiers binaires, la taille du buffer est fixe en dépendant
           de DEFAULT\_BUFFER\_SIZE.
        -  Pour les fichiers qui retourne True avec isatty()(si c’est connecté à
           un terminal), ils ont un buffer de ligne. Sinon comme ci-dessus avec
           les fichiers binaires.


encoding: Nom de l’encodage permettant de décoder le fichier(devrait
être utilisé qu’en mode texte). Par défaut utilise le décodage du
systèeme, voir ce que retourne locale.getpreferredencoding().

errors permet de spécifier comment traiter les erreurs (seulement en
mode texte):

    -  strict(None, par défaut): Lève une exception ValueError
    -  ignore: Ignore l’erreur(risque de perte de données).
    -  replace: Remplace les erreurs par des ‘?’.


newline: Spécifie comment les sauts de ligne.

newline: Spécifie comment les sauts de ligne fonctionnent. Valeurs
possible: None, ‘’, ‘\\n’, ‘\\r’ ou ‘\\r\\n’.

closefd: Doit être à true(par défaut) si un nom de fichier a été donné.
Si il est à faux et qu'un descripteur de fichier a été donné, le descripteur de fichier
restera ouvert quand le fichier sera fermé.

opener: On peut spécifier un opener à utiliser.

Méthode de io
-------------

    -  read(n): Lis le fichier jusqu’à avoir n bit(mode binaire) ou n
       bytes(mode texte). Si n est négatif ou n'est pas spécifié, lis jusqu’à la fin
       du fichier.
    -  write(b): Ecrit b dans le fichier.
    -  close(): Flush et ferme le flux. N’a aucun effet si le fichier est
       déjà fermé, seulement le premier appel à effet.
    -  closed: Retourne True si le fichier est fermé.
    -  flush(): Vide le flux d’écriture, ne fait rien en lecture.
    -  isatty(): Retourne True si le flux est connecté à un terminal.
    -  readable(): Retourne True si on peut lire depuis le flux. Si false,
       read() lève une exception OSError.
    -  writable(): Retourne True si on peut écrire depuis le flux. Si false,
       write() lève une exception OSError.

Exemple
~~~~~~~

Exemple de programme utilisant les flux d'entrée et de sortie:

.. literalinclude:: ./examples/stream.py
   :linenos:


Conclusion
----------

io_ est un module simple à utiliser pour s’occuper des flux et pour
modifier les fichiers. Il est devenu si important qu’il est passé d’un
module alternatif en python 2.\* à un module faisant parti de python
3.\*. Ce document ne cite que les méthodes les plus courante, il ne faut
pas hésiter à aller voir la documentation officiels de io_.

.. [#yb] <dylan.santosdepinho@he-arc.ch>

.. Bibliographie

.. _io:  https://docs.python.org/3.6/library/io.html
