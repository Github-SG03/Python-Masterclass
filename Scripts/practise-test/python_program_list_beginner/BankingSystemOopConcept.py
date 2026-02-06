# Base class representing a generic Bank Account
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        # Encapsulation: Private attributes
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    # Getters and Setters for encapsulated attributes
    def get_account_holder(self):
        return self.__account_holder

    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance is {self.__balance}."
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance is {self.__balance}."
        return "Insufficient balance or invalid amount."

    # Abstract method to be implemented by derived classes
    def calculate_interest(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def __str__(self):
        return f"Account Number: {self.__account_number}, Account Holder: {self.__account_holder}, Balance: {self.__balance}"

# Derived class for a Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate  # Additional attribute

    # Overriding the abstract method
    def calculate_interest(self):
        return f"Interest earned: {self.get_balance() * self.interest_rate:.2f}"

# Derived class for a Current Account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit  # Additional attribute

    # Overriding the withdraw method to include overdraft limit
    def withdraw(self, amount):
        if amount > 0 and (self.get_balance() - amount) >= -self.overdraft_limit:
            return super().withdraw(amount)
        return "Withdrawal denied. Exceeds overdraft limit."

    # Overriding the abstract method
    def calculate_interest(self):
        return "Current accounts do not earn interest."

# Composition: Bank contains multiple accounts
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []  # List to hold all accounts

    def add_account(self, account):
        if isinstance(account, BankAccount):  # Ensure it's a BankAccount object
            self.accounts.append(account)
            return f"Account {account.get_account_holder()} added."
        return "Invalid account type."

    def show_accounts(self):
        return "\n".join([str(account) for account in self.accounts])

# Real-time simulation of the banking system
if __name__ == "__main__":
    # Create a Bank
    my_bank = Bank("Global Bank")

    # Create accounts
    savings = SavingsAccount("SA123", "Alice", balance=1000)
    current = CurrentAccount("CA456", "Bob", balance=500, overdraft_limit=1000)

    # Add accounts to the bank
    print(my_bank.add_account(savings))
    print(my_bank.add_account(current))

    # Show all accounts in the bank
    print("\n--- Bank Accounts ---")
    print(my_bank.show_accounts())

    # Perform transactions
    print("\n--- Transactions ---")
    print(savings.deposit(200))
    print(savings.withdraw(150))
    print(savings.calculate_interest())

    print(current.withdraw(800))  # Overdraft usage
    print(current.calculate_interest())
