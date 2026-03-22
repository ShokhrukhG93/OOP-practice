# Define the Animal class
class Animal:
    # Initialize an Animal object with species and diet attributes
    def __init__(self, species, diet):
        self.species = species
        self.diet = diet
    

# Define the Mammal subclass of Animal
class Mammal(Animal):
    # Initialize a Mammal object with species, diet and fur_color attributes
    def __init__(self, species, diet, fur_color):
        super().__init__('Mammal', diet)
        self.fur_color = fur_color


# Define the Bird subclass of Animal
class Bird(Animal):
    # Initialize a Bird object with species, diet and wing_span attributes
    def __init__(self, species, diet, wing_span):
        super().__init__('Bird', diet)
        self.wing_span = wing_span


if __name__ == '__main__':
    # Create an Animal object
    animal = Animal('Generic Animal', 'Omnivore')
    print(f'Species: {animal.species}, Diet: {animal.diet}')

    # Create a Mammal object
    mammal = Mammal('Tiger', 'Carnivore', 'Orange')
    print(f'''Species: {mammal.species},
            Diet: {mammal.diet},
            Fur Color: {mammal.fur_color}''')

    # Create a Bird object
    bird = Bird('Eagle', 'Carnivore', '7 feet')
    print(f'''Species: {bird.species},
            Diet: {bird.diet},
            Wing Span: {bird.wing_span}''')
