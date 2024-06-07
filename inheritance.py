# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make sounds"

# Derived class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Another derived class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Another level of inheritance
class Bulldog(Dog):
    def speak(self):
        return "Woof! Woof!"

# Function to demonstrate polymorphism
def animal_speak(animal):
    print(f"{animal.name} says: {animal.speak()}")

# Creating instances of each class
generic_animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")
bulldog = Bulldog("Max")

# Demonstrating polymorphism
animal_speak(generic_animal)
animal_speak(dog)
animal_speak(cat)
animal_speak(bulldog)
