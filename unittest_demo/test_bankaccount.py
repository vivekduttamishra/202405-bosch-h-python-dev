import unittest
from bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    
    #this function is called before all tests
    # this makes sure that each test gets a fresh bank account
    def setUp(self):
        self.password="p@ss"
        self.amount=10000
        self.account=BankAccount(1,'Vivek',self.password,self.amount)


    def test_deposit_fails_for_invalid_amount(self):
        result= self.account.deposit(-1)
        self.assertFalse(result)

    def test_deposit_succeeds_for_valid_amount(self):
        result= self.account.deposit(100)
        self.assertEqual(self.amount+100, self.account.balance)


    def test_withdraw_fails_for_invalid_amount(self):
        result= self.account.withdraw(-1,self.password)
        self.assertFalse(result)

    def test_withdraw_fails_for_invalid_password(self):
        result= self.account.withdraw(1, "wrong password")
        self.assertFalse(result)

    def test_withdraw_fails_for_insuffcient_balance(self):
        result= self.account.withdraw(self.amount+1, self.password)
        self.assertFalse(result)

    def test_withdraw_succeeds_for_valid_amount(self):
        result= self.account.withdraw(1, self.password)
        self.assertEqual(self.amount-1, self.account.balance)


if __name__ == '__main__':
    unittest.main() # test runner starts