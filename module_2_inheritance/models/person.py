# Define the Person class
class Person:
    # Initialize a Person object with name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

# Define the Student class
class Student(Person):
    # Initialize a Student object with name, age and student_id
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


if __name__ == "__main__":
    person1 = Person('John', 25)
    print(f'Person Name: {person1.name}, Age: {person1.age}')

    student1 = Student('Jack', 30, 10001)
    print(f"""Student Name: {student1.name}
          Age: {student1.age}
          Student ID: {student1.student_id}""")

