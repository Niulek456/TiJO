class StudentManagement:
    """
    Klasa zarzadzajaca studentami i ich ocenami.
    """
    def __init__(self):
        self.students = {}
        self.grades = {}

    def add_student(self, id: str, name: str, age: int) -> bool:
        if id in self.students:
            return False
        self.students[id] = {"name": name, "age": age}
        return True

    def update_student(self, id: str, name: str, age: int) -> bool:
        if id not in self.students:
            return False
        self.students[id] = {"name": name, "age": age}
        return True

    def remove_student(id: str, self) -> bool:
        if id not in self.students:
            return False
        del self.students[id]
        return True


    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        if student_id not in self.students or grade not in [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]:
            return False
        if subject in self.grades:
            self.grades[subject][student_id] = grade
        else:
            self.grades[subject] = {student_id: grade}


    def avg_grades(self, subject: str) -> float:
        total, count = 0, 0
        for student_id in self.grades:
            if subject in self.grades[student_id]:
                total += sum(self.grades[student_id][subject])
                count += len(self.grades[student_id][subject])
        return total / count if count > 0 else 0.0
