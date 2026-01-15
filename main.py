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
def add_income():
    category = input("Enter income category (Salary, Freelance, etc): ")
    amount = float(input("Enter income amount: "))
    date = input("Enter date (YYYY-MM-DD): ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, ?)",
        ("Income", category, amount, date)
    )

    conn.commit()
    conn.close()

    print("Income added successfully!")
def add_expense():
    category = input("Enter expense category (Food, Travel, etc): ")
    amount = float(input("Enter expense amount: "))
    date = input("Enter date (YYYY-MM-DD): ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, ?)",
        ("Expense", category, amount, date)
    )

    conn.commit()
    conn.close()

    print("Expense added successfully!")

def view_report():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    records = cursor.fetchall()

    total_income = 0
    total_expense = 0

    print("\n---- Financial Report ----")
    print("ID | Type | Category | Amount | Date")
    print("-----------------------------------")

    for row in records:
        id, type_, category, amount, date = row
        print(f"{id} | {type_} | {category} | {amount} | {date}")

        if type_ == "Income":
            total_income += amount
        else:
            total_expense += amount

    print("\nTotal Income:", total_income)
    print("Total Expense:", total_expense)
    print("Balance:", total_income - total_expense)

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
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        view_report()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
