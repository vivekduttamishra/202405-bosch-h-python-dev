from bank_account import BankAccount

password="p@ss"
amount=10000
account = BankAccount(1,"Vivek",password,10000)


print(account.deposit(1))
print(account.deposit(-1))

print(account.withdraw(1,password))
print(account.withdraw(-1,password))
print(account.withdraw(1,"wrong password"))
print(account.withdraw(amount+1, password))
print(account.balance)


