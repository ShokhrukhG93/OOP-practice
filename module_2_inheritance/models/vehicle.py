# Define the Vehicle class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


# Define the Car SubClass of Vehicle class
class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors


# Define the Truck SubClass of Vehicle class
class Truck(Vehicle):
    def __init__(self, make, model, cargo_capacity):
        super().__init__(make, model)
        self.cargo_capacity = cargo_capacity


if __name__ == '__main__':
    # Create a Vehicle object
    vehicle = Vehicle('Generic Make', 'Generic Model')
    print(f'Make: {vehicle.make}, Model: {vehicle.model}')

    # Create a Car object
    car = Car('Honda', 'Civic', 4)
    print(f'''Make: {car.make}, Model: {car.model},
            Number of Doors: {car.number_of_doors}''')

    # Create a Truck object
    truck = Truck('Ford', 'F-150', '1000 lbs')
    print(f'''Make: {truck.make}, Model: {truck.model},
            Cargo Capacity: {truck.cargo_capacity}''')
