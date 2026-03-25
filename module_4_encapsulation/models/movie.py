class Movie:
    def __init__(self, title: str, rating: float | None) -> None:
        """
        Initialize a Movie object.

        Args:
            title (str): The title of the movie (e.g., 'Inception').
            rating (float | None): The initial rating of the movie (0 to 10).
                If None, rating is considered not set.
        """
        self.title = title
        self.__rating = rating

    def set_rating(self, new_rating: float) -> None:
        """
        Update the movie rating.

        Args:
            new_rating (float): New rating value (must be between 0 and 10).

        Raises:
            ValueError: If new_rating is outside the valid range.
        """
        if not (0 <= new_rating <= 10):
            raise ValueError("Rating must be between 0 and 10.")

        self.__rating = new_rating
        print(f"New rating for {self.title}: {self.__rating}")

    def get_rating(self) -> float | None:
        """
        Get the current movie rating.

        Returns:
            float | None: The current rating or None if not set.
        """
        return self.__rating


if __name__ == '__main__':
    # Create a Movie object
    movie = Movie('Inception', 9)

    # Updating the rating using public method
    movie.set_rating(10)

    # Getting the rating using a public method
    print(f'Current rating: {movie.get_rating()}')
