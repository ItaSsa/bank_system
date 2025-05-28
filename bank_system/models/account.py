class Account:
    def __init__(self, client, number, branch="0001", balance=0.0):
        self.client = client
        self.number = number
        self.branch = branch
        self._balance = balance
        self.history = None  
        client.add_account(self)

    
    def new_account(cls, client, number):
        return cls(client=client, number=number)
    
    @property
    def balance(self):
        return self._balance