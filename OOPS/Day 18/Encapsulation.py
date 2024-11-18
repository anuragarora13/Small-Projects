class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        if amount > self.__balance:
            return "insufficient funds!"
        self.__balance-=amount
        return f"wihdrawn: {amount}"

    def get_balance(self):
        return self.__balance

account=BankAccount("Anurag",1000)
print(account.get_balance())
account.deposit(502)
print(account.get_balance())
wi=account.withdraw(1502)
print(wi)
print(account.get_balance())

