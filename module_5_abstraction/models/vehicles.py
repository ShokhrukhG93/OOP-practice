# Import ABC and abstractmethod from the abc module
from abc import ABC, abstractmethod

# Define an abstract base class Vehicle
class Vehicle(ABC):
  # Abstract method start_engine, which must be implemented by any subclass
  @abstractmethod
  def start_engine(self):
    pass

  # Abstract method stop_engine, which must be implemented by any subclass
  @abstractmethod
  def stop_engine(self):
    pass

  # Concrete method honk with a default implementation
  def honk(self):
    print('Honking!')

# Define a concrete class Car inheriting from Vehicle
class Car(Vehicle):
  # Implementation of the start_engine abstract method
  def start_engine(self):
    print('Car engine started.')

  # Implementation of the stop_engine abstract method
  def stop_engine(self):
    print('Car engine stopped.')

# Define a concrete class Motorcycle inheriting from Vehicle
class Motorcycle(Vehicle):
  # Implementation of the start_engine abstract method
  def start_engine(self):
    print('Motorcycle engine started.')

  # Implementation of the stop_engine abstract method
  def stop_engine(self):
    print('Motorcycle engine stopped.')

# Instantiate objects and use abstract methods
my_car = Car()
my_car.start_engine()  # Output: Car engine started.
my_car.honk()          # Output: Honking!
my_car.stop_engine()   # Output: Car engine stopped.

my_motorcycle = Motorcycle()
my_motorcycle.start_engine()  # Output: Motorcycle engine started.
my_motorcycle.honk()          # Output: Honking!
my_motorcycle.stop_engine()   # Output: Motorcycle engine stopped.x`x`
