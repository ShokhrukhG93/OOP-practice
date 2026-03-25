class Book:
    def __init__(self, title: str, number_of_pages: int | None) -> None:
        """
        Initialize a Book object.

        Args:
            title (str): The title of the book (e.g., 'Python Programming').
            number_of_pages (int | None): The initial number of pages.
                If None, the number of pages is considered not set.
        """
        self.title = title
        self.__pages = number_of_pages

    def add_pages(self, amount: int) -> None:
        """
        Increase the number of pages in the book.

        Args:
            amount (int): Number of pages to add (must be positive).

        Raises:
            ValueError: If the number of pages is not set or amount is not positive.
        """
        if self.__pages is None:
            raise ValueError("Number of pages is not set.")

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.__pages += amount
        print(
            f"{self.title}: pages increased by {amount}. "
            f"New total pages: {self.__pages}."
        )

    def get_pages(self) -> int | None:
        """
        Get the current number of pages in the book.

        Returns:
            int | None: The number of pages or None if not set.
        """
        return self.__pages


if __name__ == '__main__':
    # Create a Book object
    book = Book('Python Programming', 300)

    # Adding pages
    book.add_pages(50)

    # Getting the number of pages
    print(f'Number of pages: {book.get_pages()}')
