for i in range(1, 3):
    class bank(object):
        name = ""
        acctno = 0
        initial_bal = 0.0
        amt = 0

        def accept(self):
            print("welcome to abc bank")
            print("")
            print("please enter your detail")
            self.name = input("enter your name = ")
            self.acctno = int(input("enter your account no = "))
            self.initial_bal = 5000
            print("your balance is =", self.initial_bal)
            print("custimer detail")
            print("Name = ", self.name, " account no = ", self.acctno)
            print("current balance", self.initial_bal)

        def deposit(self):
            print("enter the amount to be deposited")
            self.amt = int(input())
            self.initial_bal = self.initial_bal+self.amt
            print("update balance is", self.initial_bal)

        def widthdraw(self):
            print("enter amount to be withdraw")
            self.amt = int(input())
            self.initial_bal = self.initial_bal-self.amt
            print("updated balance is", self.initial_bal)
            print("  ")
            print("-----------------------")
b1 = bank()
b1.accept()
b1.deposit()
b1.widthdraw()
