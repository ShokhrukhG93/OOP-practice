class Car:
    """Represents a car with engine control functionality."""

    def __init__(self, make: str, model: str) -> None:
        """
        Initialize a Car object.

        Args:
            make (str): The manufacturer of the car (e.g., 'Toyota').
            model (str): The model of the car (e.g., 'Camry').
        """
        self.make = make
        self.model = model
        self.__engine_running = False

    def start_engine(self) -> None:
        """Start the engine if it is not already running."""
        if not self.__engine_running:
            self.__engine_running = True
            print(f'{self.make} {self.model} engine started.')
        else:
            print(f'{self.make} {self.model} engine is already running.')

    def stop_engine(self) -> None:
        """Stop the engine if it is running."""
        if self.__engine_running:
            self.__engine_running = False
            print(f'{self.make} {self.model} engine stopped.')
        else:
            print(f'{self.make} {self.model} engine is not running.')

    @property
    def engine_running(self) -> bool:
        """Return the current state of the engine."""
        return self.__engine_running


if __name__ == '__main__':
    car = Car('Toyota', 'Camry')

    car.start_engine()
    print(f'Is engine running? {car.engine_running}')
    car.stop_engine()
