# helper_hash.py
import bcrypt

def hash_password(plain):
    hashed = bcrypt.hashpw(plain.encode(), bcrypt.gensalt()).decode()
    print(f"Plain: {plain}")
    print(f"Hashed: {hashed}\n")

if __name__ == "__main__":
    passwords = ["admin123", "Alice123", "Bob123"]
    for pwd in passwords:
        hash_password(pwd)
