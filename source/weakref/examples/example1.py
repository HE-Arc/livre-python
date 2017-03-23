"""This is a simple example of weakref."""


class ExampleWeakref(object):
        """Class of a simple strong ref."""

        def __init__(self):
                """Constructor."""
                self.obj = None
                print('created')

        def __destroy__(self):
                """Destructor."""
                print('destroy')
