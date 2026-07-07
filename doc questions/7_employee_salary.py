class Employee:
    bonus_rate = 0.1
    def __init__(self,name,salary):
        self.name = name
        self.base_salary = salary

    def final_salary(self):
        return self.base_salary+(self.base_salary*Employee.bonus_rate)

    @classmethod
    def update_bonus(cls,nb):
        cls.bonus_rate = nb

    @staticmethod
    def valid(sal):
        return sal > 0

e1 = Employee("Amarnath", 5000000)
e2 = Employee("Shiva", 5000001)

print(e1.final_salary())
print(e2.final_salary())
e1.update_bonus(0.2)
print(e1.final_salary())
print(e2.final_salary())