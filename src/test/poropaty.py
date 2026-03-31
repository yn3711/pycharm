class ExampleClass(object):
    def __init__(self):
        self.value = None

    def get_value(self):
        return self.value

    #def set_value(self, arg):

        #return self.value = arg

    value = property(get_value, set_value)

ins = ExampleClass()
ins.value = 'test'
ins.value