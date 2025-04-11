from collections import namedtuple

car = namedtuple("car", "kinds color size")
my_car = car("prius", "red", "big")

print(my_car.kinds)
print(my_car.color)
print(my_car.size)
