def stupid_metaclass(classname, bases, attrdict):
    return type(classname, bases, attrdict)


class MyClass(metaclass=stupid_metaclass):
    pass


instance = MyClass()
