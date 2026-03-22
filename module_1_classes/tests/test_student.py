import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        """Create a test student before each test."""
        self.student = Student('Jack Smith', 201, 'Computer Science', 3.5, 'Senior')

    def test_attributes(self) -> None:
        """Test that attributes are set correctly."""
        self.assertEqual(self.student.name, 'Jack Smith')
        self.assertEqual(self.student.student_id, 201)
        self.assertEqual(self.student.major, 'Computer Science')
        self.assertEqual(self.student.gpa, 3.5)
        self.assertEqual(self.student.year, 'Senior')

    def test_repr(self) -> None:
        """Test the string representation of the student."""
        self.assertEqual(repr(self.student), f'Name: Jack Smith, ID: 201, '
                                             f'Major: Computer Science, GPA: 3.5, '
                                             f'Year: Senior.')

    def test_enroll_course(self) -> None:
        """Test that enroll_course() prints a correct message."""
        with redirect_stdout(StringIO()) as captured:
            self.student.enroll_course('Math')
        self.assertEqual(captured.getvalue().strip(),
                         'Jack Smith enrolled in the course Math.')

    def test_update_gpa(self) -> None:
        """Test that update_gpa() updates the GPA and prints a correct message."""
        with redirect_stdout(StringIO()) as captured:
            self.student.update_gpa(1.5)
        self.assertEqual(self.student.gpa, 1.5)
        self.assertEqual(captured.getvalue().strip(),
                         'New GPA of Jack Smith is 1.5.')

    def test_graduate(self) -> None:
        """Test that graduate() prints correct message when requirements are met."""
        with redirect_stdout(StringIO()) as captured:
            self.student.graduate()
        self.assertEqual(captured.getvalue().strip(),
                         'Jack Smith has graduated!')

    def test_graduate_fail(self) -> None:
        """Test that graduate() prints correct message when requirements are not met."""
        self.student.gpa = 1.5
        with redirect_stdout(StringIO()) as captured:
            self.student.graduate()
        self.assertEqual(captured.getvalue().strip(),
                         'Jack Smith has not met the graduation requirements.')


if __name__ == '__main__':
    unittest.main()
