import unittest
from lottery import lottery


class LotteryTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(lottery([1, 1, 2, 2, 2, 4, 5], 2), [[1, 1], [2, 2, 2]])

    def test_none_size(self):
        self.assertEqual(lottery([1, 2, 3], None), [])

    def test_zero_size(self):
        self.assertEqual(lottery([1, 2, 3], 0), [])

    def test_empty_input(self):
        self.assertEqual(lottery([], 2), [])

    def test_high_size(self):
        self.assertEqual(lottery([1, 2, 3], 5), [])

    def test_duplicate_trigger_once(self):
        self.assertEqual(lottery([1, 1, 1, 2, 2, 2], 3), [[1, 1, 1], [2, 2, 2]])


if __name__ == "__main__":
    unittest.main()
