class ExampleWeakref(object):
    def __init__(self):
        self.obj = None
        print('created')

    def __destroy__(self):
        print('destroy')

    def store(self,obj)
        self.obj = obj
