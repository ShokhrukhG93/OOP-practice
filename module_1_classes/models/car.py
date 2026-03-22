class Car:
    """Represents a car with basic attributes and actions."""

    def __init__(self, make: str, model: str, year: int, color: str) -> None:
        """
        Initialize a Car object.

        Args:
            make (str): The manufacturer of the car (e.g., 'Toyota').
            model (str): The model of the car (e.g., 'Corolla').
            year (int): The year the car was made (e.g., 2020).
            color (str): The color of the car (e.g., 'red').
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def start(self) -> None:
        """Print a message indicating the car is starting."""
        print(f'The {self.color} {self.make} {self.model} is starting.')

    def stop(self) -> None:
        """Print a message indicating the car is stopping."""
        print(f'The {self.color} {self.make} {self.model} is stopping.')

    def drive(self) -> None:
        """Print a message indicating the car is driving."""
        print(f'The {self.color} {self.make} {self.model} is driving.')

    def __repr__(self) -> str:
        """Return a string representation of the Car object."""
        return f'I am a {self.color} {self.make} {self.model} car!'
