class Animal:
    """Represents an animal with basic actions."""

    def speak(self) -> None:
        """Print a default sound for an animal."""
        print("Make some noise and I don't know what it sounds like...")


class Cat(Animal):
    """Represents a cat, inheriting from Animal."""

    def speak(self) -> None:
        """Print the sound a cat makes."""
        print('Meo')


class Lion(Animal):
    """Represents a lion, inheriting from Animal."""

    def speak(self) -> None:
        """Print the sound a lion makes."""
        print('AHHHHHH!')


class LionBaby(Lion):
    """Represents a baby lion, inheriting from Lion."""

    def speak(self) -> None:
        """Print the sound a baby lion makes."""
        print("I'm the king of the world!")


if __name__ == '__main__':
    a = Animal()
    c = Cat()
    l = Lion()
    lb = LionBaby()

    a.speak()
    c.speak()
    l.speak()
    lb.speak()
