class ATM(object):
    def __init__(self, cardnum, pin, bankname):
        self.cardnum=cardnum
        self.pin=pin
        self.banname=bankname
        self.amount=50000
    def checkbalance(self):
        print("Your balance is", self.amount)
    
    def withdraw(self, amount):
        bal=self.amount-amount
        if bal<0:
            print("insufficient funds")
        else:
            self.amount=bal
            print("Your balance is ", self.amount)

bank=input("Please enter your bank: ")
cardnum=input("Please enter your card number: ")
pin=input("Please enter your pin: ")
newuser=ATM(cardnum, pin, bank)
print("Choose your activity")
print("1 balance inquiry")
print("2 withdrawal")
activity=input("Please enter your option: ")
if activity==1:
    newuser.checkbalance()
elif activity==2:
    amount=int(input("Please enter your amount: "))
    newuser.withdraw(amount)
else: 
    print("Enter a valid option")