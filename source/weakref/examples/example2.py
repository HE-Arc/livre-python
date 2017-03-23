"""This is an example of a circular reference."""


class CircularRef(object):
        """Class of a circular ref."""

        def __init__(self):
                """Constructor."""
                self.obj = None
                print('created')

        def __destroy__(self):
                """Destructor."""
                print('destroy')

        def store(self, obj):
                """Store a ref in the object."""
                self.obj = obj
