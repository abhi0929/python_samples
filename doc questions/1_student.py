class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 40

s1 = Student("Abhi", 80)
s2 = Student("Ram",70)

print(s1.name, "Passed" if s1.is_passed() else "Failed")
print(s2.name, "passed" if s2.is_passed() else "Failed")