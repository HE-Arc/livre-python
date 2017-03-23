"""Module de démonstration du Diamond Problem."""


class A:
    """Classe Ancêtre."""

    def test(self):
        """Methode de test."""
        print("Appel de test depuis A")


class B(A):
    """Classe Mère."""

    def test(self):
        """Methode de test."""
        print("Appel de test depuis B")


class C(A):
    """Classe Père."""

    def test(self):
        """Methode de test."""
        print("Appel de test depuis C")


class D(B, C):
    """Classe Enfant."""

    pass


nouveauD = D()
nouveauD.test()
