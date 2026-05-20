"""Book class for the Library Management System."""


class Book:
    """Represents a book in the library.
    
    Attributes:
        book_id (str): Unique identifier for the book
        title (str): Title of the book
        author (str): Author of the book
        available (bool): Whether the book is available for borrowing
    """
    
    def __init__(self, book_id, title, author):
        """Initialize a Book object.
        
        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True  # Books are available by default
    
    def borrow(self):
        """Mark the book as borrowed.
        
        Sets available to False.
        """
        self.available = False
    
    def return_book(self):
        """Mark the book as returned.
        
        Sets available to True.
        """
        self.available = True
    
    def __str__(self):
        """String representation of the book.
        
        Returns:
            str: Book information
        """
        status = "Available" if self.available else "Borrowed"
        return f"{self.book_id} - {self.title} by {self.author} [{status}]"
    
    def __repr__(self):
        """Official string representation.
        
        Returns:
            str: Book representation
        """
        return f"Book({self.book_id!r}, {self.title!r}, {self.author!r}, available={self.available})"
