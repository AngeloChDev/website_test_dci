from tabulate import tabulate
import datetime as D
from datetime import datetime
import os, sys
cwd = os.getcwd()
sys.path.append(cwd)
from Milestone_5.data import stock
from Milestone_4.query2 import get_user, _Greet_User, shoot_down, _Confirm_Order

username = ''
MENU_ACTIONS='select one action:\n1- List all items\n2- Search an item and place an order\n3- Browse by category\n4- Quit'

def iter_stock(key,item_name=None, category_selected=None):
      out = {1:[], 2:[], 'category':dict(), 'category_selected': [] ,'error':[]}
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
                  if i["category"] not in out["category"].keys():
                        out["category"][i['category']] = 1
                  else:
                        out["category"][i['category']] += 1
            return out['category']
      elif key=='obj_category' and category_selected!=None:
            for i in stock:
                  if category_selected==i["category"]:
                        out['category_selected'].append(i)
            return out['category_selected']
      else:
            raise Exception('Some rror in date input to search item')

def _Action1():
      out = iter_stock(key='warehouse')
      tab_1=tabulate([[i['warehouse'], i['date_of_stock']] for i in out[1]], headers=[ 'warehouse', 'date of stock'])
      tab_2=tabulate([[i['warehouse'], i['date_of_stock']] for i in out[2]], headers=['warehouse', 'date of stock'])
      TAB=tabulate([[tab_1, tab_2]], headers=['   WAREHOUSE  1','     WAREHOUSE   2'], tablefmt="pipe",)
      print('TAB\n',TAB, f'\nTotal items in warehouse\n 1 : {len(out[1])}\nTotal items in warehouse\n 2 : {len(out[2])}')
      print(f"An error was found in this data: {out['error']}" if len(out['error'])>0 else '')
      return shoot_down(username)
      
def _Action2( obj):
      Warehouses = iter_stock('item', obj)
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
            return _Confirm_Order(obj,available_items)
      else:
            print('\nNot in stock')
            return True
      
def _Action3():
      
      category = iter_stock('category')
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
      category = list_category_obj[selected-1]
      obj_selected = iter_stock('obj_category', category_selected=category)
      print(f'List of {category} available :')
      for obj in obj_selected:
            print(f"{obj['state']} {obj['category']}, Warehouse {obj['warehouse']} ")
      return shoot_down(username)  

def _Menu(actions):
      user_action= input(actions)
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
      
def while_loop(MENU_ACTIONS):
      global username
      username = get_user()
      _Greet_User(username)
      x = True
      while x :
            x = _Menu(MENU_ACTIONS)
            
if __name__ == '__main__':
      while_loop(MENU_ACTIONS)