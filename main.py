"""Main module for the Library Management System.

This is the entry point for the Library Management System CLI application.
It provides an interactive menu for managing books, members, and loans.
"""

from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("   LIBRARY MANAGEMENT SYSTEM".center(50))
    print("="*50)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")
    print("="*50)


def add_book(service):
    """Handle adding a new book.
    
    Args:
        service (LibraryService): The library service instance
    """
    print("\n--- Add Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Book Title: ").strip()
        author = input("Enter Book Author: ").strip()
        
        if not book_id or not title or not author:
            print("Error: All fields are required.")
            return
        
        message = service.add_book(book_id, title, author)
        print(f"✓ {message}")
    except Exception as e:
        print(f"Error: {e}")


def register_member(service):
    """Handle registering a new member.
    
    Args:
        service (LibraryService): The library service instance
    """
    print("\n--- Register Member ---")
    try:
        member_id = input("Enter Member ID: ").strip()
        name = input("Enter Member Name: ").strip()
        email = input("Enter Member Email: ").strip()
        
        if not member_id or not name or not email:
            print("Error: All fields are required.")
            return
        
        message = service.register_member(member_id, name, email)
        print(f"✓ {message}")
    except Exception as e:
        print(f"Error: {e}")


def borrow_book(service):
    """Handle borrowing a book.
    
    Args:
        service (LibraryService): The library service instance
    """
    print("\n--- Borrow Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        if not book_id or not member_id:
            print("Error: All fields are required.")
            return
        
        message = service.borrow_book(book_id, member_id)
        print(f"✓ {message}")
    except BookNotFoundError as e:
        print(f"✗ Error: {e}")
    except MemberNotFoundError as e:
        print(f"✗ Error: {e}")
    except BookUnavailableError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Error: {e}")


def return_book(service):
    """Handle returning a book.
    
    Args:
        service (LibraryService): The library service instance
    """
    print("\n--- Return Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        if not book_id or not member_id:
            print("Error: All fields are required.")
            return
        
        message = service.return_book(book_id, member_id)
        print(f"✓ {message}")
    except BookNotFoundError as e:
        print(f"✗ Error: {e}")
    except MemberNotFoundError as e:
        print(f"✗ Error: {e}")
    except LoanNotFoundError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Error: {e}")


def view_books(service):
    """Handle viewing all books.
    
    Args:
        service (LibraryService): The library service instance
    """
    print("\n--- View Books ---")
    books = service.view_books()
    
    if not books:
        print("No books found.")
        return
    
    print("Books:")
    for book in books:
        print(f"  {book}")


def view_members(service):
    """Handle viewing all members.
    
    Args:
        service (LibraryService): The library service instance
    """
    print("\n--- View Members ---")
    members = service.view_members()
    
    if not members:
        print("No members found.")
        return
    
    print("Members:")
    for member in members:
        print(f"  {member}")


def view_loans(service):
    """Handle viewing all loans.
    
    Args:
        service (LibraryService): The library service instance
    """
    print("\n--- View Loans ---")
    loans = service.view_loans()
    
    if not loans:
        print("No loans found.")
        return
    
    print("Loans:")
    for loan in loans:
        print(f"  {loan}")


def main():
    """Main function to run the Library Management System."""
    service = LibraryService()
    
    print("\nWelcome to the Library Management System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            add_book(service)
        elif choice == "2":
            register_member(service)
        elif choice == "3":
            borrow_book(service)
        elif choice == "4":
            return_book(service)
        elif choice == "5":
            view_books(service)
        elif choice == "6":
            view_members(service)
        elif choice == "7":
            view_loans(service)
        elif choice == "8":
            print("\nProgram closed.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
