import unittest, os, sys, datetime
from unittest.mock import patch, Mock
from datetime import datetime as Date
cwd = os.getcwd()
sys.path.append(cwd)
from Milestone_7 import query2, service
import importlib
################################################################
      # MOCK TEST
from contextlib import contextmanager

@contextmanager
def mock_input(mock):
      original_input = __builtins__.input
      __builtins__.input = lambda _: mock
      yield
      __builtins__.input = original_input


@contextmanager
def mock_output(mock):
    original_print = __builtins__.print
    __builtins__.print = lambda *value: [mock.append(val) for val in value]
    yield
    __builtins__.print = original_print


#fnc="Milestone_4.query"
#pkg="Milestone_7.classes"
class TestLoader(unittest.TestCase):
      def setUp(self):
            pkg="Milestone_7.classes"
            self.module = importlib.import_module(pkg)
            pass
      def tearDown(self):
            pass

      def test_naming_of_all_classes(self):
            self.assertTrue(self.module.__getattribute__('Warehouse'))
            self.assertTrue(self.module.__getattribute__('User'))
            self.assertTrue(self.module.__getattribute__('Employee'))
            self.assertTrue(self.module.__getattribute__('Item'))
      
      def test_class_inheritance(self):
            self.assertTrue(self.module.User.__subclasscheck__(self.module.Employee))
            
      def test_User(self):
            '''User class test'''
            anonymous = self.module.User()
            frank_user = self.module.User(user_name='Frank')
            pass_user = self.module.User(user_name='Jim', password='pass123')
            #test anonymous user, 'Franc']
            self.assertEqual(anonymous._name, 'Anonymous' )
            self.assertFalse(anonymous.is_authenticated)
            self.assertFalse(anonymous.authenticate('Anony123'))
            #test user with user name 
            self.assertEqual(frank_user._name, 'Frank' )
            self.assertFalse(frank_user.is_authenticated)
            self.assertFalse(frank_user.authenticate('guest'))
            # test user with user name password 
            self.assertFalse(pass_user.is_authenticated)
            self.assertFalse(pass_user.authenticate('pass123'))

      def test_Employee(self):
            '''Employee class test'''
            anonymous = self.module.Employee()
            registred_employee = self.module.Employee('Jeremy')
            header_employee = self.module.Employee('Juno','compte', [registred_employee])
            #test anonymous employee
            self.assertEqual(anonymous._name, 'Anonymous' )
            self.assertIsNone(anonymous.head_of)
            self.assertFalse(anonymous.is_authenticated)
            self.assertFalse(anonymous.authenticate('Anony123'))
            #test employee with user name 
            self.assertFalse(registred_employee.is_authenticated)
            self.assertEqual(registred_employee.head_of, [] )
            registred_employee.authenticate('coppers')
            self.assertTrue(registred_employee.is_authenticated)
            # test employee with head of  
            self.assertFalse(header_employee.is_authenticated)
            header_employee.authenticate('compte')
            self.assertListEqual(header_employee.head_of, [registred_employee])
            
      def test_Warehouse(self):
            warehouse_noid = self.module.Warehouse()
            warehouse = self.module.Warehouse(new_id=3)
            obj = {'state':'new','category': 'mouse', 'date_of_stock': datetime.datetime(2020, 1, 1)}
            item = self.module.Item(**obj)
            obj2 = {'state':'Almost new','category': 'desktop', 'date_of_stock': datetime.datetime(2020, 1, 1)}
            item2 = self.module.Item(**obj2)
            self.assertIsNone(warehouse_noid._id)
            self.assertEqual(warehouse._id, 3)
            self.assertListEqual(warehouse.stock, [])
            self.assertEqual(warehouse.occupancy, len(warehouse.stock))
            warehouse.add_item(item)
            warehouse.add_item(item2)
            self.assertEqual(warehouse.occupancy, 2)
            self.assertListEqual(warehouse.search('new mouse'),[item])
            self.assertListEqual(warehouse.search('Almost NEW desktop'), [item2])
            self.assertListEqual(warehouse.search('ALMOST NEW DESKTOP'), [item2])
            
      def test_Item(self):
            obj = {'state':'Almost new','category': 'Desktop', 'date_of_stock': datetime.datetime(2020, 1, 1)}
            item = self.module.Item(**obj)
            self.assertEqual(item.state, 'Almost new')
            self.assertEqual(item.category, 'Desktop')
            self.assertEqual(item.date_of_stock, datetime.datetime(2020, 1, 1))
            self.assertEqual(item.__str__(), f'{item.state} {item.category}')
      
      def test_Query(self):
            with mock_input('Guest'):
                  guest_user = query2.get_user() 
            self.assertEqual(guest_user._name, 'Guest')
            self.assertTrue(isinstance(guest_user, self.module.User))
            self.assertFalse(isinstance(guest_user, self.module.Employee))
            query2.username=''

      def test_query_employe(self):      
            with mock_input('Jeremy'):
                  employee_user = query2.get_user() 
            self.assertEqual(employee_user._name, 'Jeremy')
            self.assertTrue(isinstance(employee_user, self.module.User))
            self.assertTrue(isinstance(employee_user, self.module.Employee))
            query2.username=''
            
      def test_get_selected_operation(self):
            answer=[]
            with mock_input(1):
                  with mock_output(answer):
                        query2._Menu() 
                        query2._Action1()
            self.assertEqual(answer[0][-1] , answer[1][-1])
            self.assertEqual(query2._Menu.ACTIONS , query2.MENU_ACTIONS)

      def test_list_items_by_warehouse(self):
            self.assertEqual(query2._Action1()[0], "Listed 5000 items\n")
            self.assertEqual(''.join(query2._Action1()[1]),"Total items in warehouse 1:\n1346\nTotal items in warehouse 2:\n1258\nTotal items in warehouse 3:\n1173\nTotal items in warehouse 4:\n1223\n")

      
      def test_search_item(self):
            data =service.house_run(search_item='original monitor')
            warehouses = data[0]
            found_h1 = len(warehouses[1].search('original monitor'))
            found_h2 = len(warehouses[2].search('original monitor'))
            found_h3 = len(warehouses[3].search('original monitor'))
            found_h4 = len(warehouses[4].search('original monitor'))
            all_output = {1:found_h1, 2:found_h2, 3:found_h3, 4:found_h4}
            output_true = data[1]['all_same_name_fun']
            self.assertDictEqual(all_output, output_true)
            with patch('builtins.input',side_effect=['test']):      
                  user_search_infullmagazine = query2._Action2('original monitor')
                  self.assertEqual(user_search_infullmagazine[1], data[1]['same_name_main_house'])
            self.assertEqual( len(warehouses[1].stock),warehouses[1].occupancy)
            self.assertEqual( len(warehouses[2].stock), warehouses[2].occupancy)
            self.assertEqual( len(warehouses[3].stock),warehouses[3].occupancy)
            self.assertEqual( len(warehouses[4].stock),warehouses[4].occupancy)

      def test_employee_only(self):
            with patch('builtins.input',side_effect=['Jeremy',2,'original monitor','yes','coppers',2, 'no']):
                  answer=[]
                  with mock_output(answer):
                        employe_order = query2.order('yes','original monitor',11)
            self.assertTrue(answer)
            

                        


if __name__ == "__main__":
      unittest.main()