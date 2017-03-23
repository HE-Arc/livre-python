.. _statistics-tutorial:

statistics
==========

Par Jérémy dubois [jd]_

Introduction
------------
le module statistics_ est un ensemble de fonctions offrant la possibilité de résoudre des problèmes
mathématiques de statistiques avec des valeures "real".

Il faut noté que ces méthodes ne supportent pas tous les types de variable. Sans précision explicite,
seul les *int, float, decimal.Decimal* et *fraction.Fraction* sont supportés.

:ref:`conclusion`

Fonctions
---------

Les fonctions suivantes permettent de calculer la moyenne ou d'autres valeurs typiques d'une population ou d'un échantillon.

:ref:`mean`
*mean()* : Évaluation de la moyenne arithmétique.

:ref:`harmonic`
*harmonic_mean()* : Évaluation de la moyenne harmonique.

:ref:`median`
*median()* : Évaluation de la médiane. On prend la valeur centrale, même si elle n'est pas dans les données.

:ref:`mLow`
*median_low()* : Évaluation de la médiane basse.

:ref:`mHigh`
*median_high()* : Évaluation de la médiane haute.

:ref:`mGr`
*median_grouped()* : Évaluation de la médiane pour des données groupées.

:ref:`mode`
*mode()* : Évalutaion de valeurs la plus commune dans un ensemble de valeurs discrètes.

Tandis que les fonctions ci-dessous calculent les valeurs de variations avec des valeurs standards ou moyennes.

:ref:`pstdev`
*pstdev()* :

:ref:`pVar`
*pvariance()* :

:ref:`stdev`
*stdev()* :

:ref:`var`
*variance()* :

Exception
----------

Dans cette bibliothèque, il n'y a qu'une seule exception de définie; *statistics.StatisticError*.
Cette erreur apparait lorsque les données fournies aux méthodes sont insuffisantes ou inexistantes.

Descriptions et exemples
------------------------

.. _mean:

.. _harmonic:

.. _median:

.. _mLow:

.. _mHigh:

.. _mGr:

.. _mode:

.. _pstdev:

.. _pVar:

.. _stdev:

.. _var:

.. _conclusion:

Conclusion
----------

.. [jd] <jeremy.dubois@he-arc.ch>

.. Bibliographie

.. _statistics: https://docs.python.org/3/library/statistics.html
