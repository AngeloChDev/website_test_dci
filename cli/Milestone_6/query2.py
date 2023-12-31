from tabulate import tabulate
import os, sys
cwd = os.getcwd()
sys.path.append(cwd)
from Milestone_5.query2 import get_user, _Greet_User, _Menu
from Milestone_6.data import personnel, stock
from Milestone_7.classes import User, Employee
username = ''
MENU_ACTIONS = 'select one action:\n1- List all items\n2- Search an item and place an order\n3- Browse by category\n4- Quit'

def get_user():
      username = input('\nGive a username : ')
      for log in personnel:
            if username==log['user_name']:
                  return Employee(username)
      return User(username)

def login(self):
      passwd = input('\nWrite your password :')
      for i in personnel:
            if username==i['user_name'] and passwd==i['password']:
                  return True
            elif 'head_of' in list(i.keys()):
                  for j in i['head_of']:
                        if j['user_name']==username and j['password']==passwd:
                              return True
      return False
      
      
def _Confirm_Order(item_tobuy, item_disponible):
      order_confirm = input('\nYou want buy some of this items ? tap yes or no :\n')   
      if order_confirm=='no':
            return shoot_down(username)
      if order_confirm=='yes':
            n_tobuy=input('\nHow many items you would like to buy ? \n')
            while not n_tobuy.isnumeric() or int(n_tobuy) <= 0:
                  n_tobuy=input('\nHow many items you would like to buy? \nPlease enter a numerical input greater than 0')
            if int(n_tobuy) <= item_disponible:
                  print(f'\nYour order has been placed!\nNumber of item : {n_tobuy}\nItem : {item_tobuy}')
                  return shoot_down(username)
            elif int(n_tobuy) > item_disponible:
                  print('\nYou choosed a number of items more hight than the number of items in stock')
                  buy_all= input('Do you want to buy the maximum number of items available? tap yes or no\n')
                  if buy_all=='no':
                        return shoot_down(username)
                  elif buy_all=='yes':
                        print(f'\nYour order has been placed!\nNumber of item : {item_disponible}\nItem : {item_tobuy}\n')
                        return shoot_down(username)
                  else:
                        print(ValueError('ValueError in confirmation input')) 
                        return shoot_down(username)
      else:
            print(ValueError('Error in order confirmation input'))
            return shoot_down(username)
      
def shoot_down(username):
      
      continue_ = input('You want to continue ? yes / no\n')
      if continue_=='yes':
            return True
      print(f'\nThank you for your visit, {username}')
      return False
            
def stock_sort(key, item_selected=None, category_selected=None):
      if key=='all':
            all_warehouse =dict()
            for item in stock:
                  if item['warehouse'] in all_warehouse.keys():
                        all_warehouse[item['warehouse']].append(item)
                  else:
                        all_warehouse[item['warehouse']] = [item]
            return all_warehouse
      elif key=='item' and item_selected!=None:
            item_found = dict()
            for item in stock:
                  name_item = ' '.join([item["state"], item["category"]]).lower()
                  if item["warehouse"] in item_found.keys() and name_item == item_selected:
                        item_found[item["warehouse"]] += 1
                  elif name_item == item_selected:
                        item_found[item["warehouse"]] = 1
                  else:
                        pass
            return item_found
      elif key=='category':
            d=dict()
            for i in stock:
                  if i["category"] not in d.keys():
                        d[i['category']] = 1
                  else:
                        d[i['category']] += 1
            return d
      elif key=='obj_category' and category_selected!=None:
            out=[]
            for i in stock:
                  if category_selected==i["category"]:
                        out.append(i)
            return out
      else:
            print('error in sort stock funcion')
            return True


def _Action1():
      all_warehouse = stock_sort('all')
      tot_items = 0 
      for list_item in all_warehouse.values():
            tot_items += len(list_item)
            for item in list_item:
                  print(f"{item['state']}, {item['category']} {item['warehouse']}, {item['date_of_stock']} ")
      count= [f'Total items in warehouse {k}:\n {len(v)}\n' for k, v in all_warehouse.items()]
      out_tot=f"Listed {tot_items} items\n"
      print(out_tot, *count)
      return (out_tot, count)

def _Action2(user_choose):
      res = stock_sort('item',user_choose)
      tot = sum(list(res.values()))
      for k, v in res.items():
            print(f'Amount available {v} in  Warehouse {k}')
      return _Confirm_Order(user_choose, tot )

def _Action3():
      category = stock_sort('category')
      n=0
      for k,v in category.items():
            n+=1
            print(f'{n}-{k} ({v})')       
      list_category_obj = list(category.keys())
      n_category = len(list_category_obj)
      action = input('Type the number of the category to browse:')
      while not action.isnumeric() or int(action) not in range(1,n_category+1):
            action = input('Type the number of the category to browse:')
      selected = int(action)
      category_select = list_category_obj[selected-1]
      obj_selected = stock_sort('obj_category', category_selected=category_select)
      print(f'List of {category_select} available :')
      for obj in obj_selected:
            print(f"{obj['state']} {obj['category']}, Warehouse {obj['warehouse']} ")
      return shoot_down(username)      

def _Menu():
      user_action= input(MENU_ACTIONS)
      try:
            action= int(user_action)
      except Exception as e:
            print(e)
            return shoot_down(username)
            
      if action==1:
            return _Action1()
      elif action==2:
            obj = input('\nWhat is the name of the item?  ').strip()
            return _Action2(obj.lower())
      elif action==3:
            return _Action3()
      elif action==4:
            return shoot_down(username)        
      else:
            print('Action input value not valid')
            return shoot_down(username)
      

def while_loop():
      global username
      user = get_user()
      _Greet_User(user._name)
      x = True
      while x :
            x = _Menu()
            
if __name__ == '__main__':
      while_loop()