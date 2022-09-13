import unittest
from kpn import Kpn

class TestKpn(unittest.TestCase):
    def setUp(self):
        print('Set up')

    def test_get_reverse_polish(self):
        my_kpn = Kpn()
        self.assertEqual(my_kpn.get_reverse_polish('3+4*2/(1-5)^2^3'),
            ['3', '4', '2', '*', '1', '5', '-', '2', '3', '^', '^', '/', '+'])