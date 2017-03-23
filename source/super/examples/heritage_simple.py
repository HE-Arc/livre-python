"""Module de demo heritage simple sans super."""


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
        Personne.__init__(self, prenom, nom)
        self.domaine = domaine

    def __str__(self):
        """Methode de conversion en string."""
        parent = Personne.__str__(self)
        return f"{parent}, {self.domaine}"


myPersonne = Personne("Jean", "Nemarre")
myEtudiant = Etudiant("Anthony", "Fleury", "DLM")

print(myPersonne)
print(myEtudiant)
