"""Module de demo heritage simple avec super."""


class Personne:
    """Classe représentant une personne."""

    def __init__(self, prenom, nom):
        """Methode d"initialisation."""
        self.prenom = prenom
        self.nom = nom

    def __str__(self):
        """Methode de conversion en string."""
        return f"{self.nom} {self.prenom}"


class Etudiant(Personne):
    """Classe représentant un étudiant."""

    def __init__(self, prenom, nom, domaine):
        """Methode d"initialisation."""
        super().__init__(prenom, nom)
        self.domaine = domaine

    def __str__(self):
        """Methode de conversion en string."""
        parent = super().__str__()
        return f"{parent}, {self.domaine}"


myPersonne = Personne("Jean", "Nemarre")
myEtudiant = Etudiant("Anthony", "Fleury", "DLM")

print(myPersonne)
print(myEtudiant)
