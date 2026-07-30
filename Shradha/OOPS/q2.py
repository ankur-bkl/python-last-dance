# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self,balance,acctN):
          self.bal=balance
          self.acc=acctN
          
    def debit(self,amount):
        self.bal -= amount
        print("Rs:",amount,"was debited!")
        print("Total Balance: ", self.getBalance())
        
    def credit(self,amount):
        self.bal += amount
        print("Rs:",amount,"was credited!")
        print("Total Balance: ", self.getBalance())
        
    def getBalance(self):
        return self.bal
    
acc1=Account(10000, 12234)
print("Initial Value: ",acc1.bal)
print("Acc No.: ",acc1.acc)

acc1.debit(1000)

        