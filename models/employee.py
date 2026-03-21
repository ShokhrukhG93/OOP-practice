class Employee:
    """Represents an employee with basic attributes and actions"""

    def __init__(self, name: str, employee_id: int, department: str, salary: float) -> None:
        """
        Initialize an Employee object.

        Args:
            name (str): The full name of the employee (e.g., 'John Smith').
            employee_id (int): The unique identifier of the employee (e.g., 101).
            department (str): The department of the employee (e.g., 'Engineering').
            salary (float): The salary of the employee (e.g., 50000.00).
        """
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary


    def promote(self) -> None:
        """Method to promote an employee."""
        print(f'{self.name} has been promoted.')

    def transfer(self, new_department: str) -> None:
        """
        Method to transfer an employee to a new department.
        
        Args:
            new_department (str): The name of the department where an employee has
            been transferred.
        """
        self.department = new_department
        print(f'{self.name} has been transferred to {self.department}.')
    
    def give_raise(self, amount: float) -> None:
        """Method to give an employee a raise."""
        self.salary += amount
        print(f'New salary of {self.name} is ${self.salary}.')
    
    def __repr__(self) -> str:
        """Return a string representation of the Employee object."""
        return (
            f'Employee: {self.name}, ID: {self.employee_id}, '
            f'Department: {self.department}, Salary: {self.salary}'
        )
