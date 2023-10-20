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
            self._MENU_ACTIONS= self._Set_Actions('List all items','Search an item and place an order ')
            self._Order_Loop()
      
      def iter_stock(self,key,item_name=None):
            out = {1:[], 2:[], 'error':[]}
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
                        if dictionary["state"].lower()+' '+dictionary["category"].lower() ==item_name.lower():
                              dic_data = datetime.strptime(dictionary['date_of_stock'],'%Y-%m-%d %H:%M:%S')
                              days=now - dic_data
                              dictionary['date_of_stock']= days.days
                              print(dictionary['date_of_stock'])
                              if dictionary["warehouse"]==1:
                                    out[1].append(dictionary)
                              elif dictionary["warehouse"]==2:
                                    out[2].append(dictionary)
                              else:
                                    out['error'].append(dictionary)
            else:
                  raise Exception('Some rror in date input to search item')
            return out
      
      def _Action1(self):
            out = self.iter_stock(key='warehouse')
            tab_1=tabulate([list(i.values()) for i in out[1]], headers=['status', 'category', 'warehouse', 'date of stock'])
            tab_2=tabulate([list(i.values()) for i in out[2]], headers=['status', 'category', 'warehouse', 'date of stock'])
            TAB=tabulate([[tab_1, tab_2]], headers=['   WAREHOUSE  1','     WAREHOUSE   2'], tablefmt="pipe")
            print('TAB\n',TAB)
            print(f"An error was found in this data: {out['error']}" if len(out['error'])>0 else '')
            return True
      
      def _Action2(self, obj):
            Warehouses = self.iter_stock('item', obj)
            d1=[list(i.values()) for i in Warehouses[1]]
            d2=[list(j.values()) for j in Warehouses[2]]
            L_w1, L_w2 = len(Warehouses[1]), len(Warehouses[2])
            availble_items = L_w1 + L_w2
            print(f'Amount available: {availble_items }')
            TAB=tabulate([ *d1, *d2 ], headers=['status', 'category', 'warehouse', 'days in stock'])
            print('Location:\n',TAB)
            if L_w1 > 0 or L_w2 > 0:
                  if L_w1 > L_w2:
                        print(f'Maximum availability: {L_w1} in Warehouse 1')
                  elif L_w2 > L_w1:
                        print(f'Maximum availability: {L_w2} in Warehouse 2')
                  else:
                        print(f'Maximum availability: {available_items} ')
                  return self._Confirm_Order(obj,availble_items)
            else:
                  print('Not in stock')
                  return True

UserUtils()