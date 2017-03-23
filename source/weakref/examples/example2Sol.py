"""This is an example with a weakref solution."""

import weakref


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
                """Store a weakref in the object."""
                self.obj = weakref.ref(obj)

        def storeProxy(self, obj):
                """Store a ref in the object with the proxy weakref."""
                self.obj = weakref.proxy(obj)
