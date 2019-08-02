
class SimpleDescriptor:
    def __get__(self, instance, owner):
        return f"You called __get__ with: {self!r}, {instance!r} {owner!r}"


class JustAnOrdinaryClass:
    get_me = SimpleDescriptor()