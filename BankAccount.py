class BankAccount:
    
    account_data = []
    
    def __init__(self, balance = 0, int_rate = 0.01):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.account_data.append(self)
        
    def deposit(self, amount):
        self.balance = (self.balance + amount)
        return self
        
    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds: Charging a $5 fee.')
            self.balance = (self.balance - 5)
            return self
        else: 
            self.balance = (self.balance - amount)
            return self
        
    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * 0.01) + self.balance
            return self

    @classmethod
    def all_info(cls):
        for bank_accounts in cls.account_data:
            bank_accounts.display_account_info()

BankAccount1 = BankAccount(3000.00)
BankAccount2 = BankAccount(5000.00)

BankAccount1.deposit(67.50).deposit(867.00).deposit(545.00).withdraw(999.99).yield_interest()
BankAccount2.deposit(9000.00).deposit(888.88).withdraw(50.50).withdraw(532.00).withdraw(40.00).withdraw(56.00).yield_interest()

BankAccount.all_info()