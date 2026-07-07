class BankAccount:
    bank_name = "SBI"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Amount")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount):
        return amount > 0


a1 = BankAccount("Abhi", 5000)

a1.deposit(2000)
print(a1.balance)

BankAccount.change_bank_name("SBI")

print(BankAccount.bank_name)