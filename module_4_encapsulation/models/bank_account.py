class BankAccount:
    """Represents a bank account with basic attributes and actions."""

    def __init__(self, owner: str, balance: float = 0) -> None:
        """
        Initialize a BankAccount object.

        Args:
            owner (str): The name of the account owner (e.g., 'Alice').
            balance (float): The initial balance of the account (default: 0).
        """
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self) -> float:
        """Return the current balance of the account."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        """
        Deposit an amount to the account.

        Args:
            amount (float): The amount to deposit (e.g., 500.0).
        """
        if amount > 0:
            self.__balance += amount
            print(f'{amount} deposited. New balance {self.__balance}.')
        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount: float) -> None:
        """
        Withdraw an amount from the account.

        Args:
            amount (float): The amount to withdraw (e.g., 200.0).
        """
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f'{amount} withdrawn. New balance {self.__balance}.')
        else:
            print('Insufficient balance or invalid withdrawal amount.')


if __name__ == '__main__':
    account = BankAccount('Alice', 1000)

    print(account.owner)

    account.deposit(500)
    account.withdraw(200)

    print(f'Current balance: {account.balance}')