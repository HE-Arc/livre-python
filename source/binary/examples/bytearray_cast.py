"""Module d'exemple de cast entre bytes et bytearray."""


# Cast bytes à bytearray.
mutable_bytes = bytearray(b'\x00\x0F')

# Cast bytearray à bytes.
immutable_bytes = bytes(mutable_bytes)
