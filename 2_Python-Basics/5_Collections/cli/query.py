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
            elif key=='category' and category_selected!=None:
                  self.session["category"][category_selected] = []
                  for i in stock:
                        if i["category"].lower()==category_selected:
                              self.session["category"][category_selected].append(i)
                  return self
            else:
                  raise Exception('Some rror in date input to search item')
            return out
      
      def _Action1(self):
            out = self.iter_stock(key='warehouse')
            tab_1=tabulate([list(i.values()) for i in out[1]], headers=['status', 'category', 'warehouse', 'date of stock'])
            tab_2=tabulate([list(i.values()) for i in out[2]], headers=['status', 'category', 'warehouse', 'date of stock'])
            TAB=tabulate([[tab_1, tab_2]], headers=['   WAREHOUSE  1','     WAREHOUSE   2'], tablefmt="pipe")
            tot = len(out[1]) +  len(out[2])
            print('TAB\n',TAB, f'\nTotal items{tot}')
            print(f"An error was found in this data: {out['error']}" if len(out['error'])>0 else '')
            return True
      
      def _Action2(self, obj):
            Warehouses = self.iter_stock('item', obj)
            d1=[list(i.values()) for i in Warehouses[1]]
            d2=[list(j.values()) for j in Warehouses[2]]
            L_w1, L_w2 = len(Warehouses[1]), len(Warehouses[2])
            availble_items = L_w1 + L_w2
            print(f'\nAmount available: {availble_items }')
            TAB=tabulate([ *d1, *d2 ], headers=['status', 'category', 'warehouse', 'days in stock'])
            print('Location:\n',TAB)
            if L_w1 > 0 or L_w2 > 0:
                  if L_w1 > L_w2:
                        print(f'\nMaximum availability: {L_w1} in Warehouse 1')
                  elif L_w2 > L_w1:
                        print(f'\nMaximum availability: {L_w2} in Warehouse 2')
                  else:
                        print(f'\nMaximum availability: {available_items} ')
                  return self._Confirm_Order(obj,availble_items)
            else:
                  print('\nNot in stock')
                  return True
      
      def _Action3(self):
            category_selected = input('Choose a category :').lower()
            if category_selected not in list(self.session["category"].keys()):
                  self.iter_stock('category',category_selected=category_selected)
            print(f'Category Selected : {category_selected}')
            tab_category_val=[list(i.values())for i in self.session['category'][category_selected]]
            TAB =tabulate(tab_category_val,['Status', 'Category', 'Warehouse', 'Date of stock'])
            print(TAB, f'\nItem founded : {len(tab_category_val)}')
            return True
            

UserUtils()