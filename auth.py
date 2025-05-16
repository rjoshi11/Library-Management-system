# auth.py
import bcrypt
from datetime import date
from models import Member

def register_member(members):
    member_id = input("Enter Member ID: ")
    if any(m.MemberID == member_id for m in members):
        print("❌ Member ID already exists.")
        return
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ").encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt()).decode()
    join_date = str(date.today())
    members.append(Member(member_id, name, hashed, email, join_date))
    print("✅ Member registered.")

def login(members, role):
    id = input("Enter Member ID: ").strip()
    pwd = input("Enter password: ").encode()
    for m in members:
        if m.MemberID == id and bcrypt.checkpw(pwd, m.PasswordHash.encode()):
            if role == "librarian" and m.Email == "admin@lib.com":
                print("✅ Logged in as librarian.")
                return {"role": "librarian", "user": m}
            elif role == "member" and m.Email != "admin@lib.com":
                print("✅ Logged in as member.")
                return {"role": "member", "user": m}
    print("❌ Login failed.")
    return None