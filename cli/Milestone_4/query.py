from cli.Milestone_4.data import warehouse1, warehouse2
from ..mainclass import MasterWarehouse
from tabulate import tabulate

class Warehouse(MasterWarehouse):

    def __init__(self) -> str:
        super().__init__()
        self.action1 = 'List items by warehouse'
        self.action2 = 'Search an item and place an order'
        self.warehouses = [warehouse1, warehouse2]
        self.warehouse_name = ['Warehouse 1', 'Warehouse 2']
        self._MENU_ACTIONS = self._Set_Actions(self.action1, self.action2)
        self._Order_Loop()
    
    def _Action1(self):
        tab = tabulate([[ w1 , w2] for w1,w2 in zip(*self.warehouses)], headers=self.warehouse_name)
        print(tab)
        return True
    
    def _Action2(self, user_choose):
        items_found_w1, items_found_w2, n_item_w1, n_item_w2 = [], [], 0, 0
        try:
            for item_w1 in self.warehouses[0]:
                if user_choose == item_w1.lower():
                    items_found_w1.append(item_w1)
            for item_w2 in self.warehouses[1]:
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
            return self._Confirm_Order(user_choose, n_item_w1 + n_item_w2)
    
    def _Action3(self):
        pass

Warehouse()