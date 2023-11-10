import os, sys
from tabulate import tabulate
cwd = os.getcwd()
sys.path.append(cwd)
from Milestone_4.data import warehouse1, warehouse2

username = ''
warehouses = [warehouse1, warehouse2]
MENU_ACTIONS='select one action:\n1- List items by warehouse\n2- Search an item and place an order\n3- - Quit'

def get_user():
      user = input('Give a username : ')
      return user

def _Greet_User(username):
      return print(f'\nWelcome {username}')

def shoot_down(username):
      print(f'\nThank you for your visit, {username}')
      return False

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
            return shoot_down(username)        
      else:
            print('Action input value not valid')
            return shoot_down(username)
      
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
      
      

      
def _Action1():
      tab = tabulate([[ w1 , w2] for w1,w2 in zip(*warehouses)], headers=['Warehouse 1', 'Warehouse 2'])
      print(tab)
      return True


def _Action2( user_choose):
      items_found_w1, items_found_w2, n_item_w1, n_item_w2 = [], [], 0, 0
      try:
            for item_w1 in warehouses[0]:
                  if user_choose == item_w1.lower():
                        items_found_w1.append(item_w1)
            for item_w2 in warehouses[1]:
                  if user_choose == item_w2.lower():
                        items_found_w2.append(item_w2)
      except:
            print(ValueError('Error item not found or name item '))
            return True
      finally:  
            n_item_w1, n_item_w2 = len(items_found_w1), len(items_found_w2)       
            if n_item_w1>0 and n_item_w2>0:
                  print(f"\nAmount available: {n_item_w1 + n_item_w2} \nLocation: Both warehouses")
                  print(f'\nMaximum availability : {n_item_w1} in Warehouse 1' if n_item_w1 > n_item_w2 else f'Maximum availability : {n_item_w2} in Warehouse 2')
            elif n_item_w1>0 :
                  print(f"\nAmount available: {n_item_w1} in Warehouse 1")
            elif n_item_w2>0 :
                  print(f"\nAmount available: {n_item_w2} in Warehouse 2")
            else:
                  print('\nNot in stock') 
                  return True 
            return _Confirm_Order(user_choose, n_item_w1 + n_item_w2)

def while_loop(MENU_ACTIONS):
      global username
      username = get_user()
      _Greet_User(username)
      x = True
      while x :
            x = _Menu(MENU_ACTIONS)
            
if __name__ == '__main__':
      while_loop(MENU_ACTIONS)