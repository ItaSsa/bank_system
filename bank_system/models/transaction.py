from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, value: float):
        self.value = value

    @abstractmethod
    def register(self, account):
        pass