class Account:
    def __init__(self, name, account_number, pin, balance=0):
        self.name = name
        self.account_number = account_number
        self.__pin = pin          # Encapsulation (private)
        self.__balance = balance  # Encapsulation (secure data)

    # verify PIN
    def authenticate(self, pin):
        return self.__pin == pin

    # deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    # withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    # show balance
    def show_balance(self):
        print("Current Balance:", self.__balance)

    # transfer money
    def transfer(self, other_account, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            other_account.__balance += amount
            print(f"Transferred {amount} to {other_account.name}")
        else:
            print("Transfer failed: insufficient balance")

    def get_account_number(self):
        return self.account_number

    def get_name(self):
        return self.name


# Savings Account (Inheritance)
class SavingsAccount(Account):
    def __init__(self, name, account_number, pin, balance=0, interest_rate=0.05):
        super().__init__(name, account_number, pin, balance)
        self.interest_rate = interest_rate

    # polymorphism (different behavior)
    def show_interest(self):
        print("Interest Rate:", self.interest_rate * 100, "%")


# Current Account (Inheritance)
class CurrentAccount(Account):
    def __init__(self, name, account_number, pin, balance=0, overdraft_limit=5000):
        super().__init__(name, account_number, pin, balance)
        self.overdraft_limit = overdraft_limit

    # polymorphism
    def show_overdraft(self):
        print("Overdraft Limit:", self.overdraft_limit)


# Bank System (manages all accounts)
class BankSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)
        print("Account created successfully")

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.get_account_number() == account_number:
                return acc
        return None

    # static method (utility function)
    @staticmethod
    def bank_rules():
        print("Bank Rules:")
        print("1. Keep your PIN secret")
        print("2. Maintain minimum balance")
        print("3. No illegal transactions")


# --------------------------
# SYSTEM SETUP
# --------------------------

bank = BankSystem()

# Create accounts
acc1 = SavingsAccount("Rifat", 101, 1234, 5000)
acc2 = CurrentAccount("Sakib", 102, 4321, 3000)

bank.create_account(acc1)
bank.create_account(acc2)

# --------------------------
# SIMPLE MENU SYSTEM
# --------------------------

while True:
    print("\n===== BANK MENU =====")
    print("1. Login")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        acc_no = int(input("Enter account number: "))
        pin = int(input("Enter PIN: "))

        account = bank.find_account(acc_no)

        if account and account.authenticate(pin):

            while True:
                print("\n--- ACCOUNT MENU ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Balance")
                print("4. Transfer")
                print("5. Logout")

                option = input("Choose option: ")

                if option == "1":
                    amt = int(input("Enter amount: "))
                    account.deposit(amt)

                elif option == "2":
                    amt = int(input("Enter amount: "))
                    account.withdraw(amt)

                elif option == "3":
                    account.show_balance()

                elif option == "4":
                    to_acc = int(input("Enter receiver account number: "))
                    amount = int(input("Enter amount: "))

                    receiver = bank.find_account(to_acc)

                    if receiver:
                        account.transfer(receiver, amount)
                    else:
                        print("Account not found")

                elif option == "5":
                    print("Logged out")
                    break

                else:
                    print("Invalid option")

        else:
            print("Invalid account or PIN")

    elif choice == "2":
        print("Thank you for using Bank System")
        break

    else:
        print("Invalid choice")