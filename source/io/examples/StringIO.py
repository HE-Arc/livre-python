"""Exemple de gestion de flux avec io.StrionIO."""

import io

output = io.StringIO()
output.write(u'First line.\n')  # u is for Unicode
output.write(u'Second line.\n')

# Retrieve file contents
contents = output.getvalue()

# Display:
# First Line.
# Second line.
print(contents)

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()
