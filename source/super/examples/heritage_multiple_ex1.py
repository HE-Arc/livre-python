"""Module de demo héritage multiple sans super."""


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
        A.test(self)


class C(A):
    """Classe Père."""

    def test(self):
        """Methode de test."""
        print("Appel de test depuis C")
        A.test(self)


class D(B, C):
    """Classe Enfant."""

    def test(self):
        """Methode de test."""
        print("Appel de test depuis D")
        B.test(self)
        C.test(self)


nouveauD = D()
nouveauD.test()
