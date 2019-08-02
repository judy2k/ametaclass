# class Turnable:
#     def turn(self, direction):
#         print("Turning the vehicle.")

class Car:
    def __init__(self, color):
        self._color = color

    def drive(self):
        print("You are driving the car")

my_car = Car('red')