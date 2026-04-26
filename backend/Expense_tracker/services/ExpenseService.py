from datetime import datetime
from models.expense import Expense

class ExpenseService:
    def __init__(self, repository, factory, helpers):
        self.repo = repository
        self.factory = factory
        self.helpers = helpers

    def add(self, description, amount):
        expenses = self.repo.getAll()
        new_expense = self.factory.create(description, amount)

        expenses.append(new_expense)
        self.repo.saveAll(expenses)

        return new_expense

    def update(self, id, description, amount):
        expenses = self.repo.getAll()
        expense = next((e for e in expenses if e.getid() == int(id)), None)

        if not expense:
            raise ValueError("expense not found")
        
        if description:
            expense.updateDescription(description, self.helpers.now)
        
        if amount:
            expense.updateAmount(amount, self.helpers.now)

        self.repo.saveAll(expenses)
    
    def delete(self, id):
        expense = self.repo.findById(id)
        if not expense:
            raise ValueError("expense does not exist")
        
        self.repo.deleteById(id)
        return "expense deleted"

    def get_month_total(self, month):
        from datetime import datetime

        expenses = self.repo.getAll()
        is_month = [e for e in expenses if datetime.striptime(e.date, "%Y-%m-%d").month == month]

        return sum(e.getamount() for e in is_month)

    def get_total(self):
        expenses = self.repo.getAll()
        return sum(e.getamount() for e in expenses)
    
    def list(self):
        return self.repo.getall()
    

