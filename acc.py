class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        if self.balance < amount:
            print("cannot withdraw ", amount ," Not sufficient Balance")
        else:
            self.balance=self.balance-amount

    def deposit(self,amount):
        if amount < 100:
            print("please deposit a minimum of 100")
        else:
            self.balance=self.balance+amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):

    def __init__(self,filepath,fee):
        self.fee = fee
        Account.__init__(self,filepath)

    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee


checking=Checking("accounts/balance.txt", 1)
checking.transfer(100)
print(checking.balance)
checking.commit()
