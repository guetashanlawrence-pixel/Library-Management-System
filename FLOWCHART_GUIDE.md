# Library Management System - Flowchart Guide

This document describes the flow diagrams for each feature of the Library Management System.

## 1. Add Book Flowchart

**Process Flow:**
1. Start
2. Display menu and user selects choice "1"
3. Input: Book ID
4. Input: Book Title
5. Input: Book Author
6. Create Book object with `available = True`
7. Store book in `_books` dictionary (key = book.book_id)
8. Output: "Book added: {title}"
9. End

**Key Points:**
- Books are created with availability status set to True
- Each book is stored in a dictionary for quick lookup
- The system confirms successful addition

---

## 2. Register Member Flowchart

**Process Flow:**
1. Start
2. Display menu and user selects choice "2"
3. Input: Member ID
4. Input: Member Name
5. Input: Member Email
6. Create Member object
7. Store member in `_members` dictionary (key = member.member_id)
8. Output: "Member registered: {name}"
9. End

**Key Points:**
- Members are created with their contact information
- Each member is stored in a dictionary for quick lookup
- Email is stored for future communication

---

## 3. Borrow Book Flowchart

**Process Flow:**
1. Start
2. Display menu and user selects choice "3"
3. Input: Book ID
4. Input: Member ID
5. Lookup book from `_books` dictionary
6. **Decision: Is book None?**
   - YES: Raise `BookNotFoundError` → Output error → End
   - NO: Continue
7. Lookup member from `_members` dictionary
8. **Decision: Is member None?**
   - YES: Raise `MemberNotFoundError` → Output error → End
   - NO: Continue
9. **Decision: Is book.available False?**
   - YES: Raise `BookUnavailableError` → Output error → End
   - NO: Continue
10. Call `book.borrow()` → sets available = False
11. Generate loan_id in format "L{n:03}"
12. Create Loan object with (loan_id, book, member)
13. Append loan to `_loans` list
14. Output: "{member.name} borrowed {book.title}"
15. End

**Key Points:**
- Three validation checks ensure data integrity
- Book availability is tracked with a boolean flag
- Loan records are created for tracking
- Loan IDs are auto-generated sequentially

---

## 4. Return Book Flowchart

**Process Flow:**
1. Start
2. Display menu and user selects choice "4"
3. Input: Book ID
4. Input: Member ID
5. Lookup book from `_books` dictionary
6. **Decision: Is book None?**
   - YES: Raise `BookNotFoundError` → Output error → End
   - NO: Continue
7. Lookup member from `_members` dictionary
8. **Decision: Is member None?**
   - YES: Raise `MemberNotFoundError` → Output error → End
   - NO: Continue
9. Search for active loan matching book_id, member_id
10. **Decision: Is loan not found?**
    - YES: Raise `LoanNotFoundError` → Output error → End
    - NO: Continue
11. Call `book.return_book()` → sets available = True
12. Call `loan.return_loan()` → marks as returned
13. Output: "{member.name} returned {book.title}"
14. End

**Key Points:**
- Similar validation checks as borrow
- Active loans are specifically searched
- Book availability is restored on return
- Loan is marked as closed

---

## 5. View Books Flowchart

**Process Flow:**
1. Start
2. Display menu and user selects choice "5"
3. Get list of books from `_books` dictionary values
4. **Decision: Is books list empty?**
   - YES: Output "No books found." → End
   - NO: Continue
5. Output: "Books:" header
6. For each book in books:
   a. **Decision: Is book.available True?**
      - YES: Set status = "Available"
      - NO: Set status = "Borrowed"
   b. Output: "{book_id} - {title} by {author} [{status}]"
   c. Loop to next book
7. End

**Key Points:**
- Displays all books with their status
- Status indicates whether book is available or borrowed
- Empty library is handled gracefully

---

## 6. View Members Flowchart

**Process Flow:**
1. Start
2. Display menu and user selects choice "6"
3. Get list of members from `_members` dictionary values
4. **Decision: Is members list empty?**
   - YES: Output "No members found." → End
   - NO: Continue
5. Output: "Members:" header
6. For each member in members:
   a. Output: "{member_id} - {name} ({email})"
   b. Loop to next member
7. End

**Key Points:**
- Displays all registered members
- Shows member ID, name, and email
- Empty member list is handled gracefully

---

## 7. View Loans Flowchart

**Process Flow:**
1. Start
2. Display menu and user selects choice "7"
3. Get list of loans from `_loans` list
4. **Decision: Is loans list empty?**
   - YES: Output "No loans found." → End
   - NO: Continue
5. Output: "Loans:" header
6. For each loan in loans:
   a. **Decision: Is loan.is_active True?**
      - YES: Set status = "Active"
      - NO: Set status = "Closed"
   b. Output: "{loan_id} - {member.name} borrowed {book.title} [{status}]"
   c. Loop to next loan
7. End

**Key Points:**
- Displays all loan records (active and closed)
- Status indicates if loan is still active
- Empty loan list is handled gracefully

---

## 8. Exit Flowchart

**Process Flow:**
1. Start
2. Display menu and user selects choice "8"
3. Output: "Program closed."
4. Execute break statement → exit while-True loop
5. Program execution ends
6. Return to operating system
7. End

**Key Points:**
- Graceful exit from the main loop
- Confirmation message to user
- No data cleanup (for in-memory system)

---

## Data Structures

### _books (Dictionary)
```
{
    "B001": Book("B001", "Python Programming", "John Smith", available=True),
    "B002": Book("B002", "Data Science", "Jane Doe", available=False),
    ...
}
```

### _members (Dictionary)
```
{
    "M001": Member("M001", "Alice Johnson", "alice@example.com"),
    "M002": Member("M002", "Bob Smith", "bob@example.com"),
    ...
}
```

### _loans (List)
```
[
    Loan("L001", Book(...), Member(...), is_active=True),
    Loan("L002", Book(...), Member(...), is_active=False),
    ...
]
```

---

## Error Handling Flow

```
Operation
    ↓
[Validation Checks]
    ↓
┌─────────────────┐
│ Check Passed?   │
└─────────────────┘
   ↙ NO       ↘ YES
[Raise          [Execute
 Exception]      Operation]
   ↓                ↓
[Catch]      [Success Output]
   ↓                ↓
[Error         [Return to
 Output]        Main Loop]
   ↓
[Return to
 Main Loop]
```

---

## Notes

- All collections use efficient data structures (dictionaries for O(1) lookup)
- Loan IDs are auto-generated to ensure uniqueness
- The system maintains referential integrity between entities
- Error handling prevents invalid states in the system
