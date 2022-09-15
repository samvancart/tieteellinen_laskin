from importlib.metadata import SelectableGroups
import unittest
from kpn import Kpn

class TestKpn(unittest.TestCase):
    def setUp(self):
        self.kpn = Kpn()

    def test_get_reverse_polish(self):
        self.assertEqual(self.kpn.get_reverse_polish('3+4'),
            ['3', '4', '+'])
        self.assertEqual(self.kpn.get_reverse_polish('3+4*2'),
            ['3', '4', '2', '*', '+'])
        self.assertEqual(self.kpn.get_reverse_polish('3+4*2/2'),
            ['3', '4', '2', '*', '2', '/', '+'])
        self.assertEqual(self.kpn.get_reverse_polish('3+4*2/(1-5)^2^3'),
            ['3', '4', '2', '*', '1', '5', '-', '2', '3', '^', '^', '/', '+'])

        
        
        