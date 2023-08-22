class bankaccount:
    interest_rate = 0.08
    def __init__(self,acnt_no,balance):
        self.acnt_no = acnt_no
        self.balance= balance
    def deposit(self,amount):
        self.balance = amount
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = amount
        else:
            print("insufficient funds...")
    def calculate_interest(self):
        return self.balance * self.interest_rate
    @classmethod
    def set_intrst(cls,rate):
        cls.intrst = rate
        print("method")
bank = bankaccount(12345678,1000)
print(bankaccount.interest_rate)
bankaccount.set_intrst(0.07)
print(bankaccount.interest_rate)


