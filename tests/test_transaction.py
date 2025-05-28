import pytest
from bank_system.models.account import Account
# from bank_system.models.client import Client
from bank_system.models.history import History
from bank_system.models.deposit import Deposit

@pytest.fixture
# @pytest.fixture create one account object to be used for all tests
def account():
    """
        Defining account object for nexts tests
    """
    client = "New Client"
    account_number = 123
    return Account.new_account(client=client, number=account_number)

def test_deposit_transaction_registers_to_account(account):
    deposit = Deposit(value=100.0)
    deposit.register(account)

    # Check if Balance is increased 
    assert account.balance() == 100.0

    # check if the transaction is on the Account History
    assert len(account.history.transactions) == 1
    assert account.history.transactions[0] == deposit