import unittest, os, sys, datetime
cwd = os.getcwd()
sys.path.append(cwd)
from Milestone_7.classes import User, Employee, Warehouse, Item
import importlib

pkg="Milestone_7.classes"

class TestLoader(unittest.TestCase):
      def setUp(self):
            self.module = importlib.import_module(pkg)
            pass

      def test_classes_exists(self):
            
            self.assertIsNotNone(self.module.Warehouse)
            self.assertIsNotNone(self.module.User)
            self.assertIsNotNone(self.module.Employee)
            self.assertIsNotNone(self.module.Item)
      
      def test_children_class(self):
            self.assertTrue(self.module.User.__subclasscheck__(Employee))
            
      def test_User(self):
            user_anonymous = self.module.User()
            frank_user = self.module.User(user_name='Frank')
            pass_user = self.module.User(user_name='Jim', password='pass123')
            self.assertEqual(user_anonymous._name, 'Anonymous' )
            self.assertEqual(frank_user._name, 'Frank' )
            self.assertFalse(pass_user.authenticate('pass123'))

      def test_Employee(self):
            employee_anonymous = self.module.Employee()
            employee_reg = self.module.Employee('Marc', 'janis')
            employee_reg2 = self.module.Employee('Marc', 'janis',[{"user_name": "Marc", "password": "janis"}])
            #employee_reg.authenticate('janis')
            self.assertEqual(employee_anonymous._name, 'Anonymous' )
            self.assertIsNone(employee_anonymous.head_of)
            self.assertFalse(employee_anonymous.is_authenticated)
            self.assertFalse(employee_reg.is_authenticated)
            self.assertListEqual(employee_reg2.head_of, [{"user_name": "Marc", "password": "janis"}])
            #self.assertEqual(employee_reg.head_of, [] )
            #self.assertTrue(employee_reg.authenticate('janis'),employee_reg.is_authenticated)
            
      def test_Warehouse(self):
            warehouse_noid = self.module.Warehouse()
            warehouse = self.module.Warehouse(id=3)
            obj = {'state':'new','category': 'mouse', 'date_of_stock': datetime.datetime(2020, 1, 1)}
            item = self.module.Item(**obj)
            
            self.assertIsNone(warehouse_noid._id)
            self.assertEqual(warehouse._id, 3)
            self.assertListEqual(warehouse.stock, [])
            self.assertEqual(warehouse.occupancy(), len(warehouse.stock))
            warehouse.add_item(item)
            self.assertEqual(warehouse.occupancy(), 1)


if __name__ == "__main__":
      unittest.main()