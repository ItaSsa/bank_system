class Account:
    # The banch number is fixed as we will not work with this entity
    # in this project
    def __init__(self, *, client=None, number=0, branch="0001", balance=0.0):
        self._branch = branch
        self._balance = balance
        self._number = number
        self._client = client
        self._history = None

    @classmethod
    def new_account(cls, client, number):
        return cls(client=client, number=number)

    def balance(self):
        return self._balance

    def deposit(self, value):
        if value < 0:
            print(" Only positive values are allowed for deposit")
            return False

        self._balance = self._balance + value
        return True

    def withdraw(self, value):
        if value > self._balance:
            print("The value to withdraw is greater then the balance\
                   {self._balance} ")
            return False
        
        self._balance += value
        return True
