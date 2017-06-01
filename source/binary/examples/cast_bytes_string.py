"""Module d'exemple de cast entre un bytes et un string."""


# Cast string en bytes.
my_str = "exemple"
bytes = str.encode(my_str)

# Cast bytes en string.
my_decoded_str = str.decode(bytes)
type(my_decoded_str)  # vérifie que le type est string
