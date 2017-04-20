"""Exemple de hachage simple avec hashlib."""

import getpass
import hashlib
import secrets
from hmac import compare_digest


def hash_mdp(mdp, hashage):
    """Hache le mot-de-passe.

    Ceci à l'aide de l'algorithme passé
    en argument avec un salt permettant
    un hachage plus efficace.

    Args:
        Mot-de-passe normale.
        Type du hachage souhaité.

    Returns:
        Retourne le mot-de-passe haché en hexadécimale.

    """
    # secrets génère un nombre aléatoire en héxadécimale
    salt = secrets.token_hex(16)
    contenu = salt + mdp
    h = hashlib.new(hashage)
    h.update(contenu.encode('utf-8'))
    return h.hexdigest() + ':' + salt


def check_mdp(hashed_mdp, utilisateur_mdp, hashage):
    """Check le mot-de-passe haché.

    Ceci en récupérant le mot de passe haché
    et le salt du mdp haché passée en argument.
    L'objet hachage est construit en fonction du type.

    Args:
        Le mot-de-passe haché,le mot-de-passe
        normale ainsi que le type de hachage.

    Returns:
        Retourne true ou false en fonction
        du test d'égalité.

    """
    mdp, salt = hashed_mdp.split(':')
    contenu = salt + utilisateur_mdp
    h = hashlib.new(hashage)
    h.update(contenu.encode('utf-8'))
    return compare_digest(mdp, h.hexdigest())


hashage_type = input("Entrez le type de hachage souhaité : ")

# Boucle permettant de récupérer un type de hachage correct !
while hashage_type not in hashlib.algorithms_available:
    if hashage_type != "help":
        print("\nEntrez help pour voir les types de hachage possibles")

    hashage_type = input("\nVeuillez entrer un type de hachage valide : ")

    if hashage_type == "help":
        print(hashlib.algorithms_available)

# Getpass permet de ne pas afficher en claire le mot-de-passe saisi
mdp = getpass.getpass("\nEntrez votre mot de passe : ")

hashed_mdp = hash_mdp(mdp, hashage_type)
print("\n"
      "Le mot de passe devrant être "
      f"enregistré dans la bdd est: {hashed_mdp}")

ancien_mdp = getpass.getpass('\nEntrez-à nouveau votre '
                             'mot-de-passe pour vérifier : ')

# Si le mot-de-passe est correct, alors on affiche un message de confirmation
if check_mdp(hashed_mdp, ancien_mdp, hashage_type):
    print('\nVotre mot-de-passe est correct')
else:
    print("\nJe suis désolé, ce n'est pas le bon mot-de-passe")
