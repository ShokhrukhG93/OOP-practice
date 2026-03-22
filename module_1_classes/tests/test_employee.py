import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        """Create a test employee before each test."""
        self.employee = Employee('John', 50, 'Engineering', 5000.0)

    def test_attributes(self) -> None:
        """Test that attributes are set correctly."""
        self.assertEqual(self.employee.name, 'John')
        self.assertEqual(self.employee.employee_id, 50)
        self.assertEqual(self.employee.department, 'Engineering')
        self.assertEqual(self.employee.salary, 5000.0)
    
    def test_repr(self) -> None:
        """Test the string representation of the employee."""
        self.assertEqual(repr(self.employee), f'Employee: John, ID: 50, '
                                              f'Department: Engineering, Salary: 5000.0')
    
    def test_promote(self) -> None:
        """Test the promote prints a correct message."""
        with redirect_stdout(StringIO()) as captured:
            self.employee.promote()
        self.assertEqual(captured.getvalue().strip(), 'John has been promoted.')

    def test_transfer(self) -> None:
        """
        Test the transfer() changes the name of the department
        and prints a correct message.
        """
        with redirect_stdout(StringIO()) as captured:
            self.employee.transfer('IT')
        self.assertEqual(self.employee.department, 'IT')
        self.assertEqual(captured.getvalue().strip(), 'John has been transferred to IT.')

    def test_give_raise(self) -> None:
        """
        Test the give_raise() changes the amount of the salary
        and prints a correct message.
        """
        with redirect_stdout(StringIO()) as captured:
            self.employee.give_raise(500.0)
        self.assertEqual(self.employee.salary, 5500.0)
        self.assertEqual(captured.getvalue().strip(), 'New salary of John is $5500.0.')


if __name__ == "__main__":
    unittest.main()
    