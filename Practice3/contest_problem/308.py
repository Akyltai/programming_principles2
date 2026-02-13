class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient Funds")

initial_balance, withdraw_amount = map(int, input().split())
my_account = Account("User", initial_balance)
my_account.withdraw(withdraw_amount)