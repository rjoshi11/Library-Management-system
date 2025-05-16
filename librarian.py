from datetime import datetime, timedelta
from models import Book, Loan

def add_book(books):
    isbn = input("ISBN: ")
    if any(b.ISBN == isbn for b in books):
        print("❌ Book already exists.")
        return
    title = input("Title: ")
    author = input("Author: ")
    copies = int(input("Total Copies: "))
    books.append(Book(isbn, title, author, copies, copies))
    print("✅ Book added.")

def issue_book(books, members, loans):
    isbn = input("Enter ISBN: ")
    member_id = input("Enter Member ID: ")
    book = next((b for b in books if b.ISBN == isbn), None)
    if not book or book.CopiesAvailable < 1:
        print("❌ Book unavailable.")
        return
    if not any(m.MemberID == member_id for m in members):
        print("❌ Member not found.")
        return
    loan_id = str(len(loans) + 1)
    issue_date = datetime.today()
    due_date = issue_date + timedelta(days=14)
    loans.append(Loan(loan_id, member_id, isbn, issue_date.strftime("%Y-%m-%d"), due_date.strftime("%Y-%m-%d"), ""))
    book.CopiesAvailable -= 1
    print(f"✅ Issued. Due on {due_date.strftime('%d-%b-%Y')}.")

def return_book(books, loans):
    loan_id = input("Loan ID to return: ")
    loan = next((l for l in loans if l.LoanID == loan_id and l.ReturnDate == ""), None)
    if not loan:
        print("❌ Loan not found or already returned.")
        return
    loan.ReturnDate = str(datetime.today().date())
    for b in books:
        if b.ISBN == loan.ISBN:
            b.CopiesAvailable += 1
            break
    print("✅ Book returned.")

def view_overdue(loans):
    today = datetime.today().date()
    print("\nOverdue Loans:")
    for l in loans:
        if l.ReturnDate == "" and datetime.strptime(l.DueDate, "%Y-%m-%d").date() < today:
            print(f"Loan {l.LoanID} | Member {l.MemberID} | Due: {l.DueDate}")