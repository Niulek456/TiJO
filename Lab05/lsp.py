class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def can_withdraw(self, amount):
        return self._balance >= amount

    def withdraw(self, amount):
        if not self.can_withdraw(amount):
            raise Exception("Insufficient funds")
        self._balance -= amount

    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self._min_balance = 100

    def can_withdraw(self, amount):
        return (self._balance - amount) >= self._min_balance

def perform_transaction(account: BankAccount, deposit_amount, withdraw_amount):
    account.deposit(deposit_amount)
    account.withdraw(withdraw_amount)
    print(f"Balance after transaction: {account.get_balance()}")

# Użycie
regular = BankAccount()
savings = SavingsAccount()

perform_transaction(regular, 500, 200)   # OK
perform_transaction(savings, 500, 450)   # OK
