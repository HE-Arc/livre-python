"""Example de Pycrypto."""
from Crypto import Random
from Crypto.Cipher import AES, DES

iv_AES = Random.new().read(AES.block_size)  # Vetor d'initialisation
iv_DES = Random.get_random_bytes(8)  # Vector d'initialisation

key_AES = 'abcdefghijklmnop'
key_DES = 'abcdefgh'

aese = AES.new(key_AES, AES.MODE_CFB, iv_AES)
aesd = AES.new(key_AES, AES.MODE_CFB, iv_AES)
dese = DES.new(key_DES, DES.MODE_CFB, iv_DES)
desd = DES.new(key_DES, DES.MODE_CFB, iv_DES)

plaintext = 'Hello! World'

plaintext = aesd.decrypt(aese.encrypt(plaintext))

print(plaintext)

plaintext = aesd.decrypt(dese.encrypt(plaintext))

print(plaintext)
