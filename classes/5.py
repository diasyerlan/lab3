class BankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self) -> str:
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance} '
    
    def deposit(self, dep_ent):
        self.balance += dep_ent
        print("deposit accepted")
    
    def withdraw(self, with_ent):
        if self.balance >= with_ent:
            self.balance -= with_ent
            print("withdrawal accepted")
            
        else: print('no enough balance!')

x = BankAccount('Dias', 100)
print(x)
x.deposit(100)