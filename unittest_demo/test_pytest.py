from bank_account import BankAccount
import pytest




password="p@ss"
amount=10000

@pytest.fixture
def account():
    return BankAccount(1,"Vivek",password,amount)



def test_withdraw_fails_for_invalid_password(account):
    result = account.withdraw(1,"wrong password")
    assert result == False
    assert account.balance==amount


def test_withdraw_fails_for_invalid_amount(account):
    result = account.withdraw(-1,password)
    assert result == False
    assert account.balance==amount

def test_withdraw_fails_for_insuffcient_balance(account):
    result = account.withdraw(amount+1, password)
    assert result == False
    assert account.balance==amount

def test_withdraw_succeeds_for_valid_amount(account):
    result = account.withdraw(1,password)
    assert result == True
    assert account.balance==amount-1