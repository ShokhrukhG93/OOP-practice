# Import ABC and abstractmethod from the abc module
from abc import ABC, abstractmethod


# Define an abstract base class Payment
class Payment(ABC):
    # Abstract method must be iplemented by any subclass
    @abstractmethod
    def process_payment(self, amount):
        pass


# Define a concrete class CreditCardPayment inheriting from Payment
class CreditCardPayment(Payment):
    # Implementation of the process_payment abstract method
    def process_payment(self, amount):
        print(f'Processing credit card payment of {amount} dollars.')


# Define a concrete class PayPalPayment inheriting from Payment
class PayPalPayment(Payment):
    # Implementation of the process_payment abstract method
    def process_payment(self, amount):
        print(f'Processing PayPal payment of {amount} dollars.')


# Using the abstract inference
# Create an instance of CreditCardPayment and call process_payment
payment_method = CreditCardPayment()
payment_method.process_payment(100)

# Create an instance of PayPalPayment and call process_payment
payment_method = PayPalPayment()
payment_method.process_payment(150)
