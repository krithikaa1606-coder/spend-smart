import sqlite3

def connect_db():
    return sqlite3.connect("finance.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            category TEXT,
            amount REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def show_menu():
    print("\n--- SpendSmart : Student Finance Manager ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Report")
    print("4. Exit")

create_table()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Income feature coming soon")
    elif choice == "2":
        print("Expense feature coming soon")
    elif choice == "3":
        print("Report feature coming soon")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
