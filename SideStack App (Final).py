# ===============================================
# SETUP
# ===============================================

# Import required modules
from datetime import datetime

# Define a Transaction Class
class Transaction:
    def __init__(self, description, amount, transaction_type):
        self.description = description
        self.amount = amount
        self.type = transaction_type
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def details(self):
        return f"Date: {self.date}, Description: {self.description}, Type: {self.type}, Amount: R {self.amount}"

# Store transaction objects
transactions = []

# Create add_transaction function
def add_transaction():
    print("\n--- Enter Transaction Details ---")

    # Error handling gracefully
    try:
        amount = float(input("Enter transaction amount: R "))
        description = input("Enter description: ")

        while True:
            transaction_type = input("Enter type of transaction (Earning/Expense): ")
            transaction_type_lower = transaction_type.lower()

            if transaction_type_lower == "earning" or transaction_type_lower == "expense":
                if transaction_type_lower == "earning":
                    transaction_type = "Earning"
                else:
                    transaction_type = "Expense"
                break
            else:
                print("Invalid input! Please enter either 'Earning' or 'Expense'")

        # Create a transaction object
        new_transaction = Transaction(description, amount, transaction_type)

        # Add the transaction to our list
        transactions.append(new_transaction)

        # Display what was recorded
        print(f"\nTransaction successfully recorded!")
        print(new_transaction.details())

        # Show how many transactions we have stored
        print(f"\nTotal transactions stored: {len(transactions)}")

    # Handle invalid input errors
    except ValueError:
        print("Please enter a valid amount.")

# Create view_transactions function
def view_transactions():
    print("\n" + "="*40)
    print("ALL TRANSACTIONS")
    print("="*40)

    # Check if there are any transactions
    if len(transactions) == 0:
        print("No transactions recorded yet.")
        print("Use Option 1 to add your first transaction!")
    else:
        for i, transaction in enumerate(transactions, 1):
            print(f"\nTransaction #{i}:")
            print(f"  {transaction.details()}")

        print(f"\nTotal transactions: {len(transactions)}")

    print("="*40)

# Create calculate_summary function
def calculate_summary():
    print("\n" + "=" * 40)
    print("FINANCIAL SUMMARY")
    print("=" * 40)

    # Check if there are any transactions
    if len(transactions) == 0:
        print("No transactions to summarize.")
        print("Add some transactions first using option 1!")
    else:
        total_earnings = 0
        total_expenses = 0

        # Calculate totals
        for transaction in transactions:
            if transaction.type == "Earning":
                total_earnings = total_earnings + transaction.amount
            elif transaction.type == "Expense":
                total_expenses = total_expenses + transaction.amount

        # Calculate net profit
        net_profit = total_earnings - total_expenses

        # Display the summary
        print(f"Total Earnings:  R{total_earnings:.2f}")
        print(f"Total Expenses:  R{total_expenses:.2f}")
        print("-" * 30)

        if net_profit > 0:
            print(f"Net Profit:     R{net_profit:.2f}")
            print("Great job! You're making money!")
        elif net_profit < 0:
            print(f"Net Loss:       R{abs(net_profit):.2f}")
            print("You're spending more than earning. Review your expenses!")
        else:
            print(f"Break Even:     R{net_profit:.2f}")
            print("You're breaking even - earnings equal expenses.")

        # Show transaction count
        print(f"\nBased on {len(transactions)} transactions")

    print("=" * 40)

# ===============================================
# USER INTERACTION
# ===============================================

# Welcome message and user introduction
print("=====Welcome to SideStack=====")
print("=====Stack smarter, hustle harder=====\n")

name = input("Enter your name: ")
print(f"Hello, {name}! Let's track your side hustle earnings!")

# Main menu system
while True:
    print("=" * 40)
    print("MAIN MENU")
    print("=" * 40)
    print("1. Add New Transaction")
    print("2. View All Transactions")
    print("3. View Financial Summary")
    print("4. Exit")
    print("=" * 40)

    # Get user's menu choice
    menu_choice = input("Enter your choice (1-4): ")

    # Menu handling
    if menu_choice == "1":
        add_transaction()

    elif menu_choice == "2":
        view_transactions()

    elif menu_choice == "3":
        calculate_summary()

    elif menu_choice == "4":
        print(f"Thank you for using SideStack, {name}!")
        print("Keep stacking those earnings!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")

    input("\nPress Enter to continue...")