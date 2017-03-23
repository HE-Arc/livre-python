import weakref

class CircularRef(object):
    def __init__(self):
        self.obj = None
        print('created')

    def __destroy__(self):
        print('destroy')

    def store(self, obj)
        self.obj = weakref.ref(obj)

    """
    Solution équivalente:

    def store(self,obj)
        self.obj = weakref.proxy(obj)
    """
