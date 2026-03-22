# Define a base class Animal
class Animal:
    # Initialize an Animal object with name and species
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Method to simulate making a sound
    def make_sound(self):
        print(f'This {self.species} {self.name} makes a sound.')
    

# Define a subclass Dog of Animal
class Dog(Animal):
    # Initialize a Dog object with name and breed
    def __init__(self, name, breed):
        super().__init__(name, 'Dog') # Call the constructor of Animal
        self.breed = breed


# Define a subclass Cat of Animal
class Cat(Animal):
    # Initialize a Cat object with name and breed
    def __init__(self, name, breed):
        super().__init__(name, 'Cat')
        self.breed = breed


# Define a subclass Shorthair of Cat
class Shorthair(Cat):
    # Initialize a Shorthair object with name and age
    def __init__(self, name, age):
        super().__init__(name, 'Shorthair') # Call the constructor Cat
        self.age = age
