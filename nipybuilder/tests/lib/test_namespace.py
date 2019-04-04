"""
Test cases for Namespace class.
"""

import unittest
from nipybuilder.lib import Namespace

class NamespaceTest(unittest.TestCase):
    def test_attributes_set_from_data(self):
        ns = Namespace(first_name='John')
        self.assertEqual(ns.first_name, 'John')
        
    def test_element_get_returns_value(self):
        ns = Namespace(first_name='John')
        self.assertEqual(ns['first_name'], 'John')

    def test_element_set_updates_value(self):
        ns = Namespace(first_name='John')
        ns.last_name = 'Doe'
        self.assertEqual(ns['last_name'], 'Doe')
    
    
    def test_dir_returns_list_attr(self):    
        ns = Namespace(first_name='John')
        self.assertEqual(dir(ns), ['first_name'])
        
    def test_set_attribute_adds_attribute(self):
        ns = Namespace(first_name='John')
        ns.last_name = 'Doe'
        self.assertEqual(ns.last_name, 'Doe')
        self.assertEqual(dir(ns), ['first_name', 'last_name'])
        
    def test_del_attribute_removes_attribute(self):
        ns = Namespace(first_name='John', last_name='Doe')
        del(ns.last_name)
        self.assertEqual(dir(ns), ['first_name'])
        
    def test_str_gets_string_representation(self):
        ns = Namespace(first_name='John')
        s = str(ns)
        self.assertEqual(s, "Namespace({'first_name': 'John'})")
        
    def test_call_instance_returns_attribute_value(self):
        ns = Namespace(first_name='John')
        self.assertEqual(ns('first_name'), 'John')

    def test_call_instance_returns_default_positional_value_if_attribue_missing(self):
        ns = Namespace(first_name='John')
        self.assertEqual(ns('last_name', 'Doe'), 'Doe')

    def test_call_instance_returns_default_key_value_if_attribue_missing(self):
        ns = Namespace(first_name='John')
        self.assertEqual(ns('last_name', default='Doe'), 'Doe')
        self.assertEqual(ns(name='last_name', default='Doe'), 'Doe')

if __name__ == '__main__':
    unittest.main()
