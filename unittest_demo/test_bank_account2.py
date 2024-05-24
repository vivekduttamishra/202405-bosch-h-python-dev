from bank_account_v2 import BankAccount, InvalidCredentialsException, InsufficientFundsException, InvalidAmountException
import pytest




password="p@ss"
amount=10000

@pytest.fixture
def account():
    return BankAccount(1,"Vivek",password,amount)



def test_withdraw_fails_for_invalid_password(account):
    with pytest.raises( InvalidCredentialsException):
        account.withdraw(1,"wrong password")
    
    assert account.balance==amount


def test_withdraw_fails_for_invalid_amount(account):
    with pytest.raises( InvalidAmountException):
        account.withdraw(-1,password)
    
    assert account.balance==amount
    

def test_withdraw_fails_for_insuffcient_balance(account):
    with pytest.raises( InsufficientFundsException) as e:
        account.withdraw(amount+1, password)
        
    assert account.balance==amount
    # e is ExceptionInfo
    # e.value is actual axception
    assert e.value.deficit==1

def test_withdraw_succeeds_for_valid_amount(account):
    result = account.withdraw(1,password)
    assert result == True
    assert account.balance==amount-1