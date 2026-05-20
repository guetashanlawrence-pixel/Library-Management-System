"""LibraryService class for managing library operations."""

from book import Book
from member import Member
from loan import Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


class LibraryService:
    """Service class to manage library operations.
    
    Manages books, members, and loans in the library system.
    """
    
    def __init__(self):
        """Initialize the LibraryService.
        
        Creates empty dictionaries for books and members,
        and an empty list for loans.
        """
        self._books = {}  # Key: book_id, Value: Book object
        self._members = {}  # Key: member_id, Value: Member object
        self._loans = []  # List of Loan objects
        self._loan_counter = 0  # Counter for generating loan IDs
    
    # ================= BOOK OPERATIONS =================
    
    def add_book(self, book_id, title, author):
        """Add a new book to the library.
        
        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
        
        Returns:
            str: Success message
        """
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return f"Book added: {title}"
    
    def view_books(self):
        """View all books in the library.
        
        Returns:
            list: List of all Book objects
        """
        return list(self._books.values())
    
    # ================= MEMBER OPERATIONS =================
    
    def register_member(self, member_id, name, email):
        """Register a new member in the library.
        
        Args:
            member_id (str): Unique identifier for the member
            name (str): Name of the member
            email (str): Email address of the member
        
        Returns:
            str: Success message
        """
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return f"Member registered: {name}"
    
    def view_members(self):
        """View all registered members.
        
        Returns:
            list: List of all Member objects
        """
        return list(self._members.values())
    
    # ================= LOAN OPERATIONS =================
    
    def borrow_book(self, book_id, member_id):
        """Borrow a book for a member.
        
        Args:
            book_id (str): ID of the book to borrow
            member_id (str): ID of the member borrowing the book
        
        Returns:
            str: Success message
        
        Raises:
            BookNotFoundError: If the book is not found
            MemberNotFoundError: If the member is not found
            BookUnavailableError: If the book is not available
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        
        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
        
        # Check if book is available
        if not book.available:
            raise BookUnavailableError("Book is already borrowed.")
        
        # Mark book as borrowed
        book.borrow()
        
        # Create loan record
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return f"{member.name} borrowed {book.title}"
    
    def return_book(self, book_id, member_id):
        """Return a borrowed book.
        
        Args:
            book_id (str): ID of the book being returned
            member_id (str): ID of the member returning the book
        
        Returns:
            str: Success message
        
        Raises:
            BookNotFoundError: If the book is not found
            MemberNotFoundError: If the member is not found
            LoanNotFoundError: If no active loan is found for this book and member
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        
        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
        
        # Find active loan
        active_loan = None
        for loan in self._loans:
            if (loan.book.book_id == book_id and 
                loan.member.member_id == member_id and 
                loan.is_active):
                active_loan = loan
                break
        
        if active_loan is None:
            raise LoanNotFoundError("No active loan found for this book and member.")
        
        # Mark book as returned and close loan
        book.return_book()
        active_loan.return_loan()
        
        return f"{member.name} returned {book.title}"
    
    def view_loans(self):
        """View all loans.
        
        Returns:
            list: List of all Loan objects
        """
        return list(self._loans)
