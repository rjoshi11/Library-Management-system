import storage
import auth
import librarian
import member

def main():
    books = storage.load_books("books.csv")
    members = storage.load_members("members.csv")
    loans = storage.load_loans("loans.csv")

    print("Login as (librarian/member)?")
    role = input("> ").strip().lower()
    session = auth.login(members, role)
    if not session:
        return

    while True:
        if session['role'] == "librarian":
            print("\n=== Librarian Menu ===")
            print("1. Add Book\n2. Issue\n3. Return\n4. Overdue\n5. Register Member\n6. Exit")
            choice = input("> ")
            if choice == "1": librarian.add_book(books)
            elif choice == "2": librarian.issue_book(books, members, loans)
            elif choice == "3": librarian.return_book(books, loans)
            elif choice == "4": librarian.view_overdue(loans)
            elif choice == "5": auth.register_member(members)
            elif choice == "6": break
        else:
            print("\n=== Member Menu ===")
            print("1. Search Books\n2. My Loans\n3. Exit")
            choice = input("> ")
            if choice == "1": member.search_books(books)
            elif choice == "2": member.my_loans(loans, session['user'].MemberID)
            elif choice == "3": break

    storage.save_books("books.csv", books)
    storage.save_members("members.csv", members)
    storage.save_loans("loans.csv", loans)

if __name__ == "__main__":
    main()
