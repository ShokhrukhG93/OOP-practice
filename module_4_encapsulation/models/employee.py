class Employee:
    def __init__(self, name: str, salary: float | None = None) -> None:
        """
        Initialize an Employee object.

        Args:
            name (str): The name of the employee (e.g., 'Jack Smith').
            salary (float | None): The initial salary of the employee (e.g., 10000.0).
                If None, salary is considered not set.
        """
        self.name = name
        self.__salary = salary

    def give_raise(self, amount: float = 0) -> None:
        """
        Increase the employee's salary by a given amount.

        Args:
            amount (float): The raise amount (must be positive).

        Raises:
            ValueError: If salary is not set or amount is not positive.
        """
        if self.__salary is None:
            raise ValueError("Salary is not set.")

        if amount <= 0:
            raise ValueError("Raise amount must be positive.")

        self.__salary += amount
        print(f"{self.name}'s salary increased by {amount}. New salary: {self.__salary}.")

    def get_salary(self) -> None:
        """
        Get the current salary of the employee.

        Returns:
            float | None: The current salary or None if not set.
        """
        print(f'New salary: {self.__salary}')


if __name__ == "__main__":
    employee = Employee("Jack Smith", 10000.0)

    employee.give_raise(1000.0)

    employee.get_salary()
