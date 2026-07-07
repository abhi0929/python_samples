class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


e1 = Employee("Abhi")
e2 = Employee("Ram")

print(e1.company_name)
print(e2.company_name)

Employee.change_company("Google")

print(e1.company_name)
print(e2.company_name)