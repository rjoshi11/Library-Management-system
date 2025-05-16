# Library-Management-system
Library Management System – Python CLI Project

A terminal-based Library Management System that manages books, members, and loans using CSV as a lightweight database. Designed for learning file I/O, password hashing with bcrypt, and role-based access control (Librarian & Member).

✅ Features

Role

Functionalities

Librarian

➕ Add/Delete Books📗 Register Members📖 Issue/Return Books🗕️ View Overdue Loans

Member

🔍 Search Books📘 View Own Loan History

Uses bcrypt for secure password hashing 🔐

Persists data in CSV files

CLI-based interactive menus

Role-based access: librarian vs member

🛠️ Technologies Used

Python 3.x

bcrypt for password hashing

CSV files as mini-database (no SQL needed)

dataclass models for structured data

📂 Folder Structure

D:/DJANGO/
├── main.py
├── models.py
├── auth.py
├── librarian.py
├── member.py
├── storage.py
├── helper_hash.py
├── books.csv
├── members.csv
└── loans.csv

🚀 Getting Started

🔧 Setup

Clone this repository or download the code.

Navigate to your project directory.

Install dependencies:

pip install bcrypt

Run helper to generate password hashes (only once):

python helper_hash.py

Paste the generated hashes into members.csv.

▶️ Running the App

python main.py

Then follow the prompts to login as:

Librarian:ID = admin, Password = admin123

Member:ID = 1001, Password = Alice123

