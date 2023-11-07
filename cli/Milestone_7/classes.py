from typing import Any, Union
import unittest, os, sys
cwd = os.getcwd()
sys.path.append(cwd)
from Milestone_7.data import personnel, stock
import datetime
logs=personnel
guest_users = []
class Warehouse:
      '''CLASS WAREHOUSE INVENTORY'''
      _WAREHOUSES = set()
      
      def __init__(self, id:int=None):
            if self.check_exist(id):
                  return None
            self._id = id
            self.stock = []
            Warehouse._WAREHOUSES.add(self) 
             
      @staticmethod
      def check_exist(id:int) -> bool:
            '''ON INIT METHOD CHECK IF A WAREHOUSE WITH THE SAME ID EXISTS'''
            if len(Warehouse._WAREHOUSES)>0:
                  for W in Warehouse._WAREHOUSES:
                        
                        if W._id ==id:
                              return True
            return False
      
      def add_item(self, item:object) -> list:
            '''check if the item is already in the warehouse invntory'''
            exist=False
            for W in Warehouse._WAREHOUSES:
                  if item in W.stock :
                        exist=True
                        return f'This item is already stored in warehouse {W._id}'
            if not exist:
                  self.stock.append(item)
                  return self.stock 
            
      def occupancy(self)->int:
            '''Return lenght stock of self warehouse '''
            return len(self.stock)
      
      def search(self, search_term:str)->list:
            output=[]
            for itm in self.stock:
                  if search_term in itm.values() :
                        output.append(itm)
            return output
                   
class Item:       
      def __init__(self,  state:str,category:str, date_of_stock:datetime ,*args, **kwargs)-> None:
            self.state = state
            self.category = category
            self.date_of_stock = date_of_stock
      
      def __str__(self) -> str:
            return f'{self.state} {self.category}'

class User:
      def __init__(self, user_name:str='Anonymous', password:str=None, is_authenticated:bool=False):
            self._name = user_name if user_name not in [None, '', ' '] else 'Anonymous'
            self._password = password
            self.__actions = []
            self.is_authenticated = False
      
      def is_named(self, name:str)->bool:
            self.__actions.append('You arechecking your name')
            if self._name == name:
                  return True
            return False
      
      def authenticate(self, password:str)-> bool:
            self.__actions.append('You are authenticating')
            return self.is_authenticated
      
      def greet(self)->None:
            self.__actions.append('You greetings')
            return f"Hello, {self._name}!\nWelcome to our Warehouse Database.\nIf you don't find what you are looking for,\nplease ask one of our staff members to assist you."

      def bye(self)->str:
            self.__actions.append('You leaving the software')
            if self.is_authenticated is not True:
                  self.__actions=[]
                  return "Thank you"
            else:
                  print('Your action in this session',*[i for i in self.__actions ], sep='\n')
                  self.__actions=[]
                  return f"Thank you {self._name}"
      
class Employee(User):
      
      def __init__(self,user_name:str=None, password:str=None, head_of:list=None, is_authenticated:bool=False):
            super().__init__(user_name, password, is_authenticated)
            self.__actions = []
            self.head_of = head_of
      
      def authenticate(self, password:str, list_employee:list=logs)-> bool:
            try:
                  for EMPLOYERS_LOGS in list_employee:
                        if self.is_named(EMPLOYERS_LOGS['user_name']) and password==EMPLOYERS_LOGS['password']:
                              self.is_authenticated = True
                              self.head_of = []
                              self.__actions.append('You logged in successfully')
                              return self.is_authenticated 
                        elif 'head_of' in list(EMPLOYERS_LOGS.keys()):
                              return self.authenticate(password, EMPLOYERS_LOGS['head_of'])
            except Exception as e:     
                  print(e)
                  self.__actions.append('Incorrect password; login denied')
                  print('User data not valid')
                  return False
            
      def order(self, item:Any, amount:int)->None:
            if self.is_authenticated is not True:
                  return 'Need authentication before order'
            self.__actions.append(f"You ordered {item.state} {item.category} for {amount}")
            return f"Your order {' '.join([item.state, item.category])} {amount}"
      
      def greet(self)->str:
            self.__actions.append("You are used the greet mode")
            return f"Hello, {self._name}!\nIf you experience a problem with the system,\nplease contact technical support."
         

'''      
e = Employee('Boris')
print(e.is_authenticated) 
e.authenticate('docker')
print(e.is_authenticated) '''
'''L=[]
for i in range(1,5):
      w= Warehouse(i)
      L.append(w)
I=[Item(**i) for i in stock]

for x in L:
      for j in stock:
            if x._id==j['warehouse']:
                  x.add_item(Item(**j))

for k in L:
      if k._id==4:
            
            for o in k.stock:
                  print(o,sep='\n')

            print(k.occupancy())

'''