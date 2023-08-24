import json

expenses = []

def add_expense():
    date = input("Enter the date (YYYY-MM-DD):")
    catagory = input("Enter category (e.g. Food, Transportation): ")
    Description =input("Enter a description:")
    amount = float(input("Enter the amount: $"))
    expense = {
        'date': date,
        'catagory': catagory,
        'Description': Description,
        'amount': amount
    }
    expenses.append(expense)
    print("Expense added successfully!")

def view_all_expenses():
    for expense in expenses:
        print(f"{expense['date']} . {expense['catagory']} - {expense['Description']} - ${expense['amount']}")
    if not expenses:
        print("No expenses available.")

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

def main():
    load_expenses()
    while True:
        print("\n---Expense Tracker---")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
            save_expenses()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
     main()
     print("Bye!")