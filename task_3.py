class BankAccount:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return f"Account Number: {self.acc_num}\nBalance: {self.balance}"


class CheckingAccount(BankAccount):
    def __init__(self, acc_num, balance, no_transaction):
        super().__init__(acc_num, balance)
        self.no_transaction = no_transaction
        self.transaction_count = 0

    def deposit(self, amount):
        if self.transaction_count < self.no_transaction:
            super().deposit(amount)
            self.transaction_count += 1
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.transaction_count < self.no_transaction:
            if super().withdraw(amount):
                self.transaction_count += 1
                return True
            else:
                return False
        else:
            return False

    def next_month(self):
        self.transaction_count = 0

    def __str__(self):
        return f"Checking Account\n{super().__str__()}\nTransaction Count: {self.transaction_count}"


class SavingsAccount(BankAccount):
    def __init__(self, acc_num, balance, interest_rate):
        super().__init__(acc_num, balance)
        self.interest_rate = interest_rate

    def next_month(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

    def __str__(self):
        return f"Savings Account\n{super().__str__()}\nInterest Rate: {self.interest_rate}"


