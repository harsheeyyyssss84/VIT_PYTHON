import json

class Account:

    def __init__(self, accno, bal):
        self.accountno = accno
        self.balance = bal

    # debit method

    def debit(self):        # this amount is amount which will get debited
        try:
            amount = float(input("Enter Amount you want to Debit: "))

            if amount <= self.balance:
                self.balance -= amount
                print("Debited Successfully!!!")
                print(f"Rs. {amount} was Debited from your Account with Account Number: {self.accountno}")
                print("Total Balance= ", self.get_balance())
                    
            else:
                print("Not Enough Balance!!!")

        except ValueError:
            print("INVALID INPUT!!! ENTER IN NUMBERS!")

    # credit method

    def credit(self):        # this amount1 is amount1 which will get credited

        try:
            amount1 = float(input("Enter Amount you want to Credit: "))
            self.balance += amount1
            print("Successfully Credited!!!")
            print(f"Rs. {amount1} was Credited to your Account with Account Number: {self.accountno}")
            print("Total Balance= ", self.get_balance())

        except ValueError:
            print("INVALID INPUT!!! ENTER IN NUMBERS!")


    def get_balance(self):
        return {self.balance}


try:
    with open("account.json", "r") as file:
        accounts_data = json.load(file)

except(FileNotFoundError, json.JSONDecodeError):
    accounts_data = []


search = input("Enter Account Number to Login: ")

current_acc_data = None

for acc in accounts_data:
    if str(acc["accountno"]) == search:
        current_acc_data = acc
        break

if current_acc_data:
    acc1 = Account(current_acc_data["accountno"], current_acc_data["balance"])
    print(f"\nWelcome Back! ACCOUNT {acc1.accountno} loaded!")

else:
    print("\nAccount Not Found! Create a new Account!")
    initial_bal = float(input("Enter Initial Balance: "))
    acc1 = Account(search, initial_bal)
    current_acc_data = {"accountno": search, "balance": initial_bal}
    accounts_data.append(current_acc_data)


while True:
    num = int(input("\nEnter 1 To Debit\nEnter 2 To Credit\nEnter 3 To Exit\nEnter Choice: "))

    if num == 1:
        acc1.debit()

    elif num == 2:
        acc1.credit()

    elif num == 3:
        print("Total Balance= ", acc1.get_balance(),"Rs.")
        break

    else:
        print("INVALID INPUT")
        break


    print("Current Balance: ", acc1.get_balance())


for acc in accounts_data:
    if str(acc["accountno"]) == acc1.accountno:
        acc["balance"] = acc1.balance



with open("account.json", "w") as file:
    json.dump(accounts_data, file, indent = 4)

print("\nData Saved Successfully, GOODBYE!!!")