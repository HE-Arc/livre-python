"""Module d'exemple de cast entre un bytes et un int."""


i = 16

# Crée 1 byte avec un int 16.
# Attention à utiliser le bon encodage (little ou big endian).
# vérifiez avec sys.byteorder.
single_byte = i.to_bytes(1, byteorder='big', signed=True)
print(single_byte)

# Crée un bytes avec une liste de int (0-255).
# sortie: b'\xff\xfe\xfd\xfc.
bytes_from_list = bytes([255, 254, 253, 252])

# Print out binary string (e.g. 0b010010).
print(bin(22))

# Bytes à Integer.
# Crée un int avec un bytes (non signé par défaut).
i = int.from_bytes('12', byteorder='big')

# Crée un int signé.
i = int.from_bytes(b'\x00\x0F', byteorder='big', signed=True)

# Utilise une liste d'entiers comme source pour le cast.
i = int.from_bytes([255, 0, 0, 0], byteorder='big')
