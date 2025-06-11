import unittest
from atm import ATM, InvalidPinException, InsufficientFundsException


class ATMTestCase(unittest.TestCase):

    def setUp(self):
        self.atm = ATM(pin=1234, initial_balance=1000.0)

    def test_check_balance_correct_pin(self):
        self.assertEqual(self.atm.check_balance(1234), 1000.0)

    def test_check_balance_invalid_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.check_balance(1111)

    def test_deposit_valid_amount(self):
        self.assertEqual(self.atm.deposit(1234, 500.0), 1500.0)

    def test_deposit_invalid_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.deposit(1111, 500.0)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.atm.deposit(1234, -100.0)

    def test_withdraw_valid_amount(self):
        self.assertEqual(self.atm.withdraw(1234, 200.0), 800.0)

    def test_withdraw_invalid_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.withdraw(1111, 200.0)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsException):
            self.atm.withdraw(1234, 2000.0)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.atm.withdraw(1234, -50.0)


if __name__ == "__main__":
    unittest.main()
