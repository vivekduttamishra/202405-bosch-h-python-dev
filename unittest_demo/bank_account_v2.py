
class BankingException(Exception):
    def __init__(self, id, message="Banking Exception"):
        super().__init__(message)

    

class InvalidCredentialsException(BankingException):
    pass

class InsufficientFundsException(BankingException):
    def __init__(self, id, deficit,message="InsufficientFunds"):
        super().__init__(id,message)
        self.deficit = deficit


class InvalidAmountException(BankingException):
    pass



class BankAccount:
    def __init__(self, id,name,password,balance):
        self.id = id
        self.name = name
        self.password =  password
        self.balance = balance

    def deposit(self,amount):
        if amount<=0:
            raise InvalidAmountException(self.id,"amount must be positive")
        
        self.balance += amount
        return True
    
    def withdraw(self,amount, password):

        if amount<=0:
             raise InvalidAmountException(self.id,"amount must be positive")

        if amount>self.balance:
            raise InsufficientFundsException(self.id, amount-self.balance, "Insufficient funds")
        
        self.authenticate(password)
        
        self.balance-=amount

        return True
    
    def authenticate(self,password):
        if self.password is not password:
            raise InvalidCredentialsException(self.id,"Invalid credentials")