import pytest
from bank_system.models.history import History


def test_add_deposit_transaction_history():
    transaction = "Deposit()"
    history = History()
    history.add_transaction(transaction)

    assert transaction in history._transactions


def test_add_withdraw_transaction_history():
    transaction = "Witdraw()"
    history = History()
    history.add_transaction(transaction)

    assert transaction in history._transactions