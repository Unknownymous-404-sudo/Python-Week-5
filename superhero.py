# Base class
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        print(f"I am {self.name} from the {self.universe} universe! My power is {self.power}.")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")


# Child class 1
class Speedster(Superhero):
    def __init__(self, name, universe, speed_level):
        super().__init__(name, "Super Speed", universe)
        self.speed_level = speed_level  # This is a unique attribute

    def use_power(self):
        print(f"{self.name} zooms past at speed level {self.speed_level}!")


# Child class 2
class Flyer(Superhero):
    def __init__(self, name, universe, flight_height):
        super().__init__(name, "Flight", universe)
        self.flight_height = flight_height

    def use_power(self):
        print(f"{self.name} flies up to {self.flight_height} meters in the sky!")


# Objects for my superheroes
Speed = Speedster("Speed", "DC", speed_level=10)
SpeedDemon = Flyer("SpeedDemon", "Marvel", flight_height=10000)

# Try them out
Speed.introduce()
Speed.use_power()

print()  # Just a spacer

SpeedDemon.introduce()
SpeedDemon.use_power()

print()  # Just a spacer

# Polymorphism Challenge
# Parent class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving...")


# Child class 1
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road! 🚗")


# Child class 2
class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in the sky! ✈️")


# Child class 3
class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on the water! 🚤")


# Create some vehicle objects
my_car = Car("Audi Q5")
my_plane = Plane("Boeing 747")
my_boat = Boat("Speedboat")

# Call their move methods (polymorphism in action!)
my_car.move()

print()  # Just a spacer

my_plane.move()

print()  # Just a spacer

my_boat.move()
