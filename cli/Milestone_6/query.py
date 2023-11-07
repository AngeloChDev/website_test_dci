from data import personnel, stock
from tabulate import tabulate
from ..mainclass import MasterWarehouse

class WarehouseUserReg(MasterWarehouse):
      
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
            elif key=='category':
                  for i in stock:
                        if i["category"] not in self.session["category"].keys():
                              self.session["category"][i['category']] = 1
                        else:
                              self.session["category"][i['category']] += 1
                  return self
            elif key=='obj_category' and category_selected!=None:
                  out=[]
                  for i in stock:
                        if category_selected==i["category"]:
                              out.append(i)
                  return out
            else:
                  print('error in sort stock funcion')
                  return True
                        
      def _Action1(self):
            tab_all_val = self.stock_sort('all')
            TAB = tabulate(tab_all_val,['state', 'category', 'warehouse', 'date of stock'])
            print(TAB, f'\nItems :{len(tab_all_val)}')
            self.session['cache'].append(f'You have listed the full stock  {len(tab_all_val)} items')
            return True
      
      def _Action2(self, user_choose):
            res = self.stock_sort('item',user_choose)
            tot = sum(list(res.values()))
            for k, v in res.items():
                  print(f'Amount available {v} in  Warehouse {k}')
            self.session['cache'].append(f'You searched {user_choose}; ware found {tot} itrms')
            return self._Confirm_Order(user_choose, tot )
      
      def _Action3(self):
            if len(self.session["category"].items()) < 1:
                  self.stock_sort('category')
            n=0
            for k,v in self.session["category"].items():
                  n+=1
                  print(f'{n}-{k} ({v})') 
                  
            self.session['cache'].append(f'You listed the available categories')
            list_category_obj = list(self.session["category"].keys())
            n_category = len(list_category_obj)
            action = input('Type the number of the category to browse:')
            while not action.isnumeric() or int(action) not in range(1,n_category+1):
                  action = input('Type the number of the category to browse:')
            selected = int(action)
            category = list_category_obj[selected-1]
            obj_selected = self.stock_sort('obj_category', category_selected=category)
            print(f'List of {category} available :')
            self.session['cache'].append(f'You searched {category} category')
            for obj in obj_selected:
                  print(f"{obj['state']} {obj['category']}, Warehouse {obj['warehouse']} ")
            return self.shoot_down()              


WarehouseUserReg()