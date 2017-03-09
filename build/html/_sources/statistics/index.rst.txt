.. _statistics-tutorial:

statistics
==========

Par Jérémy dubois [jd]_

Introduction
--------------
le module :py:mod:`statistics` est un ensemble de fonctions offrant la possibilité de résoudre des problèmes
mathématiques de statistiques avec des valeures "real".

Il faut noté que ces méthodes ne supportent pas tous les types de variable. Sans précision explicite,
seul les *int, float, decimal.Decimal* et *fraction.Fraction* sont supportés.

Fonctions
---------

Moyenne et calcul de valeur central
**************************************

Les fonctions suivantes permettent de calculer la moyenne ou d'autres valeurs typiques d'une population ou d'un échantillon.

:ref:`mean() <mean>` : Évaluation de la moyenne arithmétique.

:ref:`harmonic_mean() <harmonic>` : Évaluation de la moyenne harmonique.

:ref:`median() <median>` : Évaluation de la médiane. On prend la valeur centrale, même si elle n'est pas dans les données.

:ref:`median_low() <mLow>` : Évaluation de la médiane basse.

:ref:`median_high() <mHigh>` : Évaluation de la médiane haute.

:ref:`median_grouped() <mGr>` : Évaluation de la médiane pour des données groupées.

:ref:`mode() <mode>` : Évalutaion de valeurs la plus commune dans un ensemble de valeurs discrètes.

Mesure de dispersion
*************************

Tandis que les fonctions ci-dessous calculent les valeurs de variations avec des valeurs standards ou moyennes.

:ref:`pstdev() <pstdev>` : Retourne l'écart type de la population des données.

:ref:`pvariance() <pVar>` : Retourne la variance de la population des données.

:ref:`stdev() <stdev>` : Retourne l'écart type de l'échantillon de données.

:ref:`variance() <var>` : Retourne la variance de l'échantillon de données.

.. _error:

Exception
----------

Dans cette bibliothèque, il n'y a qu'une seule exception de définie; *statistics.StatisticError*.
Cette erreur apparait lorsque les données fournies aux méthodes sont insuffisantes ou inexistantes.

Descriptions et exemples
------------------------

L'ensemble de ces fonctions ne nécessite pas que les données qui sont fournies soient triées.

.. _mean:

statistics.mean(*data*)
*************************************************

Cette méthode retourne la valeur moyenne de données fournies qu'elles soit sous forme de série ou
d'itérateur.

La logique de la fonction est de sommer toutes les valeurs fournies et et de diviser cette somme par
le nombre de ces valeurs.

Exemples d'utilisation:

.. code-block:: pycon

  >>> mean([1, 4, 9, 11])
  6.25
  >>> mean([-2.0, 1.5, 4.35, 7.4])
  2.8125

Si les données sont vides, l'erreur :ref:`statisticsError <error>` est signalée.

.. _harmonic:

statistics.harmonic_mean(*data*)
*************************************************

Cette méthode a été introduite dans la version 3.6. Elle permet de calculer la moyenne harmonique
d'une série, d'un échantillon ou d'un itérateur de données.

La moyenne harmonique est un type de moyenne utile pour trouver la mesure central de données, qui
montre tout son intérêt lorsqu'il faut étudier des taux, par exemple les vitesses.

On calcul la moyenne harmonique en utilisant l'inverse de la moyenne arithmétique avec des données inversées.
 Imaginons qu'il y aie trois valeur a, b et c; le calcul serait donc (3/(1/a + 1/b + 1/c))

Exemple d'utilisation:

.. code-block:: pycon

  >>> harmonic_mean([2.5, 3, 10])
  3.6

Si les données sont vides, l'erreur :ref:`statisticsError <error>` est signalée.

.. _median:

statistics.median(*data*)
*************************************************

Cette méthode calcul la valeur médiane de données numériques. Ces dernières peuvent
venir sous plusieurs forme; séries ou itérateurs.

*median()* emploie la règle mathématique de la moyenne des éléments centraux. C'est à dire que
suivant le nombre de valeurs, le comportement le résultat peux être hors des des données.

Exemples:

Nombre de valeurs, impaire.

.. code-block:: pycon

  >>> median([1, 4, 9])
  4

Nombre de valeurs, paire.

