class SomeClass(object) :
    grammar ={
        1 : "Some string",
        2 : "Another string",
        3 : 42,
        4 : True
    }

    def __init__(self, name) :
        self.name=name

sc = SomeClass("Totoro")
print (len(sc.name)) #affiche la taille du string (6)
print (len(sc.grammar)) #affiche le nombre d'éléments (4)
