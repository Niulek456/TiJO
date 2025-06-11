from copy import deepcopy

class TimeOfTransfer:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

class Transfer:
    def __init__(self, amount, transfer_time):
        self._amount = amount
        self._transfer_time = transfer_time

    def get_transfer_time(self):
        # Kopia defensywna – chroni wewnętrzny stan
        return deepcopy(self._transfer_time)

    def get_amount(self):
        return self._amount

    def execute_transfer(self):
        print(f"Wykonuję przelew na kwotę {self._amount} o godzinie {self._transfer_time}")

# Użycie
scheduled_time = TimeOfTransfer(14, 30)
my_transfer = Transfer(100.0, scheduled_time)

print(f"Planowany czas przelewu: {my_transfer.get_transfer_time()}")
my_transfer.execute_transfer()

# Próba modyfikacji – teraz nieskuteczna!
external_copy = my_transfer.get_transfer_time()
external_copy.hour = 16
external_copy.minute = 0

print(f"Po modyfikacji z zewnątrz: {my_transfer.get_transfer_time()}")
my_transfer.execute_transfer()
