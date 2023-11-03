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


    #HW 8
    def test_find_intersection_set(self): #finds intersection of sets to display names of students who play both sports
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

        self.assertEqual(baseball.intersection(basketball), set(['Carmen','Alicia']))
        print(baseball.intersection(basketball))
    
    def test_find_union_set(self): #finds union of sets to display names of students who played either baseball or basketball
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

        self.assertEqual(baseball.union(basketball), set(['Jodi', 'Carmen', 'Aida', 'Alicia', 'Eva', 'Sarah']))
        print(baseball.union(basketball))

    def test_find_difference_set_baseball_basketball(self): #finds difference of baseball and basketball sets to display the names of students who play baseball but not basket ball
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

        self.assertEqual(baseball.difference(basketball), set(['Jodi','Aida']))
        print(baseball.difference(basketball))

    def test_find_difference_set_basketball_baseball(self): #finds difference of basketball and baseball sets to display the names of students who play basketball but not base ball
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

        self.assertEqual(basketball.difference(baseball), set(['Eva','Sarah']))
        self.assertEqual(baseball.difference(basketball), set(['Jodi','Aida']))

        print(basketball.difference(baseball))
        print(baseball.difference(basketball))

    def test_find_symmetric_difference(self): #finds symmetric difference of the basketball and baseball sets to display the names of students who play one sport but not both
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

        self.assertEqual(baseball.symmetric_difference(basketball), set(['Jodi', 'Aida', 'Eva', 'Sarah']))

        print(baseball.symmetric_difference(basketball))
