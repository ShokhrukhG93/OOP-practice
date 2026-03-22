class Vehicle:
    """Represetnts a vehicle with basic attributes and actions."""
    def __init__(self, make: str, model:str) -> None:
        """
        Initialize a vehicle object.

        Args:
            make (str): The manufacturer of the vehicle (e.g., 'Toyota').
            model (str): The model of the vehicle (e.g., 'Corolla').
        """
        self.make = make
        self.model = model

    def start(self) -> None:
        """Print a message indicating the vehicle is starting."""
        print(f'{self.make} {self.model} is starting.')
    
    def __repr__(self) -> str:
        """Return a string representation of the Vehicle object."""
        return f'This vehicle is {self.make} {self.model}'

    
# Define the Car SubClass of Vehicle class
class Car(Vehicle):
    """Represetnts a car with basic attributes and actions."""
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
    
    def __repr__(self):
        """Return a string representation of the Car object."""
        return f'{self.make} {self.model} has {self.number_of_doors} doors.'


# Define the Truck SubClass of Vehicle class
class Truck(Vehicle):
    """Represetnts a truck with basic attributes and actions."""
    def __init__(self, make: str, model: str, cargo_capacity: float) -> None:
        """
        Initialize a Truck object.

        Args:
            make (str): The manufacturer of the Truck (e.g., 'Toyota').
            model (str): The model of the Truck (e.g., 'Corolla').
            cargo_capacity (float): The cargo capacity of the Truck (e.g., 100)
        """
        super().__init__(make, model)
        self.cargo_capacity = cargo_capacity

    def __repr__(self):
        """Return a string representation of the Truck object."""
        return f'{self.make} {self.model} has {self.cargo_capacity} cargo capacity.'


if __name__ == '__main__':
    # Create a Vehicle object
    vehicle = Vehicle('Generic Make', 'Generic Model')
    print(f'Make: {vehicle.make}, Model: {vehicle.model}')
    print(vehicle)

    # Create a Car object
    car = Car('Honda', 'Civic', 4)
    print(f'''Make: {car.make}, Model: {car.model},
            Number of Doors: {car.number_of_doors}''')
    print(car)

    # Create a Truck object
    truck = Truck('Ford', 'F-150', '1000 lbs')
    print(f'''Make: {truck.make}, Model: {truck.model},
            Cargo Capacity: {truck.cargo_capacity}''')
    print(truck)
