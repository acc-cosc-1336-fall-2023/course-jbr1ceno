#
import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget


class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        dictionaryTest = {}
        widgetTestName = 'Widget1'
        quantity = 10
        add_inventory(widgetTestName, quantity, dictionaryTest)
        self.assertEqual({'Widget1':10}, dictionaryTest)
        print(dictionaryTest)
        add_inventory(widgetTestName, 25, dictionaryTest)
        self.assertEqual({'Widget1':35}, dictionaryTest)
        print(dictionaryTest)
        add_inventory(widgetTestName, -10, dictionaryTest)
        self.assertEqual({'Widget1':25}, dictionaryTest)
        
        print(dictionaryTest)
        
    
    def test_remove_inventory_widget(self):
        dictTest = {}
        add_inventory('Widget1', 10, dictTest)
        self.assertEqual({'Widget1':10}, dictTest)
        add_inventory('Widget2', 20, dictTest)
        self.assertEqual({'Widget1':10, 'Widget2':20}, dictTest)
        #self.assertEqual(2, len(dictTest))
        print(dictTest)
        print(remove_inventory_widget('Widget1', dictTest))
        #self.assertEqual({'Widget2':20}, dictTest)
        self.assertEqual(1, len(dictTest))
        print(dictTest)
