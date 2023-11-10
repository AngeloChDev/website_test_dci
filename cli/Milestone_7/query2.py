from tabulate import tabulate
import os, sys
cwd = os.getcwd()
sys.path.append(cwd)
from Milestone_6.query2 import _Greet_User, get_user
from Milestone_7.data import personnel, stock
from Milestone_7.classes import User, Employee

session = {'need_login':True, "logged":False, 'cache':[]}
username = ''
MENU_ACTIONS = 'select one action:\n1- List all items\n2- Search an item and place an order\n3- Browse by category\n4- Quit\n'

def options():
      return MENU_ACTIONS

def login(self):
      passwd = input('\nWrite your password :')
      session['cache'].append(f'You tried to login whith password : {passwd}')
      for i in personnel:
            if username==i['user_name'] and passwd==i['password']:
                  return True
            elif 'head_of' in list(i.keys()):
                  for j in i['head_of']:
                        if j['user_name']==username and j['password']==passwd:
                              return True
      session['cache'].append('Login refused')
      return False
      
def get_user():
      username = input('\nGive a username : ')
      for log in personnel:
            if username==log['user_name']:
                  return Employee(username)
      return User(username)
      
      
def _Confirm_Order(item_tobuy, item_disponible):
      order_confirm = input('\nYou want buy some of this items ? tap yes or no :\n')   
      if order_confirm=='no':
            session['cache'].append('You refused to buy')
            return shoot_down(username)
      if order_confirm=='yes':
            session['cache'].append('You accepted to buy')
            if session["need_login"]==True:
                  while session["logged"]==False: 
                        session["logged"] = login()
            session['cache'].append('Login accepted')
            n_tobuy=input('\nHow many items you would like to buy ? \n')
            while not n_tobuy.isnumeric() or int(n_tobuy) <= 0:
                  n_tobuy=input('\nHow many items you would like to buy? \nPlease enter a numerical input greater than 0')
            if int(n_tobuy) <= item_disponible:
                  print(f'\nYour order has been placed!\nNumber of item : {n_tobuy}\nItem : {item_tobuy}')
                  session['cache'].append(f'You had bought : {n_tobuy} ; {item_tobuy}')
                  return shoot_down(username)
            elif int(n_tobuy) > item_disponible:
                  print('\nYou choosed a number of items more hight than the number of items in stock')
                  buy_all= input('Do you want to buy the maximum number of items available? tap yes or no\n')
                  session['cache'].append('You selected a number of items not in stock')
                  if buy_all=='no':
                        session['cMENU_ACTIONSache'].append('You refused to buy the dsponible number of items')
                        return shoot_down(username)
                  elif buy_all=='yes':
                        print(f'\nYour order has been placed!\nNumber of item : {item_disponible}\nItem : {item_tobuy}\n')
                        session['cache'].append(f'You accepted to buy the dsponible number of items : {item_disponible} ; {item_tobuy}')
                        
                        return shoot_down(username)
                  else:
                        print(ValueError('ValueError in confirmation input')) 
                        return shoot_down(username)
      else:
            print(ValueError('Error in order confirmation input'))
            return shoot_down(username)
      
def shoot_down(username):
      if session["need_login"]:
            continue_ = input('You want to continue ? yes / no\n')
            if continue_=='yes':
                  session['cache'].append('You procede')
                  return True
            elif continue_=='no':
                  session['cache'].append('You are shooting down the software')
                  print(*session['cache'], sep='\n')
                  del session['cache']
      print(f'\nThank you for your visit, {username}')
      return False
            
def stock_sort(key, item=None, category_selected=None):
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
      tab_all_val = stock_sort('all')
      TAB = tabulate(tab_all_val,['state', 'category', 'warehouse', 'date of stock'])
      print(TAB, f'\nItems :{len(tab_all_val)}')
      session['cache'].append(f'You have listed the full stock  {len(tab_all_val)} items')
      return True

def _Action2(user_choose):
      res = stock_sort('item',user_choose)
      tot = sum(list(res.values()))
      for k, v in res.items():
            print(f'AmouMENU_ACTIONSnt available {v} in  Warehouse {k}')
      session['cache'].append(f'You searched {user_choose}; ware found {tot} itrms')
      return _Confirm_Order(user_choose, tot )

def _Action3():
      category = stock_sort('category')
      n=0
      for k,v in category.items():
            n+=1
            print(f'{n}-{k} ({v})') 
            
      session['cache'].append(f'You listed the available categories')
      list_category_obj = list(category.keys())
      n_category = len(list_category_obj)
      action = input('Type the number of the category to browse:')
      while not action.isnumeric() or int(action) not in range(1,n_category+1):
            action = input('Type the number of the category to browse:')
      selected = int(action)
      category_select = list_category_obj[selected-1]
      obj_selected = stock_sort('obj_category', category_selected=category_select)
      print(f'List of {category_select} available :')
      session['cache'].append(f'You searched {category_select} category')
      for obj in obj_selected:
            print(f"{obj['state']} {obj['category']}, Warehouse {obj['warehouse']} ")
      return shoot_down(username)      

def _Menu():
      
      _Menu.ACTIONS = options()
      user_action= input(_Menu.ACTIONS)
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
"""_Menu()     
print('hhh',_Menu.ACTIONS)"""

def while_loop():
      global username
      user = get_user()
      username = user._name
      session['cache'].append(f'Cache start session {username}')
      _Greet_User(username)
      x = True
      while x :
            x = _Menu()


if __name__ == '__main__':
      while_loop()