class History:
    def __init__(self):
        self._transactions = []

    def add_transaction(self, transaction):
        self._transactions.append(transaction)