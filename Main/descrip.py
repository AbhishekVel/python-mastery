
class Descriptor:
    def __init__(self, name):
        self.name = name
        
    def __get__(self, instance, cls):
        print('%s:__get__' % self.name)

    def __set__(self, instance, cls):
        print('%s:__set__' % self.name)
        
    def __delete__(self, instance, cls):
        print('%s:__delete__' % self.name)
        