from abc import ABC, abstractmethod


class Person(ABC):
    """
    Abstract class representing a person at the University.

    Attributes
    ----------
    name : str
        The person's name.
    age : int
        The person's age.
    """

    # Constructor to initialize the Person class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__ssn = None  # Encapsulated attribute

    # Abstract method to return the role of the person
    @abstractmethod
    def get_role(self):
        """
        Abstract method to return the role of the person.
        """
        pass

    # Method to set the Social Security Number
    def set_ssn(self, ssn):
        """
        Sets the Social Security Number.

        Parameters
        ----------
        ssn : str
            The social security number.
        """
        self.__ssn = ssn

    # Method to get the Social Security Number
    def get_ssn(self):
        """
        Gets the Social Security Number.

        Returns
        -------
        str
            The social security number.
        """
        return f'SSN: {self.__ssn}'

# Define a concrete class Student inheriting from Person
class Student(Person):
    """
    Represents a student at the university.
    """
    
    # Constructor to initialize the Student class
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    
    # Implementation of the get_role abstract method
    def get_role(self):
        return f'Student majoring in {self.major}.'

# Define a concrete class Professor inheriting from Person
class Professor(Person):
    """
    Represents a professor at the university.
    """ 

    # Constructor to initialize the Professor class
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    # Implementation of the get_role abstract method
    def get_role(self):
        return f'Professor in the {self.department} department.'

# Define a concrete class Staff inheriting from Person
class Staff(Person):
    """
    Represents a staff member at the university.
    """

    # Constructor to initialize the Staff class
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    # Implementation of the get_role abstract method
    def get_role(self):
        return f'Staff member working as {self.position}'
    

if __name__ == '__main__':
    john = Student('John Due', 20, 'Computer Science')
    john.set_ssn('123-45-6789')
    print(john.get_role()) # Polymorphism
    print(john.get_ssn()) # Encapsulation

    dr_smith = Professor('Dr. Smith', 45, 'Mathematics')
    dr_smith.set_ssn('234-56-7890')
    print(dr_smith.get_ssn())
    print(dr_smith.get_role())

    jane = Staff('Jane Dae', 35, 'Administrator')
    jane.set_ssn('123-67-8901')
    print(jane.get_ssn())
    print(jane.get_role())
