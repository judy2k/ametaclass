

def init_func(self, color):
        self._color = color

def drive(self):
    print("You are driving the car")


Car = type(
    'Car',
    (object,),
    {
        '__init__': init_func,
        'drive': drive,
    })

my_car = Car('red')