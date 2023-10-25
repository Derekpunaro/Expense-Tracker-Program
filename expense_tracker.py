from expense import Expense
def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = input("What is your expected monthly income for this month: ")
    # Gets user expense
    expense = get_user_expense()
    # Save the file 
    save_expense_to_file(expense, expense_file_path)
    summarize_expense(expense_file_path, budget)
    
# TODO: Get user input for expense 
def get_user_expense():
    print(f"🎯Get the user's expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    # Create your own Categories so user doesn't mess it up.

    expense_categories = [
        "🧾 Bills",
        "🧋 Groceries",
        "🍦 Dates", 
        "⛽️ Gas", 
        "🦄 Subscriptions",
        "💰 Savings",
        "🛫 Traveling",
        "🛍 Shopping",
    ]
    
    while True:
        print("Select a category: ")
        # returns a tuple of a list index and items
        for i, category_name in  enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1 
        except Exception:
            print("You did not input an integar value. ERROR 404")

        if i in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("INVALID category. Please, try again.")

        

        break

# TODO: Write the expense into a csv file
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
    


# TODO: Read file and summarize expenses
def summarize_expense(expense_file_path, budget_amount):
    print(f"🎯Read file and summarize expenses")
    print(f"********************************************")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(",")
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            print(line_expense)
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense_category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
             amount_by_category[key] = expense.amount
    print(f"********************************************")
    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"   {key}: $ {amount:.2f}")
    
    total_spent = sum([expense.amount for x in expenses])
    print(f"💵You've spent ${total_spent:.2f} this month!")
    remaining_budget = float(budget_amount) - total_spent 
    print(f"✅This is how much money you have left ${remaining_budget}.")

# This if function ensures that we only run this app when we call main directly
if __name__ == "__main__":  
    main()