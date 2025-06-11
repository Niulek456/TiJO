import unittest
from student_management import StudentManagement

class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.sm = StudentManagement()
        self.sm.add_student("1", "Jan", 20)
        self.sm.add_student("2", "Anna", 22)

    def test_add_student_should_add_student(self):
        self.assertTrue(self.sm.add_student("3", "Kamil", 23))
        self.assertFalse(self.sm.add_student("1", "Jan", 20))

    def test_update_student_should_update_student(self):
        self.assertTrue(self.sm.update_student("1", "Jan Nowak", 21))
        self.assertFalse(self.sm.update_student("5", "Krzysztof", 25))
    def test_remove_student_should_remove_student(self):
        self.assertTrue(self.sm.remove_student("1"))
        self.assertFalse(self.sm.remove_student("5"))

    def test_add_grade_should_add_grade_to_student(self):
        self.assertTrue(self.sm.add_grade("1", "Programowanie w C", 4.0))
        self.assertFalse(self.sm.add_grade("1", "Analiza Matematyczna", 3.0))
        self.assertFalse(self.sm.add_grade("5", "Fizyka", 4.0))
    def test_avg_grade_should_return_average_grade(self):
        self.sm.add_grade("1", "Programowanie w C", 4.0)
        self.sm.add_grade("2", "Fizyka", 5.0)
        self.assertEqual(self.sm.avg_grades("Programowanie w C"), 4.5)
        self.assertEqual(self.sm.avg_grades("Fizyka"), 0.0)


if __name__ == "__main__":
    unittest.main()
