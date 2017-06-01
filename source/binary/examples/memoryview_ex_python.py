"""Module d'exemple d'une memoryview."""


buf = bytearray(b'abcdefgh')
mv = memoryview(buf)
mv[4:6] = b'ZA'
buf
# sortie bytearray(b'abcdZAgh')
