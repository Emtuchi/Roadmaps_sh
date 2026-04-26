class Expense:
    def __init__(self, id, description, amount, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.amount = amount
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def updateDescription(self, newDesc, now):
        if not newDesc:
            raise ValueError("invalid input: description required")
        
        self.description = newDesc
        self.updatedAt = now()
    
    def updateAmount(self, newAmount, now):
        if newAmount <= 0:
            raise ValueError("Amount must be greater than 0")
        
        self.amount = newAmount
        self.updatedAt = now()

    def getid(self):
        return self.id
    
    def getamount(self):
        return self.amount
    
    def getDate(self):
        return self.updatedAt
    
    def toDict(self):
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "createdAt":self.createdAt,
            "updatedAt": self.updatedAt
        }
    
    @staticmethod
    def fromDict(expenseObj):
        return Expense(
            expenseObj["id"],
            expenseObj["description"],
            expenseObj["amount"],
            expenseObj["createdAt"],
            expenseObj["updatedAt"]
        )