import pytest
from bank_system.models.deposit import Deposit
from bank_system.models.withdraw import Withdraw
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

def test_register_deposit():
    account = 


def test_register_withdraw():


