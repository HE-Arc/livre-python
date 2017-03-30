"""Exemple très simpliste de hashage de cookie en utilisant blake 2."""

from hashlib import blake2b
from hmac import compare_digest
from http import cookies

# Constantes qui permettent un hashage "personnalisé" du cookie
SECRET_KEY = b'cle secrete provenant du serveur'
AUTH_SIZE = 16


def sign(cookie):
    """Signe le cookie."""
    h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY)
    h.update(cookie.output().encode('utf-8'))
    cookie['signature'] = h.hexdigest()


user_name = input("Entrez votre nom d'utilisateur : ")

# Le cookie sera le même pour tester l'identité
cookie = cookies.SimpleCookie()
cookie['user'] = user_name

print("\nBienvenue "
      f"{user_name} votre cookie hashé est le suivant : ")
# Récupère le cookie signé en fonction de la personne qui s'identifie
sign(cookie)
# Affiche ce dernier pour montrer ce qui devrait être utilisé dans une
# vraie application

print("\nCookie:", cookie, sep="\n")

user_name = input("\nConfirmez votre identité : ")

# Si le cookie est hashé par la même personne, on sait que cela n'a pas changé

new_cookie = cookies.SimpleCookie()
new_cookie['user'] = user_name
sign(new_cookie)

if compare_digest(cookie['signature'].value, new_cookie['signature'].value):
    print("\nVous êtes bien vous-même")
else:
    # Génère une erreure dans le cas ou le hashage n'est plus le même
    print("\nVous avez changé d'identité")
