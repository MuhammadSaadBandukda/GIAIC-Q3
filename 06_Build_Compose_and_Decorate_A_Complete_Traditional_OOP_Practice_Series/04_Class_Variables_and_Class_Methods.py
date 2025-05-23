class Bank:
    bank_name = "HBL"
    
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    
b = Bank()

b2 = Bank()
print(b2.bank_name)
b.change_bank_name("UBL")
print(b.bank_name)
print(Bank.bank_name)