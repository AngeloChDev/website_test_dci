from abc import ABC, abstractmethod

class Task(ABC):

      def __init__(self):
            self.username = input('Give a username : ')
            self._Greet_User()
      
      def _Set_Actions(self, A1, A2):
            _MENU_ACTIONS='select one action:\n1-{} \n2-{}\n3- Quit\n'.format(A1, A2)
            return _MENU_ACTIONS
            
      def _Greet_User(self):
            return print(f'Welcome {self.username}')

      def _Menu(self):
            user_action= input(self._MENU_ACTIONS)
            try:
                  action= int(user_action)
            except Exception as e:
                  print(e)
                  return True
            if action==3:
                  return print(f'Thank you for your visit, {self.username}')
            elif action==1:
                  return self._Action1()
            elif action==2:
                  obj = input('What is the name of the item?  ').strip()
                  return self._Action2(obj)
      
      def _Order_Loop(self):
            x=True
            while x :
                  x = self._Menu()
      
      @abstractmethod
      def _Action1(self):
            pass
      
      @abstractmethod
      def _Action2(self):
            pass
            
      def _Confirm_Order(self, item_tobuy, item_disponible):
            order_confirm = input('You want buy some of this items ? tap yes or no :\n')   
            if order_confirm=='no':
                  print(f'Thank you for your visit, {self.username}')
                  return False
            elif order_confirm=='yes':
                  n_tobuy=input('How many items you would like to buy ? \n')
                  if int(n_tobuy) <= item_disponible:
                        print(f'Your order has been placed!\nNumber of item : {n_tobuy}\nItem : {item_tobuy}')
                        return True
                  elif int(n_tobuy) > item_disponible:
                        print('You choosed a number of items more hight than the number of items in stock')
                        buy_all= input('Do you want to buy the maximum number of items available? tap yes or no\n')
                        if buy_all=='no':
                              print(f'Thank you for your visit, {self.username}')
                              return False
                        elif buy_all=='yes':
                              print(f'Your order has been placed!\nNumber of item : {item_disponible}\nItem : {item_tobuy}\n')
                              return True
                  else:
                        print(ValueError('ValueError in number of items input')) 
                        return True
            else:
                  print(ValueError('Error in order confirmation input'))
                  return True
            
            
