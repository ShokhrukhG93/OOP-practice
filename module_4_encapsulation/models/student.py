class Student:
    """Represents a student with a name and grades."""

    def __init__(self, name: str, grades: list = None) -> None:
        """
        Initialize a Student object.

        Args:
            name (str): The full name of the student (e.g., 'John Smith').
            grades (list): The list of grades (default: None).
        """
        self.name = name
        self.__grades = grades if grades is not None else []

    def add_grade(self, grade: int) -> None:
        """
        Add a grade to the student's grades.

        Args:
            grade (int): The grade to add, must be between 0 and 100.
        """
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f'Grade {grade} added.')
        else:
            print('Invalid grade.')

    @property
    def grades(self) -> list:
        """Return the list of grades."""
        return self.__grades

    @property
    def average_grade(self) -> float:
        """Return the average grade of the student."""
        return sum(self.__grades) / len(self.__grades) if self.__grades else 0


if __name__ == '__main__':
    student = Student('John')

    student.add_grade(85)
    student.add_grade(92)

    print(f'Grades: {student.grades}')
    print(f'Average Grade: {student.average_grade}')
