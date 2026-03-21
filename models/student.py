# Your Code Here
class Student:
    """Represents a student with basic attributes and actions."""

    def __init__(self, name: str, student_id: int, major: str, gpa: float, year: str) -> None:
        """
        Initialize a student object.
        
        Args:
            name (str): The full name of the student (e.g., 'John Smith').
            student_id (int): The unique identifier of the student (e.g. 101).
            major (str): The major field of study of the student (e.g., 'Computer Science').
            gpa (float): The grade point average of the student (e.g., 3.8).
            year (str): The year of study of the student (e.g., 'Senior')..
        """
        self.name = name
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
        self.year = year
    
    def __repr__(self) -> str:
        """Return a string representation of the Student object."""
        return (
            f'Name: {self.name}, ID: {self.student_id}, '
            f'Major: {self.major}, GPA: {self.gpa}, '
            f'Year: {self.year}.'
        )

    def enroll_course(self, course_name: str) -> None:
        """
        Method to enroll a student in a course.
        
        Args:
            course_name (str): The name of the course to enroll in (e.g., 'Data Structures').
        """
        print(f'{self.name} enrolled in the course {course_name}.')
    
    def update_gpa(self, new_gpa: float) -> None:
         """Method to update the student's GPA."""
         self.gpa = new_gpa
         print(f'New GPA of {self.name} is {self.gpa}.')

    def graduate(self) -> None:
        """Method to check if a student has met the graduation requirements."""
        if self.year == 'Senior' and self.gpa >= 2.0:
            print(f'{self.name} has graduated!')
        else:
            print(f'{self.name} has not met the graduation requirements.')
