from abc import ABC, abstractmethod

class Task(ABC):

      def __init__(self):
            self.USERS=[]
            self.session = {'need_login':False, "logged":False}
            self.action1 = ''
            self.action2 = ''
            self.action3 = None
            self.username = input('Give a username : ')
            self._Greet_User()
      
      def _Set_Actions(self, A1, A2, A3=None):
            if A3==None:
                  quit_action = '3'
                  A3=''
            else:
                  quit_action='4'
            _MENU_ACTIONS='select one action:\n1-{} \n2-{}\n{}{}- Quit\n'.format(A1, A2,A3,quit_action)
            return _MENU_ACTIONS
      
      def login(self):
            passwd = input('\nWrite your password :')
            for i in self.USERS:
                  if self.username==i['user_name'] and passwd==i['password']:
                        return True
                  elif 'head_of' in list(i.keys()):
                        for j in i['head_of']:
                              if j['user_name']==self.username and j['password']==passwd:
                                    return True
                  
            return False
            
      def _Greet_User(self):
            return print(f'\nWelcome {self.username}')

      def _Menu(self):
            user_action= input(self._MENU_ACTIONS)
            try:
                  action= int(user_action)
            except Exception as e:
                  print(e)
                  return True
                  
            if action==1:
                  return self._Action1()
            elif action==2:
                  obj = input('\nWhat is the name of the item?  ').strip()
                  return self._Action2(obj.lower())
            elif self.action3==None and action==3:
                  return print(f'\nThank you for your visit, {self.username}')
            elif self.action3 != None:
                  if action==3:
                        return self._Action3()
                  elif action==4:
                        return print(f'\nThank you for your visit, {self.username}')
                  else:
                        print('Action input value not valid')
                        return True
            else:
                  print('Action input value not valid')
                  return True
                  
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
      
      @abstractmethod
      def _Action3(self):
            pass
            
      def _Confirm_Order(self, item_tobuy, item_disponible):
            order_confirm = input('\nYou want buy some of this items ? tap yes or no :\n')   
            if order_confirm=='no':
                  print(f'\nThank you for your visit, {self.username}')
                  return False
            elif order_confirm=='yes':
                  if self.session["need_login"]==True:
                        chance= 0
                        while chance < 3 and self.session["logged"]==False: 
                              self.session["logged"] = self.login()
                              chance+=1
                        if chance>=3:
                              return self._Order_Loop()
                  n_tobuy=input('\nHow many items you would like to buy ? \n')
                  if int(n_tobuy) <= item_disponible:
                        print(f'\nYour order has been placed!\nNumber of item : {n_tobuy}\nItem : {item_tobuy}')
                        return True
                  elif int(n_tobuy) > item_disponible:
                        print('\nYou choosed a number of items more hight than the number of items in stock')
                        buy_all= input('Do you want to buy the maximum number of items available? tap yes or no\n')
                        if buy_all=='no':
                              print(f'\nThank you for your visit, {self.username}')
                              return False
                        elif buy_all=='yes':
                              print(f'\nYour order has been placed!\nNumber of item : {item_disponible}\nItem : {item_tobuy}\n')
                              return True
                  else:
                        print(ValueError('ValueError in number of items input')) 
                        return True
            else:
                  print(ValueError('Error in order confirmation input'))
                  return True
            
            
