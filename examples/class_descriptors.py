class GetMe:
    def __init__(self, t):
        self.t = t

    def __get__(self, instance, owner):
        return f"You got me: {self.t}"
    
    def __set__(self, instance, value):
        pass


class MyMeta(type):
    get_me = GetMe('meta')


class MyClass(metaclass=MyMeta):
    get_me = GetMe('class')


print(MyClass.get_me)