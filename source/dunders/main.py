class Main(object):
    def __init__(self, *args):
        self.cartes = args

    def ajouter(self, carte):
        obj2 = list(self.cartes)  # Converti en liste
        obj2.append(carte)
        self.cartes = tuple(obj2)

    def __str__(self):
        return str(u'; '.join(self.cartes).encode('utf8'))

    def __len__(self):
        return len(self.cartes)

    def __getitem__(self, key):
        # Est appelé quand on fait objet[index] ou objet[key].
        return self.cartes[key]

    def __iter__(self):
        # Est appelé quand on fait un iter(objet).
        # La valeur retournée doit être un iterateur.
        return iter(self.cartes)

    def __reversed__(self):
        # Est appelé quand on fait reversed(objt)
        return reversed(self.cartes)

    def __contains__(self, item):
        # Est appelé quand "in objet"
        return item in self.cartes


main = Main('1Coeur', '7Pique')
print(str(main))

main.ajouter('AsCoeur')

# parc qu'on a défini __iter__!
for carte in main:
    print(carte)

# 1Coeur
print(main[0])

# False
print('3Coeur' in main)

# 3
print(len(main))
