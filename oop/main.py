from library_system import Book, EBook, PrintBook, Library, Bank

def main():
    # Library Demo
    library = Library()
    library.add_book(Book("Pride and Prejudice", "Jane Austen"))
    library.add_book(EBook("Snow Crash", "Neal Stephenson", 500))
    library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 234))

    print("Library Books:")
    library.list_books()

    # Bank Demo
    bank = Bank()
    bank.create_account("Alice", 100)
    bank.deposit("Alice", 50)
    bank.withdraw("Alice", 30)
    print("\nBank Balance for Alice:", bank.check_balance("Alice"))

if __name__ == "__main__":
    main()
