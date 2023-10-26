from typing import Any, Optional
from datetime import datetime
from loader import Loader

'''
personnel = Loader(model="personnel")
stock = Loader(model="stock")
'''

class Warehouse:
      _WAREHOUSES = dict()
      
      def __init__(self, id:int)->None:
            if self.check_exist(id):
                  raise ValueError('A warehouse with this id already exist')
            self.id = id
            self.stock = []
            Warehouse._WAREHOUSES[self.id] = self.stock
            
 
      @staticmethod
      def check_exist( id:int)->bool:
            if id in list(Warehouse._WAREHOUSES.keys()):
                  return True 
            return False
      
      def add_item(self, item:object) -> None:
            exist=False
            for v in list(Warehouse._WAREHOUSES.values()):
                  if item in v:
                        exist=True
            if exist:
                  return print('This item is already stored in some warehouse')
            else:      
                  self.stock.append(item)
                  return self.stock
      
      def occupancy(self)->int:
            return len(self.stock)
      
      def search(self, search_term)->list:
            out = []
            for k, v in Warehouse._WAREHOUSES.items():
                  for j in v:
                        for i in j.values():
                              if search_term.lower() == i.lower():
                                    out.append(j)
            return out
            
class Item:
      def __init__(self, state:str, category:str, date_of_stock:Any)->None:
            self.state = state
            self.category = category
            self.date_of_stock = date_of_stock  
      
      def __str__(self) -> str:
            return f'State : {self.state} Category : {self.category} Date of stock : {self.date_of_stock}'

class User:
      def __init__(self, user_name:str)->None:
            self._name = user_name if user_name not in [None, '', ' '] else 'Anonymous'
            self.__actions = []
            self.is_authenticated = False
      
      def is_named(self, name:str)->bool:
            self.__actions.append('You arechecking your name')
            if self._name == name:
                  return True
            return False
      
      def authenticate(self)-> bool:
            self.__actions.append('You are authenticating')
            return self.is_authenticated
      
      def greet(self)->None:
            self.__actions.append('You greetings')
            return f"Hello, {self._name}!\nWelcome to our Warehouse Database.\nIf you don't find what you are looking for,\nplease ask one of our staff members to assist you."

      def bye(self):
            self.__actions.append('You leaving the software')
            return f"Thank you {self._name}"
      
      
'''      def auth_user(fun):
            def wrapper(self):
                  if  not self.is_authenticated:
                        return None
                  else:
                        return fun()
            return wrapper
      
      @auth_user
      def actions(self):
            for i in self.__actions:
                  print(i)'''
      
class Employee(User):
      
      def __init__(self,user_name:str, password:str=None, head_of:list=[]):
            super().__init__(user_name)
            self.__password = password
            self.__actions = []
            self.head_of = head_of
      
      def authenticate(self, password:str)-> bool:
            if self.__password == password:
                  self.__auth = True
                  self.__actions.append('You logged in successfully')
                  return True
            self.__actions.append('Incorrect password; login denied')
            return False
      
      def order(self, item:Any, amount:int)->None:
            self.__actions.append(f"You ordered {item.state} {item.category} for {amount}")
            return f"Your order {' '.join([item.state, item.category])} {amount}"
      
      def greet(self):
            self.__actions.append("You are used the greet mode")
            return f"Hello, {self._name}!\nIf you experience a problem with the system,\nplease contact technical support."

      def bye(self):
            super().bye()
            '''self.actions(self)
            del self.__actions[:]'''

u=User('John')
print(u.greet(), u.actions())
"""  
ite = {"state": "Almost new", "category": "Smartwatch", "warehouse": 1, "date_of_stock": "2019-12-04 06:58:22"}
ite2 = {"state": "Almost", "category": "Smartwatch", "warehouse": 1, "date_of_stock": "2019-12-04 06:58:22"}

w = Warehouse(1)
y = Warehouse(3)
w.add_item(ite)
w.add_item(ite)
w.add_item(ite2)
y.add_item(ite)


print(y.search('almost new'))

u=User('John')
print(u.greet(),u._name)"""
it= Item('Almost new', 'Smartwatch', datetime.now())
e = Employee('John', 'pass123')
print(e.authenticate('pass123'), e._name, e.is_named('John'), e.order(it,2))
print(e.bye())