.. code-block:: pycon

  >>> median([1, 4, 6, 9])
  5.0

On remarque que dans la série paire, la valeurs médiane a été interpolée.

Si les données sont vides, l'erreur :ref:`statisticsError <error>` est signalée.


.. _mLow:

statistics.median_low(*data*)
*************************************************

Cette méthode calcul le même élément que *median()* mais avec cette fonction la valeurs médiane
est toujours une valeurs parmis les données choisies. Les données peuvent prendre les même forme
que pour la fonction précédente; série ou itérateur.

La valeur médiane rendue par cette méthode est toujours la plus petite des deux valeurs centrales.

Exemples:

Nombre de valeurs, impaire.

.. code-block:: pycon

  >>> median_low([1, 4, 9])
  4

Nombre de valeurs, paire.

.. code-block:: pycon

  >>> median_low([1, 4, 6, 9])
  4

On utilise la médiane basse sur des données discrètes et dont la valeurs médiane doit appartenir
à l'ensemble choisi.

Si les données sont vides, l'erreur :ref:`statisticsError <error>` est signalée.

.. _mHigh:

statistics.median_high(*data*)
*************************************************

Cette méthode calcul le même élément que *median()* mais avec cette fonction la valeurs médiane
est toujours une valeurs parmis les données choisies. Les données peuvent prendre les même forme
que pour la fonction précédente; série ou itérateur.

La valeur médiane rendue par cette méthode est toujours la plus grande des deux valeurs centrales.

Exemples:

Nombre de valeurs, impaire.

.. code-block:: pycon

  >>> median_high([1, 4, 9])
  4

Nombre de valeurs, paire.

.. code-block:: pycon

  >>> median_high([1, 4, 6, 9])
  6

On utilise la médiane haute sur des données discrètes et dont la valeurs médiane doit appartenir
à l'ensemble choisi.

Si les données sont vides, l'erreur :ref:`statisticsError <error>` est signalée.

.. _mGr:

statistics.median_grouped(*data, interval=1*)
*************************************************

Cette méthode retourne la médiane de données groupées continues. Elle résout en cherchant le
50e centile avec la méthode de l'interpolation. Les données que la fonction peut traiter ont la
frome de séries ou d'itérateurs.

L'argument *interval* est optionnel. Si il n'est pas fourni, la fonction prend la valeur par défault
1. Dans l'exemple ci-dessous, onconstat aussi que cette argument influe sur l'interpolation du résultat.

Exemples d'utilisation:

.. code-block:: pycon

  >>> median_grouped([42, 43 , 44, 45])
  43.5
  >>> median_grouped([1, 2, 2, 2, 2, 3, 3, 4, 6])
  2.375
  >>> median_grouped([1, 2, 2, 2, 2, 3, 3, 4, 6], interval=1)
  2.375
  >>> median_grouped([1, 2, 2, 2, 2, 3, 3, 4, 6], interval=2)
  2.75

Cette fonciton ne vérifie pas si les valeurs sont séparées par au moins *interval*.

Si les données sont vides, l'erreur :ref:`statisticsError <error>` est signalée.

.. _mode:

statistics.mode(*data*)
*************************************************

Cette méthode retourne l'élément le plus commun d'un ensembe de données, soit numérique, soit nominale.

Exemples d'utilisation:

.. code-block:: pycon

  >>> mode([1, 2, 2, 3, 4, 4, 4, 4, 10])
  4

C'est la seule méthode de statistique qui s'applique aussi à des données nominales.

.. code-block:: pycon

  >>> mode(["red", "yellow", "blue", "blue", "yellow", "yellow", "yellow",])
  'yellow'

Si les données sont vides ou si il n'y a pas qu'une seule valeur la plus représentée, l'erreur :ref:`statisticsError <error>` est signalée.

.. _pstdev:

statistics.pstdev(*data, mu=None*)
*************************************************

Cette méthode retourne l'écart type standard d'une population ( c'est aussi la racine carrée de la
variance de la population). Voir :ref:`pvariance() <pVar>` pour l'explication des arguments.

Exemple d'utilisation:

.. code-block:: pycon

  >>> pstdev([0.5, 2.5, 5.5, 6.25, 9.5])
  3.1128764832546763

