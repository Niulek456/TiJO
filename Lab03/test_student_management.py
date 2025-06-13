import unittest
from student_management import StudentManagement

class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        self.sm = StudentManagement()

    # RED: Test dodawania studenta
    def test_add_student_should_succeed(self):
        result = self.sm.add_student("Anna", "S1", 20)
        self.assertTrue(result)
        self.assertIn("S1", self.sm.students)

    def test_add_existing_student_should_fail(self):
        self.sm.add_student("Anna", "S1", 20)
        result = self.sm.add_student("Anna", "S1", 20)
        self.assertFalse(result)

    def test_update_existing_student_should_succeed(self):
        self.sm.add_student("Tom", "S2", 21)
        result = self.sm.update_student("S2", "Tommy", 22)
        self.assertTrue(result)
        self.assertEqual(self.sm.students["S2"]["name"], "Tommy")

    def test_update_nonexistent_student_should_fail(self):
        result = self.sm.update_student("S3", "Mark", 20)
        self.assertFalse(result)

    def test_remove_student_should_succeed(self):
        self.sm.add_student("Anna", "S4", 20)
        result = self.sm.remove_student("S4")
        self.assertTrue(result)
        self.assertNotIn("S4", self.sm.students)

    def test_remove_nonexistent_student_should_fail(self):
        result = self.sm.remove_student("S5")
        self.assertFalse(result)

    def test_add_grade_valid_should_succeed(self):
        self.sm.add_student("Ola", "S6", 20)
        result = self.sm.add_grade("S6", "Math", 4.0)
        self.assertTrue(result)

    def test_add_grade_invalid_student_should_fail(self):
        result = self.sm.add_grade("S7", "Math", 4.0)
        self.assertFalse(result)

    def test_add_grade_out_of_range_should_fail(self):
        self.sm.add_student("Ola", "S8", 20)
        result = self.sm.add_grade("S8", "Math", 1.0)
        self.assertFalse(result)

    def test_avg_grades_should_return_average(self):
        self.sm.add_student("A", "S9", 20)
        self.sm.add_student("B", "S10", 22)
        self.sm.add_grade("S9", "Math", 4.0)
        self.sm.add_grade("S10", "Math", 5.0)
        self.assertEqual(self.sm.avg_grades("Math"), 4.5)

    def test_avg_grades_no_grades_should_return_0(self):
        self.assertEqual(self.sm.avg_grades("Biology"), 0.0)

    def tearDown(self):
        self.sm = None

if __name__ == "__main__":
    unittest.main()
