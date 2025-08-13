# Unlimited Posistional Arguments
# *args

def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(3, 5, 7)

# Many Keyworded Arguments
# ** kwargs

def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

calculate(2, add=3, multiply=4)

# Create a class similar to TKinter's

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model") # instead of [], so if model not in dict it just gives None not an error

my_car = Car(make="Toyota", model="Rav4", color="red")
print(my_car.make)