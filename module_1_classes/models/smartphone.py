class Smartphone:
    """Represents a smartphone with basic attributes and actions."""

    def __init__(self, brand: str, model: str, storage: int,
                 color: str, price: float) -> None:
        """
        Initialize a Smartphone object.
        
        Args:
            brand (str): The manufacturer of the smartphone (e.g., 'Apple').
            model (str): The model of the smartphone (e.g., 'iPhone 15').
            storage (int): The storage capacity in GB (e.g., 128).
            color (str): The color of the smartphone (e.g., 'black').
            price (float): The price of the smartphone (e.g., 999.99).
        """
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color
        self.price = price

    def __repr__(self) -> str:
        """Return a string representation of the Smartphone object."""
        return (
            f'Brand: {self.brand}, Model: {self.model}, '
            f'Storage: {self.storage}, Color: {self.color}, '
            f'Price: {self.price}.'
        )
    
    def make_call(self, phone_number: str) -> None:
        """Method to simulate making a call on the smartphone."""
        print(f'{self.brand} {self.model} is calling {phone_number}.')
