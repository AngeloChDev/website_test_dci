
from abc import ABC, abstractmethod, abstractclassmethod
class MasterWarehouse(ABC):
      _w=[]
      @abstractmethod
      def h(self):
            pass
      
      @staticmethod
      def chek(ic):
            if ic in MasterWarehouse._w:
                  return True
            else:
                  MasterWarehouse._w.append(ic)
                  return False
            
print(MasterWarehouse.chek(1),MasterWarehouse._w)
print(MasterWarehouse.chek(1),MasterWarehouse._w)
print(MasterWarehouse.chek(2),MasterWarehouse._w)
x = MasterWarehouse()
x.chek(3)
print(MasterWarehouse._w,x._w)