Si les données sont vides, l'erreur :ref:`statisticsError <error>` est signalée.

.. _pVar:

statistics.pvariance(*data, mu=None*)
*************************************************

Cette méthode retourne la variance de population des données. La variance est une mesure de la
dispersion des données. Plus la variance est grande, plus les valeurs sont étalées. Tandis qu'une
petite variance indique que les valeurs sont regroupées autour de la moyenne.

L'argument *mu* est optionnel, mais il peut être utilisé si la moyenne des données a déjà étée
calculée. Si ce n'est pas le cas ou que l'argument est *None*, la méthode calcul automatiquement *mean()*.

Cette méthode est utile lorsqu'il est souhaité de calculé la variance d'une entière population.
Par contre, il mieux d'utiliser :ref:`variance() <var>` si on estime des échantillons.

Exemples d'utilisation:

.. code-block:: pycon

  >>> data= [0.0, 0.25, 1.5, 2.25, 2.75, 3.5]
  >>> pvariance(data)
  1.6128472222222223
  >>> m = mean(data)
  >>> variance(data, m)
  1.6128472222222223

La fonction n'essaie pas de vérifier la valeur de *mu* donc l'utilisation d'une valeur arbitraire
pour *mu* peut mener à un résultat invalide ou impossible.

Si les données sont vides, l'erreur :ref:`statisticsError <error>` est signalée.

Cette méthode supporte aussi les types *Decimal* et *Fraction*.

Exemple:

..code-block:: pycon

    >>> from decimal import Decimal as D
    >>> statistics.pvariance([D("42.00"), D("48.25"), D("48.25"), D("49.5"), D("51.25")])
    9.765
    >>> from fractions import Fraction as F
    >>> statistics.pvariance([F(1, 4), F(5, 4), F(1, 2)])
    13/72

.. _stdev:

statistics.stdev(*data, xbar=None*)
*************************************************

Cette méthode retourne l'écart type standard ( c'est aussi la racine carrée de la
variance de la population). Voir :ref:`variance() <var>` pour l'explication des arguments.

Exemple d'utilisation:

.. code-block:: pycon

  >>> stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
  1.0810874155219827

Si il y a moins de deux valeurs, l'erreur :ref:`statisticsError <error>` est signalée.

.. _var:

statistics.variance(*data, xbar=None*)
*************************************************

Cette méthode retournela variance d'un échantillon de données, un itérative d'au moins deux
nombres réels. La variance mesure la dispersion des données. Une Grande variance indique que les
valeurs sont éparses. Tandis qu'une petite indique que les données sont regroupées vers la valeurs
de la moyenne.

*xbar* est un argument optionnel qui représente la moyenne des données de l'argument *data*.
Si, *xbar* est *None* ou n'est pas rempli, alors la moyenne est calculée automatiquement.

On utilise cette fonction lorsqu'il est souhaité de calculer la variance d'échantillons d'une population.
Si on veut calculer la variance sur toute la population, voir :ref:`pvariance() <pVar>`.

Exemples d'utilisation:

.. code-block:: pycon

  >>> data= [2.75, 1.25, 0.75, 0.5, 1.75, 3.25]
  >>> variance(data)
  1.2104166666666667


Si la moyenne a déjà été calculée on peut l'entrer dans l'argument *xbar*.

.. code-block:: pycon

  >>> m = mean(data)
  >>> variance(data, m)
  1.2104166666666667

La fonction n'essaie pas de vérifier la valeur de *xbar* donc l'utilisation d'une valeur arbitraire
pour *xbar* peut mener à un résultat invalide ou impossible.

Si il y a moins de deux valeurs, l'erreur :ref:`statisticsError <error>` est signalée.

Cette méthode supporte aussi les types *Decimal* et *Fraction*.

Exemple:

..code-block:: pycon

    >>> from decimal import Decimal as D
    >>> statistics.variance([D("42.00"), D("48.25"), D("48.25"), D("49.5"), D("51.25")])
    12.20625
    >>> from fractions import Fraction as F
    >>> statistics.variance([F(1, 4), F(5, 4), F(1, 2)])
    13/48

Conclusion
----------

Cette bibliothèque permet de ne pas devoir recoder les outils mathématique
de statistique.

.. [jd] <jeremy.dubois@he-arc.ch>
