import abc

class Driveable(abc.ABC):
    @abc.abstractmethod
    def drive(self):
        pass

# This is *also* abstract - no `drive` method:
class Car(Driveable):
    def drive(self):
        print("Driving!")

my_car = Car()
# Traceback (most recent call last):
#   File "abc_example.py", line 13, in <module>
#     my_car = Car()
# TypeError: Can't instantiate abstract class Car with abstract methods drive
my_car.drive()