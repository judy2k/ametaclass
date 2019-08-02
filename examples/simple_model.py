
class Field:
    def __init__(self, sql_type):
        self._sql_type = sql_type

    def __set_name__(self, owner, name):
        self._name = name
    
    def sql_definition(self):
        return f"{self._name} {self._sql_type}"


def create(cls):
    print(cls._fields())
    fields_part = ', '.join(field.sql_definition() for field in cls._fields())
    return f"CREATE TABLE {cls.__name__} ({fields_part})"


def fields(cls):
    return [v for v in cls.__dict__.values() if isinstance(v, Field)]


def model(cls):
    cls.create = classmethod(create)
    cls._fields = classmethod(fields)
    return cls


@model
class RankedFood:
    name = Field('VARCHAR(128)')
    score = Field('INT')


print(RankedFood.create())
# CREATE TABLE RankedFoods (name VARCHAR(128), score INT)