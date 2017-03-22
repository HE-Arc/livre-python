"""Module d'exemple des opérations avec une memoryview."""


# retourne les données comme string de bytes.
# sortie: b'abc'.
mv = memoryview(b"abc")
mv.tobytes()

# retourne les données en hexadécimale.
# sortie: '616263'.
mv = memoryview(b"abc")
mv.hex()

# retourne les données en une lsite d'élements.
# sortie: [97, 98, 99].
memoryview(b'abc').tolist()

# relacher le buffer.
mv.release()
