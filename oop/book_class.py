# book_class.py

class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize the Book object with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method to print a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a human-readable string representation of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns a formal string representation that can recreate the Book object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
