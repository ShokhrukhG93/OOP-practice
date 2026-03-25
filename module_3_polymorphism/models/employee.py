class Employee:
    def get_pay(self):
        return 'Generic employee pay'
    

class FullTimeEmployee(Employee):
    def get_pay(self):
        return 'Full time employee'
    

class PartTimeEmployee(Employee):
    def get_pay(self):
        return 'Part time employee'
