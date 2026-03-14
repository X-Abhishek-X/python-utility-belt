import sys
from datetime import datetime
from data_manager import load_expenses, save_expenses

def add_expense(amount, category, description):
    expenses = load_expenses()
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'Date':<20} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 60)
    for expense in expenses:
        print(f"{expense['date']:<20} | {expense['category']:<15} | ${expense['amount']:<9} | {expense['description']}")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python tracker.py add <amount> <category> <description>")
        print("  python tracker.py list")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 5:
            print("Usage: python tracker.py add <amount> <category> <description>")
            return
        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return
        category = sys.argv[3]
        description = " ".join(sys.argv[4:])
        add_expense(amount, category, description)
    
    elif command == "list":
        list_expenses()
    
    else:
        print("Unknown command. Use 'add' or 'list'.")

if __name__ == "__main__":
    main()
