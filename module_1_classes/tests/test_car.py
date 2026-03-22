import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.car import Car


class TestCar(unittest.TestCase):

    def setUp(self) -> None:
        """Create a test car before each test."""
        self.car = Car('Toyota', 'Corolla', 2020, 'red')

    def test_attributes(self) -> None:
        """Test that attributes are set correctly."""
        self.assertEqual(self.car.make, 'Toyota')
        self.assertEqual(self.car.model, 'Corolla')
        self.assertEqual(self.car.year, 2020)
        self.assertEqual(self.car.color, 'red')

    def test_repr(self) -> None:
        """Test the string representation of the car."""
        self.assertEqual(repr(self.car), 'I am a red Toyota Corolla car!')

    def test_start(self) -> None:
        """Test that start() prints the correct message."""
        with redirect_stdout(StringIO()) as captured:
            self.car.start()
        self.assertEqual(captured.getvalue().strip(),
                         'The red Toyota Corolla is starting.')

    def test_stop(self) -> None:
        """Test that stop() prints the correct message."""
        with redirect_stdout(StringIO()) as captured:
            self.car.stop()
        self.assertEqual(captured.getvalue().strip(),
                         'The red Toyota Corolla is stopping.')

    def test_drive(self) -> None:
        """Test that drive() prints the correct message."""
        with redirect_stdout(StringIO()) as captured:
            self.car.drive()
        self.assertEqual(captured.getvalue().strip(),
                         'The red Toyota Corolla is driving.')


if __name__ == '__main__':
    unittest.main()
