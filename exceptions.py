"""Custom exceptions for the Library Management System."""


class LibraryException(Exception):
    """Base exception for library-related errors."""
    pass


class BookNotFoundError(LibraryException):
    """Exception raised when a book is not found."""
    pass


class MemberNotFoundError(LibraryException):
    """Exception raised when a member is not found."""
    pass


class BookUnavailableError(LibraryException):
    """Exception raised when a book is already borrowed."""
    pass


class LoanNotFoundError(LibraryException):
    """Exception raised when a loan is not found."""
    pass
