.. _secrets-tutorial:

``secrets``
===========

.. image:: ./img/lock.png
    :scale: 30%
    :align: right
    :alt: lock logo
    :target: https://cdn.pixabay.com/photo/2017/01/10/03/54/icon-1968247_960_720.png

Par Maël Pedretti [#mp]_

Introduction
------------
Avec une croissance toujours plus rapide et s'intégrant de plus en plus dans notre quotidien, l'informatique moderne requiert une sécurité accrue. Les équipements devenant de plus en plus puissants, il n'est plus suffisant d'utiliser des chaînes pseudo-aléatoires pour sécuriser une transmission. Pour remédier à ce problème, Python s'est aggrandi du module suivant.

:py:mod:`secrets` est un module python utilisé pour générer des chaînes de caractères aléatoires cryptographiquement fortes. Celles-ci sont utilisables pour gérer des données telles que des mots de passe, des authentifications, des jetons de sécurité et autres secrets associés. Ce module n'est disponible que depuis la version 3.6 de python (:pep:`506`).


Utilisations
------------
Ce mode devrait être utilisé de préférence au générateur de nombres pseudo-aléatoires par défaut dans le module :py:mod:`random`, qui est conçu pour la modélisation et la simulation et non pas la sécurité ou la cryptographie.

Nombres aléatoires
******************
Ce module donne accès à la source d'aléatoire la plus sécurisée que votre système d'exploitation fournit. Pour fournir des nombres aléatoirs cryptographiquement sûres, le système ne se base pas sur des calculs mais sur un composant physique (`un générateur de nombres aléatoires matériel`_) réagissant à des phénomènes microscopiques qui créent de faibles signaux de bruit statistiquement aléatoires, comme le bruit thermique ou l'effet photoélectrique.

- Classe :py:class:`secrets.SystemRandom` permet de générer des nombres aléatoires, voir :py:class:`random.SystemRandom` pour plus de détails
- :py:func:`secrets.choice(séquence) <secrets.choice()>` retourne un élément aléatoire à partir d'une *séquence*
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
D'après la documentation python, des jetons de 32 bytes sont suffisament sécurisés à l'heure actuelle.

Autre
*****

- :py:func:`secrets.compare_digest(a,b) <secrets.compare_digest()>` permet de comparer deux chaînes de texte de manière à réduire le risque d'`attaques temporelles`_. Pour faire court, une attaque temporelle consiste à mesurer le temps requis pour comparer deux chaînes et de ce fait en déduire l'algorithme de comparaison afin de pouvoir subtiliser un mot de passe ou une chaîne de chiffrement.

Exemples
--------

.. literalinclude:: ./examples/password.py

.. code-block:: console

    $ python password.py
    68sZmkdve4

Génération d'un jeton hexadécimal d'une longueur de 16 bytes.

.. code-block:: pycon

    >>> secrets.token_hex(16)
    b'7e5e31e55f5a878980bb230b7e5c7fbe'

Génération d'un jeton d'une longueur de 16 bytes pouvant être utilisé dans une URL

.. code-block:: pycon

    >>> secrets.token_urlsafe(16)
    k84RkJMyMpX6e3qzVXRqcw

On notera la différence de longueur des deux chaînes de 16 bytes. L'encodage utilisé dans la deuxième (base64) encode environ un caractère sur 6 bits tandis que dans la première ce ne sont que 4 bits qui sont convertis en un caractère.


Tokens et sécurité annexe
-------------------------

L'image ci-dessous démontre l'utilisation de tokens. Pour qu'une application tierce puisse se connecter à l'`API Twitter`_, OAuth_ est utilisé pour lui fournir un accès sécurisé. Dans ce cas, deux jetons sont générés pour pouvoir se connecter. De ce fait, twitter peut vérifier que l'application qui a requis les informations est bien autorisée à le faire et qu'elle respecte le niveau de confidentialité enregistré dans les paramètres.

Dans ce cas, le jeton correspond à une chaîne de caractère hachée selon l'algorithme de cryptographie HMAC_ (Python comprend un module :py:mod:`hmac`). Afin de crypter correctement la chaîne d'origine, il est nécessaire d'avoir une clé suffisament sûre. Une clé sûre est une clé ayant été générée par une source suffisament aléatoire et étant suffisament longue.

Pour que la sécurité des échanges soit garantie, il ne faut pas que la clé aléatoire puisse être prédite par le hacker. Une source d'aléatoire comme random est prédictible et permet donc au final de déduire la clé et ensuite de voler les données cryptées. En effet, il suffit de faire crypter le même message plusieurs fois, de le décrypter par force brute, d'en déduire les clés utilisées, de faire un peu de maths, et si la source n'est pas sûre, il est possible de prédire les futures clés produites et donc de décrypter toutes les communications. C'est ce qu'on appelle une `attaque de générateur de nombre aléatoire`_.

C'est là qu'est tout l'intérêt du module secret et de ses fonctions de génération de chaînes aléatoires. En empêchant qui que ce soit de prédire les résultats aléatoires, il est possible d'empêcher que les clés soient découvertes.

.. image:: ./img/exampleTwitterApi.PNG
    :scale: 100%
    :align: center
    :alt: twitter exemple of the use of tokens


Cependant, le problème ne s'arrête pas là. Premièrement, lors des communications, si aucun protocole de sécurité de couche de transport n'est utilisé, la durée de validité d'un secret partagé ne doit pas être supérieur au temps qu'il faudrait à un hacker pour le découvrir via une attaque de force brute. Le serveur doit donc adapter la complexité du secret partagé. Une bonne pratique consiste à générer les secrets aussi longs que possibles afin d'avoir une sécurité maximum [#rfc5849]_.

Deuxièmement, lorsque le jeton est reçu en retour et qu'il faut le comparer au jeton calculé à partir de la chaîne de référence et de la clé secrète, cela peut créer des failles de sécurité. Il s'agit des attaques temporelles citées plus haut. Si la fonction de comparaison n'est pas assez sûre et ne prend pas toujours le même temps pour comparer les jetons et retourner la réponse, un hacker suffisament doué pourra récupérer des informations sur le système de comparaison, et de ce fait déduire le jeton correct en le devinant bytes après bytes.

Conclusion
----------

Le module :py:mod:`secrets` est un module destiné aux utilisateurs avancés ayant des besoins de sécurité supérieurs à la normale. 
Il est simple d'utilisation et offre différents outils permettant la création de mots de passe et jetons sécurisés. Toutefois, ce module n'offre pas la sécurité absolue. Il est nécessaire de connaître le domaine de la sécurité avant d'utiliser les fonctions le composant en se disant que magiquement les données seront protégées. Par exemple, un token aléatoire de 8 bytes ne tiendra pas longtemps face à une attaque de brute-force.



.. [#mp] <mael.pedretti@he-arc.ch>
.. [#rfc5849] https://tools.ietf.org/html/rfc5849#section-4.9

.. Bibliographie

.. _URL: https://fr.wikipedia.org/wiki/Uniform_Resource_Locator
.. _base64: https://fr.wikipedia.org/wiki/Base64
.. _force brute: https://fr.wikipedia.org/wiki/Attaque_par_force_brute
.. _API: https://fr.wikipedia.org/wiki/Interface_de_programmation
.. _attaques temporelles: https://fr.wikipedia.org/wiki/Attaque_temporelle
.. _API Twitter: https://dev.twitter.com/oauth
.. _OAuth: https://oauth.net
.. _HMAC: https://tools.ietf.org/html/rfc2104.html
.. _un générateur de nombres aléatoires matériel: https://fr.wikipedia.org/wiki/Générateur_de_nombres_aléatoires_matériel
.. _attaque de générateur de nombre aléatoire: https://en.wikipedia.org/wiki/Random_number_generator_attack