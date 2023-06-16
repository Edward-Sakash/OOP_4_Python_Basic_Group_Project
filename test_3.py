from task_3 import CheckingAccount, SavingsAccount

# Create instances of CheckingAccount and SavingsAccount
checking_account = CheckingAccount("12345678", 1000, 2)
savings_account = SavingsAccount("98765432", 5000, 0.05)

# Perform transactions and print account details
print("Checking Account Details:")
checking_account.deposit(500)
checking_account.withdraw(200)
print(checking_account)
print()

print("Savings Account Details:")
savings_account.deposit(1000)
savings_account.withdraw(500)
print(savings_account)
print()

# Move to the next month
checking_account.next_month()
savings_account.next_month()

# Print account details after next month
print("Checking Account Details after next month:")
print(checking_account)
print()

print("Savings Account Details after next month:")
print(savings_account)
