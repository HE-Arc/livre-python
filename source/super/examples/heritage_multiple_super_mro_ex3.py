"""Module de demo heritage multiple super et MRO."""


class A:
    """Classe Ancêtre."""

    def __init__(self):
        """Methode d"initialisation."""
        print("Constructeur de A")


class B(A):
    """Classe Mère."""

    def __init__(self):
        """Methode d"initialisation."""
        print("Constructeur de B")
        super().__init__()


class C(A):
    """Classe Père."""

    def __init__(self):
        """Methode d"initialisation."""
        print("Constructeur de C")
        super().__init__()


class D(B, C):
    """Classe Enfant."""

    def __init__(self):
        """Methode d"initialisation."""
        print("Constructeur de D")
        super().__init__()


nouveauD = D()

print(D.__mro__)
print(B.__mro__)
print(C.__mro__)
print(A.__mro__)
