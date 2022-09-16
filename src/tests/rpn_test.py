import unittest
from rpn import Rpn

class TestRpn(unittest.TestCase):
    def setUp(self):
        self.rpn = Rpn()

    def test_get_reverse_polish(self):
        self.assertEqual(self.rpn.get_reverse_polish('3+4'),
            ['3', '4', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('(3+4)'),
            ['3', '4', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2'),
            ['3', '4', '2', '*', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/2'),
            ['3', '4', '2', '*', '2', '/', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/(1-5)^2^3'),
            ['3', '4', '2', '*', '1', '5', '-', '2', '3', '^', '^', '/', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('((1)*2)'),
            ['1', '2', '*'])
        self.assertEqual(self.rpn.get_reverse_polish('((1)*)2'),
            None)
        self.assertEqual(self.rpn.get_reverse_polish('1**2'),
            None)
        # Make method clean_input for special case
        # self.assertEqual(self.kpn.get_reverse_polish('+++1'),
        #     ['1'])       
        self.assertEqual(self.rpn.get_reverse_polish('()'),
            None)
        self.assertEqual(self.rpn.get_reverse_polish('((()))'),
            None)

        """Test for mismatched parenthesis"""
        self.assertEqual(self.rpn.get_reverse_polish('(3+4'),
            None)
        self.assertEqual(self.rpn.get_reverse_polish('3+4)'),
            None)
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/1-5)^2)^3'),
            None)
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/(1-5^2^3'),
            None)
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/(1-5(^2^3'),
            None)
        self.assertEqual(self.rpn.get_reverse_polish('())'),
            None)
        self.assertEqual(self.rpn.get_reverse_polish('(()'),
            None)
        
        
 
        
        
        