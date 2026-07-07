class Course:
    total_students = 0

    def __init__(self, student_name):
        self.student_name = student_name

    def enroll(self):
        Course.total_students += 1
        print(self.student_name, "Enrolled")

    @classmethod
    def show_total(cls):
        print("Total Students:", cls.total_students)

    @staticmethod
    def is_eligible(age):
        return age >= 18


s1 = Course("Abhi")
s2 = Course("Ram")
s3 = Course("Patel")

s1.enroll()
s2.enroll()
s3.enroll()

Course.show_total()

print(Course.is_eligible(20))
print(Course.is_eligible(16))