from models.car import Car

car1 = Car('Toyota', 'Corolla', 2020, 'red')
car2 = Car('Honda', 'Civic', 2019, 'blue')
car3 = Car('Tesla', 'Model S', 2024, 'silver')

available_cars = [car1, car2, car3]

for car in available_cars:
    print(car)
    car.start()
    car.stop()
    car.drive()
