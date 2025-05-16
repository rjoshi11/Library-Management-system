def search_books(books):
    query = input("Enter title or author keyword: ").lower()
    for b in books:
        if query in b.Title.lower() or query in b.Author.lower():
            print(f"{b.Title} by {b.Author} | Available: {b.CopiesAvailable}")

def my_loans(loans, member_id):
    print("\nMy Loans:")
    for l in loans:
        if l.MemberID == member_id:
            print(f"{l.ISBN} | Issued: {l.IssueDate} | Due: {l.DueDate} | Returned: {l.ReturnDate or 'No'}")