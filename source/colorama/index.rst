.. _colorama-tutorial:

``colorama``
============

Par Killian Castella [#contact]_

Introduction
------------

Les caractères d'échappement ANSI sont depuis longtemps utilisé pour produire des terminaux colorés et déplacer le curseur d'écriture dans les terminaux Unix.
Seulement, ces caractères d'échappement ne sont pas compatibles avec le terminal natif de Windows.
La bibliothèque externe de python Colorama est la pour palier à ce problème en convertissant ces caractères en appels win32 appropriés.

Grace à Colorama il est possible d'utiliser de nombreuses bibliothèques se basant sur Les caractères d'échappement ANSI d’être utilisées sur Windows.

Pour résumer, Colorama est une bibliothèque python multiplateforme pour afficher des terminaux colorés en Python. 

Exemples
--------

Fonctionalités de base
**********************

Pour commencer avant d'utiliser colorama il faut importer les fonctionnalités désirées et initialiser colorama : 

.. code-block:: pycon

    >>> from colorama import Fore, Back, Style
    >>> init()

On peut ensuite utiliser les diverses fonctionnalités :  

- Fore : Permet de changer la couleur de l'arrière-plan.
- Back : Permet de changer la couleur de l'écriture.
- Style : Permet de changer la brillance de la police

Et la liste des attributs associés :
::

	Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
	Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
	Style: DIM, NORMAL, BRIGHT, RESET_ALL


Utilisation : 

.. literalinclude:: ./examples/style.py

Résultat  : 
 .. image:: ./images/CommandeBase.PNG
	:alt: Texte mis en forme avec couleurs

Pour arrêter colorama avant la fin du programme il suffit d'appeler deinit() : 

.. code-block:: pycon

    >>> deinit()


Avant l’arrêt, Colorama va appeler Style.RESET_ALL afin de rétablir le style initial.

Déplacement du curseur
**********************

Il est également possible d'utiliser les sequences ANSI directement dans notre code , c'est de cette manière que nous pouvons également déplacer le curseur.

.. literalinclude:: ./examples/cursor.py

\\033 correspond au code octal en style C pour le caractère ESC. Les caractères qui se trouvent après le '[' sont les séquences ANSI.

Résultat  : 
 .. image:: ./images/CursorPositioning.png
    :alt: Texte placé à divers endroit selon le code ci-dessus
    
Colorama ne convertit qu'une partie des séquences ANSI en appel win32. la liste des séquences prises en charge se trouve `ici <https://github.com/tartley/colorama#recognised-ansi-sequences>`_.

    
Utilisation d'une bibliothèque utilisant les caractères d'échappement ANSI
**************************************************************************

Certaines bibliothèques se basent sur les séquences ANSI pour colorer les terminaux et ne sont donc pas fonctionelles avec windows, Ici un exemple d'utilisation de termcolor sous windows :
 
 .. image:: ./images/termcolorWithoutColorama.png
    :alt: affichage de termcolor non interpreté
	
On voit bien que tout n'est pas interpreté comme il se doit, C'est la qu'entre en jeu Colorama qui permet d'interpreter correctement ces séquences :

.. literalinclude:: ./examples/termcolor.py

Ce qui nous donne :

 .. image:: ./images/termcolor.png
    :alt: affichage de termcolor correctement interpreté

Conclusion
------------------

Colorama est une bibliothèque très simple d'utilisation et très utile pour faire fonctionner diverses autres bibliothèques se basant sur les séquences ANSI sous Windows.
Il est également possible de l'utiliser en stand-alone pour certaines applications simples.
Malheureusement en l'état actuel, il y a encore un grand nombre de séquences non prises en charge, ceci est toutefois probablement amené à changer étant donné que Colorama est mis à jour régulièrement.

.. [#contact] <killian.castella@he-arc.ch>