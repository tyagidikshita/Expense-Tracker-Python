expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))

    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n----- Expense List -----")
    for expense in expenses:
        print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: ₹{expense['amount']}")
    print()

def monthly_total():
    month = input("Enter month (YYYY-MM): ")

    total = 0

    for expense in expenses:
        if expense["date"].startswith(month):
            total += expense["amount"]

    print(f"Total expenses for {month}: ₹{total}")

def category_wise_spending():
    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        if category in category_totals:
            category_totals[category] += expense["amount"]
        else:
            category_totals[category] = expense["amount"]

    print("\n----- Category Wise Spending -----")
    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount}")

def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Total")
        print("4. Category Wise Spending")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            monthly_total()

        elif choice == "4":
            category_wise_spending()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice!")

menu()