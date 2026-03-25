from abc import ABC, abstractmethod

# Define an abstract base class 'Idea' using inheritance from 'ABC' class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# Define a concrete class Bird inheriting from Animal
class Bird(Animal):
    # Implementation of the make_sound abstract method
    def make_sound(self):
        print('Chirp! Chirp!')

# Define a concrete class Dog inheriting from Animal
class Dog(Animal):
    # Implementation of the make_sound abstract method
    def make_sound(self):
        print('Woof! Woof!')

# Using the abstract interface
# Create an instance of Dog and call make_sound
dog = Dog()
dog.make_sound()

# Create an instance of Bird and call make_sound
bird = Bird()
bird.make_sound()
