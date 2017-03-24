"""Exemple très simpliste de hashage de cookie en utilisant blake 2."""

import hashlib
import hmac

from hashlib import blake2b
from hmac import compare_digest

# Constantes qui permettent un hashage "personnalisé" du cookie
SECRET_KEY = b'cle secrete provenant du serveur'
AUTH_SIZE = 16


def sign(cookie, personne):
    """Hashe le cookie en fonction de la personne (paramètre de blake2)."""
    h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY, person=personne)
    h.update(cookie)
    return h.hexdigest()


user_name = input("Entrez votre nom d'utilisateur : ")

# Le cookie sera le même pour tester l'identité
cookie = 'user:'+user_name
cookie = cookie.encode()

print("\nBienvenu " + user_name + " votre cookie hashé est le suivant : ")
# Récupère le cookie signé en fonction de la personne qui s'identifie
cookie_signe = sign(cookie, user_name.encode())
# Affiche ce dernier pour montrer ce qui devrait être utilisé dans une
# vraie application
print("\n" + cookie_signe)

user_name = input("\nConfirmez votre identité : ")

# Si le cookie est hashé par la même personne, on sait que cela n'a pas changé
if compare_digest(cookie_signe, sign(cookie, user_name.encode())):
    print("\nVous êtes bien vous-même")
else:
    # Génère une erreure dans le cas ou le hashage n'est plus le même
    print("\nVous avez changé d'identité")
