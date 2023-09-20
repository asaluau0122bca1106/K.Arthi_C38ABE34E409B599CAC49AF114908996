'''Implement a class called bankAccount that represents a bank account.the class should have private
attributes for account number,account holdername,and account balance.include methods to 
deposit money,withdraw money,and display the account balance.ensure that the account balance
cannot be accessed directly from outside the class.write a program to create an instance of the 
bankAccount class and test the deposit and withdrawal functionality.'''


class bankAccount:

def __init__(self,account_number,account_holder_name,initial_balance=0.0):
  self.__account_number=account_number
  self.__account_holder_name=account_holder_name
  self.__account_balance=initial_bal

def deposit(self,amount):
  if amount>0:
    self.__account_balance+=amount
    print("deposited ${}.new balance: ${}".format(amount,self.__account_balance))

  else:
    print("invalid deposit amount.please deposit a positive amount.")

def withdraw(self,amount):
  if amount > 0 and amount <=self.__account_balance:
    self.__account_balance-=amount
    #self.__account_balance=self.__account_balance_amount
    print("withdrew ${}. new balance: ${}".format(amount,self.__account_balance))
  else:
    print("invalid withdrawal amount or insufficient balance.")
    def display_balance(self):
      print("account balance for {} (account ${}):${}". format(self.account_holder_name,self.__account_number,self.__account_balance))
      #create an instance of the bankAccount class
      account=bankAccount(account_number="1234567890",account_holder_name="hari.doss",initial_balance=5000.0)
      #test deposit and withdrawal functionality
      account.display_balance()
      account.deposit(500.0)
      account.withdraw(200)
      account.display_balance()