class StudentManagement:
    def __init__(self):
        self.students = {}
        self.grades = {}

    def add_student(self, name: str, id: str, age: int) -> bool:
        if id in self.students:
            return False
        self.students[id] = {"name": name, "age": age}
        return True

    def update_student(self, id: str, name: str, age: int) -> bool:
        if id not in self.students:
            return False
        self.students[id]["name"] = name
        self.students[id]["age"] = age
        return True

    def remove_student(self, id: str) -> bool:
        if id in self.students:
            del self.students[id]
            self.grades = {k: v for k, v in self.grades.items() if v["student_id"] != id}
            return True
        return False

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        if student_id not in self.students or grade < 2.0 or grade > 5.0:
            return False
        key = (student_id, subject)
        self.grades[key] = {"student_id": student_id, "subject": subject, "grade": grade}
        return True

    def avg_grades(self, subject: str) -> float:
        subject_grades = [
            g["grade"] for g in self.grades.values() if g["subject"] == subject
        ]
        if not subject_grades:
            return 0.0
        return round(sum(subject_grades) / len(subject_grades), 2)
