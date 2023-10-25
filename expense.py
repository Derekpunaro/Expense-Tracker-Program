class Expense:
    # Classes need a constructor method
    def __init__(self, name, category, amount) -> None:
        # I want a name and and expense so make sure to add arguments so the constructors knows where to pull from
        self.name = name
        self.category = category
        self.amount= amount
    
    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"