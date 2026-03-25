class Grandparent:
    """Represents a grandparent."""

    def speak(self) -> None:
        """Print a message from the grandparent."""
        print('Grandparent says, "Back in my day..."')


class Parent(Grandparent):
    """Represents a parent."""

    def speak(self) -> None:
        """Print a message from the parent."""
        print('Parent says, "When I was your age..."')


class Child(Parent):
    """Represents a child."""

    def speak(self) -> None:
        """Print a message from the child."""
        print('Child says, "Can I have some money?"')


class Grandchild(Child):
    """Represents a grandchild."""

    def speak(self) -> None:
        """Print a message from the grandchild."""
        print('Grandchild says, "I love my Lego set!"')


if __name__ == '__main__':
    grandparent = Grandparent()
    parent = Parent()
    child = Child()
    grandchild = Grandchild()

    for person in (grandparent, parent, child, grandchild):
        person.speak()