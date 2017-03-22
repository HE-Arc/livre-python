"""Module d'exemple d'instanciation d'un bytes."""


msg = bytes('exemple', encoding='utf-8')
# On peut aussi affecter une chaine directement
# mais l'encodage par défaut sera utilisé.
msg = b"exemple$"
