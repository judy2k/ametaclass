class ClientMeta(type):
    def __new__(mcs, name, bases, classdict, **kwargs):
        result = super().__new__(mcs, name, bases, dict(classdict))
        print("Classdict:", classdict.keys())
        return result

    def a_method(self):
        print("Called a method!", self)


class ClientBase(metaclass=ClientMeta, private=True):
    def __init__(self):
        print("Selfie!")

cb = ClientBase()
try:
    cb.a_method()
except AttributeError:
    print("Can't call a_method on the instance.")

cb.__class__.a_method()