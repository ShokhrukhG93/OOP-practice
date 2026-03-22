import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.smartphone import Smartphone


class TestSmartphone(unittest.TestCase):

    def setUp(self) -> None:
        """Creare a test smartphone before each test."""
        self.smartphone = Smartphone('Apple', 'Iphone 17 pro max', 512, 'Black', 1750.0)

    def test_attributes(self) -> None:
        """Test that attributes are set correctly."""
        self.assertEqual(self.smartphone.brand, 'Apple')
        self.assertEqual(self.smartphone.model, 'Iphone 17 pro max')
        self.assertEqual(self.smartphone.storage, 512)
        self.assertEqual(self.smartphone.color, 'Black')
        self.assertEqual(self.smartphone.price, 1750.0)

    def test_repr(self) -> None:
        """Test the string representation of the smartphone."""
        self.assertEqual(repr(self.smartphone), f'Brand: Apple, Model: Iphone 17 pro max, '
                                                f'Storage: 512, Color: Black, '
                                                f'Price: 1750.0.')

    def test_make_call(self) -> None:
        """Test the make_call() print a correct message."""
        with redirect_stdout(StringIO()) as captured:
            self.smartphone.make_call('+99899 000-00-01')
        self.assertEqual(captured.getvalue().strip(), f'Apple Iphone 17 pro max '
                                                      f'is calling +99899 000-00-01.')


if __name__ == "__main__":
    unittest.main()