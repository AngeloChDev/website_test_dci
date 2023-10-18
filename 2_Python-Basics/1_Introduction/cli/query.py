"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2
from tabulate import tabulate
import re

chooses='''
make a choose
1. List items by warehouse 
2. Search an item and place an order 
3. Quit
'''

class UserHelp:
    '''class '''
    def __init__(self) -> None:
        '''init class'''
        self.warehouses = [warehouse1, warehouse2]
        self.warehouse_name = ['Warehouse 1', 'Warehouse 2']
        self.username = input('Give a username : ')
        self.greet = self.greet_user()
        self.make_order = True
        self.chart= []
        self.print_menu = self.order_loop(self.make_order)
        
        
    def order_loop(self, makeorder):
        while self.make_order==True:
            self.menu()
        
    def greet_user(self):
        '''funcion to greet the user'''
        return print(f'Welcome {self.username}')
    
    def menu(self):
        '''funcion to print the possles user chooses'''
        self.user_choose = input(chooses)
        return self.elaborate_choose(self.user_choose)
    
    def elaborate_choose(self, choose):
        '''funcion to elaborate the user choose'''
        if int(choose)==1:
            tab = tabulate([[ w1 , w2] for w1,w2 in zip(*self.warehouses)], headers=self.warehouse_name)
            print(tab)
            return self.make_order
        elif int(choose)==2:
            user_choose= input('Choose some item : ').strip()
            try:
                if user_choose in self.warehouses[0]:
                    items_found_w1 = [item for item in self.warehouses[0] if item==user_choose]
                    n_item_w1 = len(items_found_w1)
                if user_choose in self.warehouses[1]:
                    items_found_w2 = [item for item in self.warehouses[1] if item==user_choose]
                    n_item_w2 = len(items_found_w2)
                    
                if n_item_w1>0 and n_item_w2>0:
                    print(f"Item found : {user_choose} \nNumber of items founded {n_item_w1 + n_item_w2} in Both warehouse")
                    if n_item_w1 > n_item_w2:
                        print(f'found more items in the {self.warehouse_name[0]} : {n_item_w1}')
                    elif n_item_w2 > n_item_w1:
                        print(f'found more items in the {self.warehouse_name[1]} : {n_item_w2}')
                elif n_item_w1>0 :
                    print(f"Item found : {user_choose} \nNumber of items founded {n_item_w1} in {self.warehouse_name[0]}")
                elif n_item_w2>0 :
                    print(f"Item found : {user_choose} \nNumber of items founded {n_item_w2} in {self.warehouse_name[1]}")
                else:
                    print('Not in stock')  
                    
                if True :
                    order_confirm = input('You want buy th items ? tap yes or no : ')   
                    if order_confirm=='no':
                        self.make_order= False
                        print(f'Thank you for your visit, {self.username}')
                        return self.make_order
                    elif order_confirm=='yes':
                        n_tobuy=input('How many items you would like to buy ? ')
                        if int(n_tobuy) <= n_item_w1 + n_item_w2:
                            print(f'Your order has been placed!\nNumber of item : {n_tobuy}\nItem : {user_choose}') 
                            self.chart.append({f'{user_choose}': n_tobuy})
                            return self.make_order
                        elif int(n_tobuy) > n_item_w1 + n_item_w2:
                            print('You choosed a number of items more hight than the number of items in stock')
                            buy_all= input('Do you want to buy the maximum number of items available?')
                            if buy_all=='no':
                                self.make_order = False
                                print(f'Thank you for your visit, {self.username}')
                                return self.make_order
                            elif buy_all=='yes':
                                print(f'Your order has been placed!\nNumber of item : {n_item_w1 + n_item_w2}\nItem : {user_choose}')
                                self.chart.append({f'{user_choose}': n_item_w1 + n_item_w2})
                            
                                return self.make_order
                    else:   
                        raise Exception('Some error with the user input')
            except Exception as e:
                return print(e)
            
        elif int(choose)==3:
            self.make_order = False
            print(f'Thank you for your visit, {self.username}')
            return self.make_order
        else:
            raise Exception('Some error in the user input')
        
        

task = UserHelp()

# YOUR CODE STARTS HERE

# Get the user name

# Greet the user

# Show the menu and ask to pick a choice

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit
