class Vehicle:
    """Represents a vehicle with basic attributes and actions."""
    def __init__(self, make: str, model:str) -> None:
        """
        Initialize a vehicle object.

        Args:
            make (str): The manufacturer of the vehicle (e.g., 'Toyota').
            model (str): The model of the vehicle (e.g., 'Corolla').
        """
        self.make = make
        self.model = model

    def __repr__(self) -> str:
        """Return a string representation of the Vehicle object."""
        return f'The manufacture: {self.make}, the model: {self.model}.'

    def start(self) -> None:
        """Print a message indicating the vehicle is starting."""
        print(f'The {self.make} {self.model} is starting.')
    
    def stop(self) -> None:
        """Print a message indicating the vehicle is stopping."""
        print(f'The {self.make} {self.model} is stopping.')

    def drive(self) -> None:
        """Print a message indicating the vehicle is driving."""
        print(f'The {self.make} {self.model} is driving.')

    def fuel_type(self) -> str:
        """Return the string representation of fuel type"""
        return 'Gasoline'


# Define the Car SubClass of Vehicle class
class Car(Vehicle):
    """Represents a car."""
    def __init__(self, make: str, model: str, number_of_doors: int) -> None:
        """
        Initialize a car object.

        Args:
            make (str): The manufacturer of the vehicle (e.g., 'Toyota').
            model (str): The model of the vehicle (e.g., 'Corolla').
            number_of_doors (int): The number of doors of the car (e.g., 4)
        """
        super().__init__(make, model)
        self.number_of_doors = number_of_doors
    
    def __repr__(self) -> str:
        """Return a string representation of the Car object."""
        return f'{self.make} {self.model} has {self.number_of_doors} doors.'


# Define the Truck SubClass of Vehicle class
class Truck(Vehicle):
    """Represents a truck."""
    def __init__(self, make: str, model: str, cargo_capacity: str) -> None:
        """
        Initialize a Truck object.

        Args:
            make (str): The manufacturer of the Truck (e.g., 'Toyota').
            model (str): The model of the Truck (e.g., 'Corolla').
            cargo_capacity (str): The cargo capacity of the Truck (e.g., 1000 lbs)
        """
        super().__init__(make, model)
        self.cargo_capacity = cargo_capacity

    def __repr__(self) -> str:
        """Return a string representation of the Truck object."""
        return f'{self.make} {self.model} has {self.cargo_capacity} cargo capacity.'


class ElectricCar(Car):
    """Represents an electric car."""
    
    def fuel_type(self) -> str:
        """Return the fuel type of the electric car."""
        return 'Electric'


if __name__ == '__main__':
    # Create a Vehicle object
    vehicle = Vehicle('Generic Make', 'Generic Model')
    print(f'Make: {vehicle.make}, Model: {vehicle.model}')
    print(vehicle)

    # Create a Car object
    car = Car('Honda', 'Civic', 4)
    print(f'Make: {car.make}, Model: {car.model}, '
          f'Number of Doors: {car.number_of_doors}')
    print(car)
    print(car.fuel_type())

    # Create a Truck object
    truck = Truck('Ford', 'F-150', '1000 lbs')
    print(f'Make: {truck.make}, Model: {truck.model}, '
          f'Cargo Capacity: {truck.cargo_capacity}')
    print(truck)
    print(truck.fuel_type())

    # Create an Electriccar object
    eletric_car = ElectricCar('Tesla', 'Model Y', 4)
    print(f'Make: {eletric_car.make}, Model: {eletric_car.model}')
    print(eletric_car)
    print(eletric_car.fuel_type())

    print(ElectricCar.__mro__)
