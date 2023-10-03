class BankAccount:
    pass

def create(account_number, name, password, balance, interest_rate):
    account = BankAccount()
    account.account_number = account_number
    account.name = name
    account.password = password
    account.balance = balance
    account.interest_rate = interest_rate
    return account

def deposit(account, amount):
    if amount > 0:
        account.balance += amount
    else:
        print("deposit amount must be greater than 0")

def withdraw(account, amount, password):
    if amount > 0 and amount <= account.balance and password == account.password:
        account.balance -= amount
    else:
        print("withdrawal failed: invalid amount, insufficient balance, or wrong password")

def credit_interest(account):
    account.balance += (account.balance * account.interest_rate / 1200)

def info(account):
    return f'Account Number: {account.account_number}\nName: {account.name}\nBalance: {account.balance}'

# Example usage:
account = create(36542014, "Akash patil", "password378", 100000, 5.75)

print(info(account))
print()
deposit(account,100)
print(info(account))
print()
withdraw(account, 300, "password123")
print(info(account))
print()
credit_interest(account)
print(info(account))
