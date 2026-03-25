class E:
    """Demonstrates encapsulation with public, protected, and private attributes."""

    def __init__(self) -> None:
        """Initialize E object with public, protected, and private attributes."""
        self.att1 = 1
        self._att2 = 2
        self.__att3 = 3

    @property
    def att2(self) -> int:
        """Return the protected attribute _att2."""
        return self._att2

    @att2.setter
    def att2(self, v: int) -> None:
        """Set the protected attribute _att2."""
        print(f'The original value {self._att2} will be changed to {v}')
        self._att2 = v

    @property
    def att3(self) -> int:
        """Return the private attribute __att3."""
        print('I am a private attribute!')
        return self.__att3

    @att3.setter
    def att3(self, v: int) -> None:
        """Set the private attribute __att3."""
        print(f'The original value {self.__att3} will be changed to {v}')
        self.__att3 = v


if __name__ == '__main__':
    e = E()

    print('Original values.')
    print(e.att1)
    print(e.att2)
    print(e.att3)

    print('We are changing the values.')
    e.att1 = 4
    e.att2 = 5
    e.att3 = 6

    print('We are printing the changed values.')
    print(e.att1)
    print(e.att2)
    print(e.att3)