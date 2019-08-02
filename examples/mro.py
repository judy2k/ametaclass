from inspect import getmro
from operator import attrgetter

class Horatio:
    def callme(self):
        print("Horatio")


class James(Horatio):
    def callme(self):
        print("James")


class Tom(James):
    def callme(self):
        print("Tom")

print(getmro(Tom))
my_tom = Tom()
my_tom.callme()


class AlphabeticMRO(type):
    def __new__(cls, name, bases, classdict):
        return super().__new__(cls, name, bases, classdict)

    def mro(self):
        default = super().mro()
        return list(sorted(default, key=attrgetter('__name__')))

class Horatio(metaclass=AlphabeticMRO):
    def callme(self):
        print("Horatio")


class James(Horatio):
    def callme(self):
        print("James")


class Tom(James):
    def callme(self):
        print("Tom")

print(getmro(Tom))
my_tom = Tom()
my_tom.callme()