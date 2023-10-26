from abc import ABC, abstractmethod

class Task(ABC):

      def __init__(self):
            self.USERS=[]
            self.session = {'need_login':False, "logged":False, "category":dict(), 'cache': []}
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
            self.session['cache'].append(f'You tried to login whith password : {passwd}')
            for i in self.USERS:
                  if self.username==i['user_name'] and passwd==i['password']:
                        return True
                  elif 'head_of' in list(i.keys()):
                        for j in i['head_of']:
                              if j['user_name']==self.username and j['password']==passwd:
                                    return True
            self.session['cache'].append('Login refused')
            return False
      
      def shoot_down(self):
            if self.session["need_login"]:
                  continue_ = input('You want to continue ? yes / no\n')
                  if continue_=='yes':
                        self.session['cache'].append('You procede')
                        return True
                  elif continue_=='no':
                        self.session['cache'].append('You are shooting down the software')
                        print(*self.session['cache'], sep='\n')
                        del self.session 
            print(f'\nThank you for your visit, {self.username}')
            return False
            
                  
            
      def _Greet_User(self):
            return print(f'\nWelcome {self.username}')

      def _Menu(self):
            user_action= input(self._MENU_ACTIONS)
            try:
                  action= int(user_action)
            except Exception as e:
                  print(e)
                  return self.shoot_down()
                  
            if action==1:
                  return self._Action1()
            elif action==2:
                  obj = input('\nWhat is the name of the item?  ').strip()
                  return self._Action2(obj.lower())
            elif self.action3==None and action==3:
                  return self.shoot_down()
            elif self.action3 != None:
                  if action==3:
                        return self._Action3()
                  elif action==4:
                        return self.shoot_down()
                  else:
                        print('Action input value not valid')
                        return self.shoot_down()
            else:
                  print('Action input value not valid')
                  return self.shoot_down()
                  
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
                  self.session['cache'].append('You refused to buy')
                  return self.shoot_down()
            elif order_confirm=='yes':
                  self.session['cache'].append('You accepted to buy')
                  if self.session["need_login"]==True:
                        while self.session["logged"]==False: 
                              self.session["logged"] = self.login()
                  self.session['cache'].append('Login accepted')
                  n_tobuy=input('\nHow many items you would like to buy ? \n')
                  while not n_tobuy.isnumeric() or int(n_tobuy) <= 0:
                        n_tobuy=input('\nHow many items you would like to buy? \nPlease enter a numerical input greater than 0')
                  if int(n_tobuy) <= item_disponible:
                        print(f'\nYour order has been placed!\nNumber of item : {n_tobuy}\nItem : {item_tobuy}')
                        self.session['cache'].append(f'You had bought : {n_tobuy} ; {item_tobuy}')
                        return self.shoot_down()
                  elif int(n_tobuy) > item_disponible:
                        print('\nYou choosed a number of items more hight than the number of items in stock')
                        buy_all= input('Do you want to buy the maximum number of items available? tap yes or no\n')
                        self.session['cache'].append('You selected a number of items not in stock')
                        if buy_all=='no':
                              self.session['cache'].append('You refused to buy the dsponible number of items')
                              return self.shoot_down()
                        elif buy_all=='yes':
                              print(f'\nYour order has been placed!\nNumber of item : {item_disponible}\nItem : {item_tobuy}\n')
                              self.session['cache'].append(f'You accepted to buy the dsponible number of items : {item_disponible} ; {item_tobuy}')
                              
                              return self.shoot_down()
                        else:
                              print(ValueError('ValueError in confirmation input')) 
                              return self.shoot_down()
            else:
                  print(ValueError('Error in order confirmation input'))
                  return self.shoot_down()
            
            
