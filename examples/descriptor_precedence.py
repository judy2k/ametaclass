

class DataDescriptor:
    def __get__(self, instance, owner):
        return "A data descriptor value"
    
    def __set__(self, instance, value):
        print(f"Setting {value!r} on {instance!r}")


class NonDataDescriptor:
    def __get__(self, instance, owner):
        return "A non-data descriptor value"


class DesignedToConfuseYou:
    data = DataDescriptor()
    non_data = NonDataDescriptor()

    def __init__(self):
        self.__dict__['data'] = "Data set on the instance."
        self.non_data = "Not data set on the instance."


confusion = DesignedToConfuseYou()
print(confusion.__dict__['data'], confusion.__dict__['non_data'])
print(DesignedToConfuseYou.__dict__['data'], DesignedToConfuseYou.__dict__['non_data'])
print(confusion.data)
print(confusion.non_data)
