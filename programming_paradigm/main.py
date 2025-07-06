from libaray_management import Book, Library

def main():
    Library = Library()
    Library.add_book(Book("Brave New World", "Aldous Huxley"))
    Library.add_book(Book("1984", "George Orwell"))

    print("Available books after setup:")
    Library.list_available_books()

    Library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    Library.list_available_books()

    Library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    Library.list_available_books()

    if __name__ == "__main__":
        main()