from models.expense import Expense
from utils.file import readFile, writeFile

class ExpenseRepo:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def getAll(self):
        data = readFile(self.file_path)
        return [Expense.fromDict(d) for d in data]
    
    def saveAll(self, expenses):
        writeFile(self.file_path, [e.toDict() for e in expenses])

    def findById(self, id):
        return next((e for e in self.getAll() if e.getid() == int(id)), None)
    
    def deleteById(self, id):
        expenses = [e for e in self.getAll() if e.getid() != int(id)]
        self.saveAll(expenses)
