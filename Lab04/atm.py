class InvalidPinException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class ATM:
    def __init__(self, pin: int, balance: float):
        self._pin = pin
        self._balance = balance

    def check_pin(self, pin: int):
        if pin != self._pin:
            raise InvalidPinException("Nieprawidłowy PIN.")

    def check_balance(self, pin: int) -> float:
        self.check_pin(pin)
        return self._balance

    def deposit(self, pin: int, amount: float) -> float:
        self.check_pin(pin)
        if amount <= 0:
            raise ValueError("Kwota musi być dodatnia.")
        self._balance += amount
        return self._balance

    def withdraw(self, pin: int, amount: float) -> float:
        self.check_pin(pin)
        if amount > self._balance:
            raise InsufficientFundsException("Niewystarczające środki.")
        if amount <= 0:
            raise ValueError("Kwota musi być dodatnia.")
        self._balance -= amount
        return self._balance
