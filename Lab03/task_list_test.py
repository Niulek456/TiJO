import unittest
from task_list import TaskList

class TakListTestCase(unittest.TestCase):
    def test_add_task_should_add_task_to_list(self):
        task_list = TaskList()

        task_list.add_task("Buy milk")

        self.assertEqual(task_list.tasks(), ["Buy milk"])

if __name__ == "__main__":
    unittest.main()