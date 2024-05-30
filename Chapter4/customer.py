
# File: customer.py

class Customer(object):
   def __init__(self, name, balance=0.0):
       self.name = name
       self.balance = balance
   def withdraw(self, amount):
       if amount > self.balance:
          raise RuntimeError('Amount greater than available balanace.')
       self.balance -= amount
       return self.balance

if __name__ == "__main__":

   jeff = Customer('Jeff Knupp', 1000.0)
   print("Customer name: <{a}>".format(a=jeff.name) )
   print("Customer balance: <{a}>".format(a=jeff.balance) )

# -- end of file
