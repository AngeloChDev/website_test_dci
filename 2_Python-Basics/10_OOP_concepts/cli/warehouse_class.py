from abc import ABC

class Warehouse:
      WAREHOUSES = dict()
      
      def __init__(self, warehouse_id:int):
            if self.check_exist(warehouse_id):
                  raise ValueError('A warehouse with this id already exist')
            self._id = warehouse_id
            self.stock = []
            Warehouse.WAREHOUSES[self._id] = self.stock
            
 
      @staticmethod
      def check_exist( _id):
            if _id in list(Warehouse.WAREHOUSES.keys()):
                  return True 
            return False
      
      def add_item(self, item:dict):
            d=item.copy()
            d.pop('warehouse')
            for k, v in Warehouse.WAREHOUSES.items():
                  if d in v:
                        print('This item is already in some warehouse stored')
                        return False
            self.stock.append(d)
            return self.stock
      
      def occupancy(self):
            return len(self.stock)
      
      def search(self, item):
            out = []
            
            

ite = {"state": "Almost new", "category": "Smartwatch", "warehouse": 1, "date_of_stock": "2019-12-04 06:58:22"}
ite2 = {"state": "Almost", "category": "Smartwatch", "warehouse": 1, "date_of_stock": "2019-12-04 06:58:22"}

w = Warehouse(1)
w.add_item(ite)
w.add_item(ite)
w.add_item(ite2)

print(w._id, w.stock, Warehouse.WAREHOUSES,sep='\n')