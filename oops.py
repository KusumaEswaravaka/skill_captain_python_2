class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        """
        Initializes a BankAccount with the given account number, account holder name, and initial balance.
        """
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount. Please provide a positive value."

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_info(self):
        """
        Displays account information.
        """
        return f"Account Number: {self.account_number}\nHolder Name: {self.account_holder_name}\nBalance: ${self.balance}"


account1 = BankAccount("123456", "John Doe", 1000)
print(account1.display_info())
print(account1.deposit(500))
print(account1.withdraw(200))
