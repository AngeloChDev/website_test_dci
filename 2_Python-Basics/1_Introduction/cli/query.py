"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2
from tabulate import tabulate
import os , sys
cwd = os.getcwd()
sys.path.append(cwd)
from mainclass import Task

class UserHelp(Task):

    def __init__(self) -> str:
        super().__init__()
        self.warehouses = [warehouse1, warehouse2]
        self.warehouse_name = ['Warehouse 1', 'Warehouse 2']
        self._MENU_ACTIONS = self._Set_Actions('List items by warehouse','Search an item and place an order')
        self._Order_Loop()
    
    def _Action1(self):
        tab = tabulate([[ w1 , w2] for w1,w2 in zip(*self.warehouses)], headers=self.warehouse_name)
        print(tab)
        return True
    
    def _Action2(self, user_choose):
        items_found_w1, items_found_w2, n_item_w1, n_item_w2 = [], [], 0, 0
        try:
            print(user_choose)
            for item_w1 in self.warehouses[0]:
                print(item_w1)
                if user_choose.lower() == item_w1.lower():
                    items_found_w1.append(item_w1)
            for item_w2 in self.warehouses[1]:
                if user_choose.lower() == item_w2.lower():
                    items_found_w2.append(item_w2)
        except:
            print(ValueError('Error item not found or name item '))
            return True
        finally:  
            n_item_w1, n_item_w2 = len(items_found_w1), len(items_found_w2)       
            if n_item_w1>0 and n_item_w2>0:
                print(f"Amount available: {n_item_w1 + n_item_w2} \nLocation: Both warehouses")
                print(f'Maximum availability : {n_item_w1} in Warehouse 1' if n_item_w1 > n_item_w2 else f'Maximum availability : {n_item_w2} in Warehouse 2')
            elif n_item_w1>0 :
                print(f"Amount available: {n_item_w1} in Warehouse 1")
            elif n_item_w2>0 :
                print(f"Amount available: {n_item_w2} in Warehouse 2")
            else:
                print('Not in stock') 
                return True 
            return self._Confirm_Order(user_choose, n_item_w1 + n_item_w2)
    

UserHelp()