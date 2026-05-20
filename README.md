# Library Management System

A Python-based Library Management System that provides functionality to manage books, members, and loans in a library.

## Features

### 1. Add Book
Register a new book in the library system.
- **Input**: Book ID, Title, Author
- **Process**: Create a Book object with availability set to True
- **Output**: Confirmation message

### 2. Register Member
Register a new member in the library system.
- **Input**: Member ID, Name, Email
- **Process**: Create a Member object
- **Output**: Confirmation message

### 3. Borrow Book
Allow a member to borrow an available book.
- **Input**: Book ID, Member ID
- **Validation**: 
  - Check if book exists
  - Check if member exists
  - Check if book is available
- **Process**: 
  - Mark book as borrowed
  - Create a Loan record
- **Output**: Success message or error message

### 4. Return Book
Handle the return of a borrowed book.
- **Input**: Book ID, Member ID
- **Validation**:
  - Check if book exists
  - Check if member exists
  - Check if there's an active loan
- **Process**:
  - Mark book as available
  - Close the loan record
- **Output**: Success message or error message

### 5. View Books
Display all books in the library with their availability status.
- **Process**: Retrieve all books from the library
- **Output**: List of books with format: `{book_id} - {title} by {author} [{status}]`

### 6. View Members
Display all registered members.
- **Process**: Retrieve all members from the library
- **Output**: List of members with format: `{member_id} - {name} ({email})`

### 7. View Loans
Display all loan records (both active and closed).
- **Process**: Retrieve all loans from the library
- **Output**: List of loans with format: `{loan_id} - {member_name} borrowed {book_title} [{status}]`

### 8. Exit
Exit the program gracefully.

## Project Structure

```
library-management-system/
├── main.py                 # Entry point and CLI interface
├── book.py                 # Book class definition
├── member.py               # Member class definition
├── loan.py                 # Loan class definition
├── library_service.py      # LibraryService class for business logic
├── exceptions.py           # Custom exception definitions
└── README.md              # This file
```

## Classes

### Book
Represents a book in the library.
- **Attributes**:
  - `book_id`: Unique identifier
  - `title`: Book title
  - `author`: Author name
  - `available`: Availability status (True/False)
- **Methods**:
  - `borrow()`: Mark book as borrowed
  - `return_book()`: Mark book as available

### Member
Represents a library member.
- **Attributes**:
  - `member_id`: Unique identifier
  - `name`: Member name
  - `email`: Email address

### Loan
Represents a book loan transaction.
- **Attributes**:
  - `loan_id`: Unique identifier
  - `book`: Book object
  - `member`: Member object
  - `date_borrowed`: Date when borrowed
  - `date_returned`: Date when returned (if applicable)
  - `is_active`: Loan status
- **Methods**:
  - `return_loan()`: Mark loan as returned

### LibraryService
Manages all library operations.
- **Methods**:
  - `add_book(book_id, title, author)`: Add a new book
  - `register_member(member_id, name, email)`: Register a new member
  - `borrow_book(book_id, member_id)`: Borrow a book
  - `return_book(book_id, member_id)`: Return a book
  - `view_books()`: Get all books
  - `view_members()`: Get all members
  - `view_loans()`: Get all loans

## Exceptions

- `LibraryException`: Base exception class
- `BookNotFoundError`: Raised when a book is not found
- `MemberNotFoundError`: Raised when a member is not found
- `BookUnavailableError`: Raised when a book is already borrowed
- `LoanNotFoundError`: Raised when a loan is not found

## Usage

### Running the Application

```bash
python main.py
```

### Example Workflow

1. **Add Books**:
   ```
   Choice: 1
   Book ID: B001
   Title: Python Programming
   Author: John Smith
   ```

2. **Register Members**:
   ```
   Choice: 2
   Member ID: M001
   Name: Alice Johnson
   Email: alice@example.com
   ```

3. **Borrow a Book**:
   ```
   Choice: 3
   Book ID: B001
   Member ID: M001
   ```

4. **View Books**:
   ```
   Choice: 5
   ```

5. **Return a Book**:
   ```
   Choice: 4
   Book ID: B001
   Member ID: M001
   ```

## Error Handling

The system includes comprehensive error handling for:
- Missing books
- Missing members
- Unavailable books (already borrowed)
- Missing loan records
- Invalid user input

## Future Enhancements

- Data persistence (file storage or database)
- Late fee calculations
- Member search functionality
- Book search functionality
- Loan history reports
- Admin authentication
- GUI interface
