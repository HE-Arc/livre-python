"""Module de demo heritage multiple avec super."""


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
        super().test()


class C(A):
    """Classe Père."""

    def test(self):
        """Methode de test."""
        print("Appel de test depuis C")
        super().test()


class D(B, C):
    """Classe Enfant."""

    def test(self):
        """Methode de test."""
        print("Appel de test depuis D")
        super().test()


nouveauD = D()
nouveauD.test()
