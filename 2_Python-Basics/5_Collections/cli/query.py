from data import stock
from tabulate import tabulate
import datetime as D
from datetime import datetime
import os , sys
cwd = os.getcwd()
sys.path.append(cwd)
from mainclass import Task

class UserUtils(Task):
      
      def __init__(self):
            super().__init__()
            self.action1 = 'List all items'
            self.action2 = 'Search an item and place an order '
            self.action3 = '3-Browse by category\n' 
            self._MENU_ACTIONS= self._Set_Actions(self.action1 ,self.action2, self.action3 )
            self._Order_Loop()
      
      def iter_stock(self,key,item_name=None, category_selected=None):
            out = {1:[], 2:[], 'category':[], 'error':[]}
            if key=='warehouse':
                  for dictionary in stock:
                        if dictionary["warehouse"]==1:
                              out[1].append(dictionary)
                        elif dictionary["warehouse"]==2:
                              out[2].append(dictionary)
                        else:
                              out['error'].append(dictionary)
                  return out
            elif key=='item' and item_name!=None:
                  now= datetime.now()
                  for dictionary in stock:
                        d_item= ' '.join([dictionary["state"], dictionary["category"]]).lower()
                        if d_item ==item_name:
                              dic_data = datetime.strptime(dictionary['date_of_stock'],'%Y-%m-%d %H:%M:%S')
                              days=now - dic_data
                              dictionary['date_of_stock']= days.days
                              if dictionary["warehouse"]==1:
                                    out[1].append(dictionary)
                              elif dictionary["warehouse"]==2:
                                    out[2].append(dictionary)
                              else:
                                    out['error'].append(dictionary)
                  return out
            elif key=='category':
                  for i in stock:
                        if i["category"] not in self.session["category"].keys():
                              self.session["category"][i['category']] = 1
                        else:
                              self.session["category"][i['category']] += 1
                  return self
            elif key=='obj_category' and category_selected!=None:
                  for i in stock:
                        if category_selected==i["category"]:
                              out['category'].append(i)
                  return out['category']
            else:
                  raise Exception('Some rror in date input to search item')
      
      def _Action1(self):
            out = self.iter_stock(key='warehouse')
            tab_1=tabulate([[i['warehouse'], i['date_of_stock']] for i in out[1]], headers=[ 'warehouse', 'date of stock'])
            tab_2=tabulate([[i['warehouse'], i['date_of_stock']] for i in out[2]], headers=['warehouse', 'date of stock'])
            TAB=tabulate([[tab_1, tab_2]], headers=['   WAREHOUSE  1','     WAREHOUSE   2'], tablefmt="pipe",)
            print('TAB\n',TAB, f'\nTotal items in warehouse\n 1 : {len(out[1])}\nTotal items in warehouse\n 2 : {len(out[2])}')
            print(f"An error was found in this data: {out['error']}" if len(out['error'])>0 else '')
            return self.shoot_down()
      
      def _Action2(self, obj):
            Warehouses = self.iter_stock('item', obj)
            L_w1, L_w2 = len(Warehouses[1]), len(Warehouses[2])
            available_items = L_w1 + L_w2
            print(f'\nAmount available: {available_items }\nLocation: ')
            for w in Warehouses.keys():
                  for v in Warehouses[w]:
                        print(f'-Warehouse {w} ( in stock for {v["date_of_stock"]} days)')
            if L_w1 > 0 or L_w2 > 0:
                  if L_w1 > L_w2:
                        print(f'\nMaximum availability: {L_w1} in Warehouse 1')
                  elif L_w2 > L_w1:
                        print(f'\nMaximum availability: {L_w2} in Warehouse 2')
                  else:
                        print(f'\nMaximum availability: {available_items} ')
                  return self._Confirm_Order(obj,available_items)
            else:
                  print('\nNot in stock')
                  return True
      
      def _Action3(self):
            if len(self.session["category"].items()) < 1:
                  self.stock_sort('category')
            n=0
            for k,v in self.session["category"].items():
                  n+=1
                  print(f'{n}-{k} ({v})') 
            list_category_obj = list(self.session["category"].keys())
            n_category = len(list_category_obj)
            action = input('Type the number of the category to browse:')
            while not action.isnumeric() or int(action) not in range(1,n_category+1):
                  action = input('Type the number of the category to browse:')
            selected = int(action)
            category = list_category_obj[selected-1]
            obj_selected = self.stock_sort('obj_category', category_selected=category)
            print(f'List of {category} available :')
            for obj in obj_selected:
                  print(f"{obj['state']} {obj['category']}, Warehouse {obj['warehouse']} ")
            return self.shoot_down()  
            

UserUtils()