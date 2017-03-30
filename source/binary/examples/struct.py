"""Module d'exemple struct."""

from collections import namedtuple
from struct import pack, unpack

# packing et unpacking de trois entiers.
pack('hhl', 1, 2, 3)
# sortie : '\x00\x01\x00\x02\x00\x00\x00\x03'
unpack('hhl', '\x00\x01\x00\x02\x00\x00\x00\x03')
# sortie : (1, 2, 3)

# On peut assigner des noms aux champs.
record = 'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = unpack('<10sHHb', record)

Student = namedtuple('Student', 'name serialnum school gradelevel')
Student._make(unpack('<10sHHb', record))
Student(name='raymond   ', serialnum=4658, school=264, gradelevel=8)
