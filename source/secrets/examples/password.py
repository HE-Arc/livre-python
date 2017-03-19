"""
Génération d'un mot de passe aléatoire.

Mot de passe aléatoire de 10 charactères contenant au minimum :

- une lettre majuscule,
- une lettre minuscule,
- et un chiffre.
"""

import string
from secrets import choice

alphabet = string.ascii_letters + string.digits

while True:
    password = ''.join(choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            sum(c.isdigit() for c in password) >= 3):
        break

print(password)
