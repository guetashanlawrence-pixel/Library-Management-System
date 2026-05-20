"""Loan class for the Library Management System."""

from datetime import datetime


class Loan:
    """Represents a loan transaction in the library.
    
    Attributes:
        loan_id (str): Unique identifier for the loan
        book (Book): The book object being borrowed
        member (Member): The member object borrowing the book
        date_borrowed (datetime): Date when the book was borrowed
        date_returned (datetime): Date when the book was returned (None if active)
        is_active (bool): Whether the loan is still active
    """
    
    def __init__(self, loan_id, book, member):
        """Initialize a Loan object.
        
        Args:
            loan_id (str): Unique identifier for the loan
            book (Book): The book object being borrowed
            member (Member): The member object borrowing the book
        """
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.date_borrowed = datetime.now()
        self.date_returned = None
        self.is_active = True
    
    def return_loan(self):
        """Mark the loan as returned.
        
        Sets is_active to False and records return date.
        """
        self.date_returned = datetime.now()
        self.is_active = False
    
    def __str__(self):
        """String representation of the loan.
        
        Returns:
            str: Loan information
        """
        status = "Active" if self.is_active else "Closed"
        return f"{self.loan_id} - {self.member.name} borrowed {self.book.title} [{status}]"
    
    def __repr__(self):
        """Official string representation.
        
        Returns:
            str: Loan representation
        """
        return f"Loan({self.loan_id!r}, {self.book!r}, {self.member!r}, is_active={self.is_active})"
