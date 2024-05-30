
# File: cust_02.py

class Customer(object):

   name: str = 'A'
   balance: float = 0.0

   def __init__(self, name, balance=0.0):
       print("self.name before assignment: <{a}>".format(a=self.name) )
       self.name = name
       self.balance = balance
       print("@@ self.name: <{a}>".format(a=self.name) )
       print("@@ type(Customer): <{a}>".format(a=type(Customer)) )
       print("@@ dir(Customer): <{a}>".format(a=dir(Customer)) )
       print("@@ Customer __annotations__: <{a}>".format(a=self.__annotations__) )
       for k,v in self.__annotations__.items():
          print("Key: <{a}>, value: {b}.".format(a=k,b=v) )

   def get_name(self):
       return self.name

   def get_balance(self):
       return self.balance

   def withdraw(self, amount):
       if amount > self.balance:
          raise RuntimeError('Amount greater than available balanace.')
       self.balance -= amount
       return self.balance

if __name__ == "__main__":

   jeff = Customer('Jeff Knupp', 1000.0)
   print("Customer funds available: <{a}>".format(a=jeff.get_balance()) )

   print("Customer name: <{a}>".format(a=jeff.get_name()) )
   amount = 500.0
   print("Customer withdraw: <{a}>".format(a=amount) )
   jeff.withdraw(amount)
   print("Customer new balance: <{a}>".format(a=jeff.balance) )

# -- end of file
