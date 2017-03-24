from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'Vecteur(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
         return hypot(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, other):
        raise TypeError("On ne peut pas diviser un vecteur !")

vect = Vector(4,7)
print(repr(vect)+" a pour norme "+str(abs(vect)))
vect = vect*2 #(8,14)
vect+=Vector(2,5) #(10,19)
vect/=Vector(4,5) #lève une erreur
