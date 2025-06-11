import unittest
from unittest.mock import Mock
from counter import Counter, Operation

class CounterTestCase(unittest.TestCase):

    def test_count_characters_returns_value_from_mock(self):
        mock_operation = Mock(spec=Operation)
        mock_operation.count.return_value = 5

        counter = Counter(mock_operation)
        result = counter.count_characters("Hello")

        self.assertEqual(result, 5)
        mock_operation.count.assert_called_once_with("Hello")

    def test_count_characters_call_once(self):
        mock_operation = Mock(spec=Operation)
        counter = Counter(mock_operation)

        counter.count_characters("Hello")
        self.assertEqual(mock_operation.count.call_count, 1)
        mock_operation.count.assert_called_with("Hello")

    def test_count_characters_multiple_calls(self):
        mock_operation = Mock(spec=Operation)
        counter = Counter(mock_operation)

        counter.count_characters("Hello")
        counter.count_characters("World")
        counter.count_characters("Test")

        self.assertEqual(mock_operation.count.call_count, 3)
        mock_operation.count.assert_any_call("Hello")
        mock_operation.count.assert_any_call("World")
        mock_operation.count.assert_any_call("Test")

if __name__ == "__main__":
    unittest.main()
