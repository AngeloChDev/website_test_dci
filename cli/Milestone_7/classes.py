from typing import Any, Union
from abc import ABC
import datetime
import unittest, os, sys, typing
cwd = os.getcwd()
sys.path.append(cwd)
from Milestone_7.data import personnel, stock


      
################################################################################################      
logs=personnel
guest_users = []
class Warehouse:
      '''CLASS WAREHOUSE INVENTORY'''
      __WAREHOUSES = dict()
      #__stock=list(set(w_s._Stock for w_s in _WAREHOUSES if len(_WAREHOUSES)>1))
      
      def __init__(self, new_id:int=None, stock:list=[]):
            
            self._id =new_id
            self.stock = self.check_exist(new_id) if  not None else stock 
            #(self._id, self.stock )= (new_id, x) if(not None, not None)  else (new_id, stock)# if (not None, []) else (print(f"One warehouse with this {new_id} already existe"), None)
            Warehouse.__WAREHOUSES[new_id]=self.stock #if not None else stock if new_id is not None and self.check_exist(new_id) is False else print('print') #breakpoint
            
      @staticmethod
      def check_exist(search_id:int)->None:
            '''ON INIT METHOD CHECK IF A WAREHOUSE WITH THE SAME ID EXISTS
            if more one are registered check the is'''
            if len(Warehouse.__WAREHOUSES.items())>0:
                  if search_id in Warehouse.__WAREHOUSES.keys():
                        return Warehouse.__WAREHOUSES[search_id]
            return []
      @classmethod
      @property
      def __stock__(cls)->list:
            __house_stock__= []
            for h in list(Warehouse.__WAREHOUSES.values()):
                  __house_stock__.extend(h)
            return __house_stock__
      
      def add_item(self, item:object) -> list:
            '''Check if the item is already in the Main-Warehouse invntory add if Not'''
            exist=False
            s=Warehouse.__stock__ 
            #for W in Warehouse._WAREHOUSES:
            if item in s:
                  return print(f'This item is already stored in warehouse{item.values}')
            else:
                  self.stock.append(item)
                  Warehouse.__WAREHOUSES[self._id]=self.stock
                  return True             
      @property      
      def occupancy(self)->int:
            '''Return lenght stock of self warehouse instance '''
            return len(self.stock)
      
      def search(self, name_item:str)->list:
            name_item = name_item.lower()
            output = [item for item in self.stock if item.is_name(name_item) or name_item==item.values[2]]
            return output 
           
class Item:
      def __init__(self, state:str, category:str, date_of_stock:datetime)-> None:
            self.state = state
            self.category = category
            self.date_of_stock = date_of_stock     
      @property      
      def values(self)->tuple:
            return self.state.lower(), self.category.lower(), self.date_of_stock
      def is_name(self, name:str)->bool:
            return bool(name.lower()==self.__str__().lower())
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
            return print(f"Hello, {self._name}!\nWelcome to our Warehouse Database.\nIf you don't find what you are looking for,\nplease ask one of our staff members to assist you.")

      def bye(self)->str:
            self.__actions.append('You leaving the software')
            if self.is_authenticated is not True:
                  self.__actions=[]
                  return print("Thank you")
            else:
                  print('Your action in this session',*[i for i in self.__actions ], sep='\n')
                  self.__actions=[]
                  return print(f"Thank you {self._name}")
            
class Employee(User):
      
      def __init__(self,user_name:str=None, password:str=None, head_of:list=[], is_authenticated:bool=False):
            super().__init__(user_name, password, is_authenticated)
            self.__actions = []
            self.head_of = head_of if user_name is not None  else None
            
      
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
                  return print('Need authentication before order')
            self.__actions.append(f"You ordered {item.state} {item.category} for {amount}")
            return print(f"Your order {' '.join([item.state, item.category])} {amount}")
      
      def greet(self)->str:
            self.__actions.append("You are used the greet mode")
            return print(f"Hello, {self._name}!\nIf you experience a problem with the system,\nplease contact technical support.")
