import os , sys
from typing import Union, Iterable
from collections import Counter
cwd = os.getcwd()
sys.path.append(cwd)
from Milestone_7.classes import Warehouse, Item
from Milestone_7.data import stock 

def check_name_item(name, o=None):
      output={1:0, 2:0, 3:0, 4:0}
      output2={1:0, 2:0, 3:0, 4:0}
      for d in stock:
            if f"{d['state']} {d['category']}".lower() == name and d['warehouse'] in output.keys():
                  output[d['warehouse']] += 1
      for i in range(1,5):
            if o is not None:
                  x=len(o[i].search(name))
                  output2[i]=x
      return output, output2


def house_run(stock:[list,[dict, dict]]=stock,search_item:str=None,all_search:bool=False):
      Houses = dict()
      same=0
      all_search_fun={1:0, 2:0, 3:0, 4:0}
      for n in range(1,5):
            x = Warehouse(n)
            Houses[n]=x
      
      for o in stock:
            item = Item(o['state'], o['category'], o['date_of_stock'])
            Houses[o['warehouse']].add_item(item)
      h1 = Houses[1].occupancy
      h2 = Houses[2].occupancy
      h3 = Houses[3].occupancy
      h4 = Houses[4].occupancy
      main_house_stock = Houses[3].__stock__
      len_main_house_stock = len(Houses[3].__stock__)
      if search_item!=None:
            all_search_fun = check_name_item(search_item,Houses)[1]
            for d in main_house_stock:
                  if d.is_name(search_item):
                        same+=1
      return Houses, {'main_house':len_main_house_stock, 1:h1, 2:h2, 3:h3, 4:h4, 'same_name_main_house':same, 'all_same_name_fun':all_search_fun, 'sum':sum((h1, h2, h3, h4))}
#result_dict = house_run(stock, 'original monitor', True)  
#print('FUNCION 1',*result_dict, sep='\n')
#print('STOCK', len(stock))
