"""Module d'exemple d'une memoryview avec un bytearray."""


# Avec bytearray.
buf = bytearray(b'abcdefgh')
mv = memoryview(buf)
mv[4:6] = b'ZA'
buf
bytearray(b'abcdZAgh')
