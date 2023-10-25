from data import personnel, stock
from tabulate import tabulate
import os , sys
cwd = os.getcwd()
sys.path.append(cwd)
from mainclass import Task

class SignedUser(Task):
      
      def __init__(self):
            super().__init__()
            self.session = {'need_login':True, "logged":False,'category':dict(), 'cache':[]}
            self.USERS = personnel
            self.action1='List all items'
            self.action2 = 'Search an item and place an order '
            self.action3 = '3-Browse by category\n'
            self._MENU_ACTIONS= self._Set_Actions(self.action1 ,self.action2 , self.action3 )
            self.session['cache'].append(f'Cache start session {self.username}')
            self._Order_Loop()
      
      
      def stock_sort(self, key, item=None, category_selected=None):
            if key=='all':
                  tab_all=[list(i.values()) for i in stock]
                  return tab_all
            elif key=='category' and category_selected!=None:
                  self.session["category"][category_selected] = list()
                  for i in stock:
                        if category_selected==i["category"].lower():
                              self.session["category"][category_selected].append(i)
                  return self
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
            tab_all_val = self.stock_sort('all')
            TAB = tabulate(tab_all_val,['state', 'category', 'warehouse', 'date of stock'])
            print(TAB, f'\nItems :{len(tab_all_val)}')
            self.session['cache'].append(f'You have viewed the stock  {len(tab_all_val)}')
            return True
      
      def _Action2(self, user_choose):
            res = self.stock_sort('item',user_choose)
            tot = sum(list(res.values()))
            for k, v in res.items():
                  print(f'Amount available {v} in  Warehouse {k}')
            self.session['cache'].append(f'You serced {user_choose}; ware found {tot} itrms')
            return self._Confirm_Order(user_choose, tot )
      
      def _Action3(self):
            category_selected = input('Choose a category :').lower()
            if category_selected  not in list(self.session["category"].keys()):
                  self.stock_sort('category',category_selected=category_selected)
            print(f'Category Selected : {category_selected}\n{self.session["category"]}')
            tab_category_val=[list(i.values())for i in self.session['category'][category_selected]]
            TAB =tabulate(tab_category_val,['Status', 'Category', 'Warehouse', 'Date of stock'])
            print(TAB, f'\nItem founded : {len(tab_category_val)}')
            self.session['cache'].append(f'you have viewed the items in the {category_selected} category; ware found {len(tab_category_val)} items')
            return True
                              
SignedUser()