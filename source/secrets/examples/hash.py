"""
Hashage d'un message avec hmac à partir d'une clé générée par secrets.

La clé secrète est connue du client et du serveur uniquement.
Normalement un identifiant est transmis afin que le serveur puisse
trouver la clé privée correspondant au client

La clé secrète peut être générée de n'importe quelle manière,
pour autant qu'elle soit cryptographiquement sûre.
"""

import hmac
import secrets

# Le client a un message à transmettre, il le hash et
# envoie le message et la signature (digest)

secret_key = secrets.token_bytes(32)
message = "Ceci est un exemple de hashage"

encoded_message = message.encode('utf-8')
hash_object = hmac.new(secret_key, encoded_message)
digest = hash_object.digest()

print("Client digest -- ", digest)

# Admettons maintenant que le serveur reçoive le message et le digest.
# Il répète le même processus et compare les resultats.

server_encoded_message = message.encode('utf-8')
server_hash_object = hmac.new(secret_key, server_encoded_message)
server_digest = server_hash_object.digest()

print("Server digest -- ", server_digest)

if(secrets.compare_digest(digest, server_digest)):
    print("-> Provenance confirmée")
else:
    print("-> Provenance non confirmée")
