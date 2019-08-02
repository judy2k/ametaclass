import itertools

class A:
    def a(self):
        print("You called a")

class B:
    def b(self):
        print("You called b")

class C:
    def c(self):
        print("You called c")


def init_combinations():
    for parents in itertools.combinations([A, B, C], 2):
        classname = ''.join([c.__name__ for c in parents])
        print(f"Creating class: {classname}, with parents: {parents!r}")
        globals()[classname] = type(classname, parents, {})

init_combinations()

my_ab = AB()
print(f"Bases: {AB.__bases__}")
my_ab.a()
my_ab.b()
my_ab.c()