class MyMeta(type):
    def __new__(self, classname, bases, attrdict, private=False):
        if private:
            # Do something clever here
            pass
        return super().__new__(self, classname, bases, attrdict)


class MyClass(metaclass=MyMeta, private=True):
    pass


instance = MyClass()