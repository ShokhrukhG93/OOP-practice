from models.car import Car
from models.employee import Employee


car1 = Car('Toyota', 'Corolla', 2020, 'red')
car2 = Car('Honda', 'Civic', 2019, 'blue')
car3 = Car('Tesla', 'Model S', 2024, 'silver')

available_cars = [car1, car2, car3]

for car in available_cars:
    print(car)
    car.start()
    car.stop()
    car.drive()


emp1 = Employee('John Smith', 101, 'Engineering', 50000.0)
emp1.promote()
emp1.transfer('Management')
emp1.give_raise(5000.0)
print(emp1)
