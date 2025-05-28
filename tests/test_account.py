import pytest
from bank_system.models.account import Account


@pytest.fixture
# @pytest.fixture create one account object to be used for all tests
def account():
    """
        Defining account object for nexts tests
    """
    client = "New Client"
    account_number = 123
    return Account.new_account(client=client, number=account_number)


# When one account is created it hast to be linked to a client
def test_new_account(account):
    assert isinstance(account, Account)
    assert account._client == "New Client"
    assert account._number == 123


# Testing deposit 

def test_deposit_valid(account):
    '''
       One deposit increments balance
    '''
    assert account.deposit(100.0)
    assert account.balance() == 100.0


def test_deposit_invalid(account):
    '''
        Only positive values are allowed
    '''
    assert not account.deposit(-50.0)
    assert account.balance() == 0.0

# Testing withdraw


def test_withdraw_valid(account):
    '''
        Sufficient balance
    '''
    assert account.deposit(100.0)
    assert account.withdraw(50.0)
    assert account.balance() == 150.0


def test_withdraw_invalid(account):
    '''
       Insufficient balance
    '''
    assert not account.withdraw(50.0)
    assert account.balance() == 0.0


def test_balance_valid(account):
    '''
        Correct balance
    '''
    assert account.balance() == 0.0
