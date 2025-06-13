import unittest
from atm import ATM, InvalidPinException, InsufficientFundsException

class ATMTestCase(unittest.TestCase):
    def setUp(self):
        self.atm = ATM(pin=1234, balance=100.0)

    def test_check_balance_correct_pin(self):
        balance = self.atm.check_balance(1234)
        self.assertEqual(balance, 100.0)

    def test_check_balance_wrong_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.check_balance(9999)

    def test_deposit_successful(self):
        new_balance = self.atm.deposit(1234, 50.0)
        self.assertEqual(new_balance, 150.0)

    def test_deposit_invalid_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.deposit(1111, 50.0)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.atm.deposit(1234, -10)

    def test_withdraw_successful(self):
        new_balance = self.atm.withdraw(1234, 40.0)
        self.assertEqual(new_balance, 60.0)

    def test_withdraw_invalid_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.withdraw(1111, 10)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsException):
            self.atm.withdraw(1234, 150.0)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.atm.withdraw(1234, -30)

    def tearDown(self):
        self.atm = None

if __name__ == "__main__":
    unittest.main()
