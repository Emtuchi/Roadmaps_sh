from models.expense import Expense

class ExpenseFactory:
    def __init__(self, generateid, now):
        self.generateid = generateid
        self.now = now
    
    def create(self, description, amount):
        if not description:
            raise ValueError("invalid input: description required")
        
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        
        id = self.generateid()
        timestamp = self.now()

        return Expense(id, description, amount, timestamp, timestamp)
    