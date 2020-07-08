class Account:
    # Step 1 - Define the suite.
    # Can use 'pass' is just stubbing out our classes.
    # Is a placeholder for creating future code
    # a suite is required, allows us to get through the error for not technically having code
    # it still works.
    # pass

    interest = 0.02
    # initializer method
    def __init__(self, account_holder):
        # Prints out the initializer of the instance.
        # Creates 
        # print(self)

        self.holder = account_holder
        self.balance = 10000

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds :('
        self.balance -= amount
        return self.balance

# my_account = Account('Matt')
sean_account = Account('Sean')
# print(my_account.holder)
# print(sean_account.holder)
# sean_account.deposit(20000)
# print(sean_account.balance)
# sean_account.withdraw(5000)
# print(sean_account.balance)
# sean_account.deposit(500)
# print(sean_account.balance)
print(sean_account.interest)
Account.interest = 0.04
print(sean_account.interest)
sean_account.interest = 0.05
print(sean_account.interest)