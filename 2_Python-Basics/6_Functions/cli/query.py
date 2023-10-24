from data import personnel, stock
from tabulate import tabulate
import os , sys
cwd = os.getcwd()
sys.path.append(cwd)
from mainclass import Task

class SignedUser(Task):
      
      def __init__(self):
            super().__init__()
            self.session = {'need_login':True, "logged":False}
            self.USERS=personnel
            self.action1='List all items'
            self.action2 = 'Search an item and place an order '
            self.action3 = '3-Browse by category\n'
            self._MENU_ACTIONS= self._Set_Actions(self.action1 ,self.action2 , self.action3 )
            self._Order_Loop()
      
      
      def stock_sort(self, key, item=None):
            if key=='all':
                  tab_v=[list(i.values()) for i in stock]
                  return tab_v
            elif key=='warehouse':
                  d = dict()
                  for i in stock:
                        if i["warehouse"] in d.keys():
                              if i["category"] in d[i["warehouse"]].keys():
                                    d[i["warehouse"]][i["category"]] += 1
                              else:
                                    d[i["warehouse"]][i["category"]] = 1
                        else:
                              d[i["warehouse"]]={i["category"]:1}
                  return d
            elif key=='item' and item!=None:
                  d = dict()
                  for i in stock:
                        i_item = ' '.join([i["state"], i["category"]]).lower()
                        if i["warehouse"] in d.keys() and i_item==item:
                              d[i["warehouse"]] +=1
                        elif i_item==item:
                              d[i["warehouse"]] = 1
                        else:
                              pass
                  return d
            else:
                  print('error in sort stock funcion')
                  return True
                        
      def _Action1(self):
            val = self.stock_sort('all')
            TAB = tabulate(val,['state', 'category', 'warehouse', 'date of stock'])
            print(TAB)
            return True
      
      def _Action2(self, user_choose):
            res = self.stock_sort('item',user_choose)
            for k, v in res.items():
                  print(f'Amount available {v} in  Warehouse {k}')
            return self._Confirm_Order(user_choose, sum(list(res.values())))
      
      def _Action3(self):
            items = self.stock_sort('warehouse')
            for i in items.keys():
                  print(f'\n \nWAREHOUSE  {i}')
                  for k, v in items[i].items():
                        print(f'{k} : {v}')
                        
            return True
                              
SignedUser()