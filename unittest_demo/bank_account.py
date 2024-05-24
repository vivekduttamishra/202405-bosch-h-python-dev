

class BankAccount:
    def __init__(self, id,name,password,balance):
        self.id = id
        self.name = name
        self.password =  password
        self.balance = balance

    def deposit(self,amount):
        if amount<=0:
            return False
        
        self.balance += amount
        return True
    
    def withdraw(self,amount, password):

        if amount<=0:
            return False

        if amount>self.balance:
            return False
        
        if not self.authenticate(password):
            return False
        
        self.balance-=amount

        return True
    
    def authenticate(self,password):
        return self.password == password