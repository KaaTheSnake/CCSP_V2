
# File: show_customer.py

import sys
from customer import Customer

if __name__ == "__main__":

   jeff = Customer('Jeff Knupp', 1000.0)
   print("Customer name: <{a}>".format(a=jeff.name) )
   print("Customer balance: <{a}>".format(a=jeff.balance) )

   print("\n@@ All methods of class(Customer): <{a}>".format(a=dir(Customer)) )
   X = dir(Customer)
   for i in range(0,len(X)):
       print("@@ All methods of class(Customer): [{a}], method: <{b}>".format(a=i,b=X[i]) )

   object_methods = [method_name for method_name in dir(Customer)
                     if callable(getattr(Customer, method_name))]
   print("\n@@ Callable methods of class(Customer)")
   for i in range(0,len(object_methods)):
      print("  i: <{a}>, b: <{b}>".format(a=i,b=object_methods[i]) )

   object_nc_methods = [method_name for method_name in dir(Customer)
                     if not callable(getattr(Customer, method_name))]
   print("\n@@ Non_callable methods of class(Customer): {a}".format(a=object_nc_methods) )

   print("\n@@ sys.path: <{a}>".format(a=sys.path) )

# -- end of file
