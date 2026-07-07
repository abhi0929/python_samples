class Student:
    passing_marks = 40
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print(f"{self.name} : pass")
        else:
            print(f"{self.name} : fail")

    @classmethod
    def update(cls,pm):
        cls.passing_marks = pm

    @staticmethod
    def grade_category(m):
        if m >= 90:
            return "A"
        elif m >= 80:
            return "B"
        elif m >= 70:
            return "C"
        elif m >= 60:
            return "D"
        else:
            return "F"


s1 = Student("Abhi", 99)
s2 = Student("Shiva", 98)
s3 = Student("Ram", 35)
s4 = Student("Sumanth", 96)

s1.result()
s2.result()
s3.result()
s4.result()

s3.update(99)
s1.marks = 9
s3.marks = 100
s1.result()
s2.result()
s3.result()
s4.result()


print(s1.grade_category(s1.marks))