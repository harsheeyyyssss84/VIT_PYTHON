class Account:

    def __init__(self, accno, bal):
        self.accountno = accno
        self.balance = bal


    # debit method
    def debit(self, amount):        # this amount is amount which will get debited
        self.balance -= amount
        print("Rs.", amount, "was Debited from your Account with Account Number:", self.accountno)
        print("Total Balance=", self.get_balance())


    # credit method
    def credit(self, amount):        # this amount is amount which will get credited
        self.balance += amount
        print("Rs.", amount, "was Credited from your Account with Account Number:", self.accountno)
        print("Total Balance=", self.get_balance())


    def get_balance(self):
        return self.balance

acc1 = Account(123456789, 100000)
acc1.debit(1000)
acc1.credit(2000)
print("Account Number:", acc1.accountno, "has total of", acc1.balance,"Rs. Balance")