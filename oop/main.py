from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    # Uses __str__
    print(my_book)

    # Uses __repr__
    print(repr(my_book))

    # Trigger __del__
    del my_book

if __name__ == "__main__":
    main()
