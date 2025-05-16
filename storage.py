# storage.py
import csv
from models import Book, Member, Loan

def load_books(file):
    with open(file, newline='') as f:
        return [Book(row['ISBN'], row['Title'], row['Author'], int(row['CopiesTotal']), int(row['CopiesAvailable']))
                for row in csv.DictReader(f)]

def save_books(file, books):
    with open(file, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(Book.__annotations__.keys())
        for b in books:
            w.writerow([b.ISBN, b.Title, b.Author, b.CopiesTotal, b.CopiesAvailable])

def load_members(file):
    with open(file, newline='') as f:
        return [Member(**row) for row in csv.DictReader(f)]

def save_members(file, members):
    with open(file, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(Member.__annotations__.keys())
        for m in members:
            w.writerow([m.MemberID, m.Name, m.PasswordHash, m.Email, m.JoinDate])

def load_loans(file):
    with open(file, newline='') as f:
        return [Loan(**row) for row in csv.DictReader(f)]

def save_loans(file, loans):
    with open(file, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(Loan.__annotations__.keys())
        for l in loans:
            w.writerow([l.LoanID, l.MemberID, l.ISBN, l.IssueDate, l.DueDate, l.ReturnDate])