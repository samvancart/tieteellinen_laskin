import unittest
from services.variable import Variable


class TestVariable(unittest.TestCase):
    def setUp(self):
        self.variable = Variable('var', 'sqrt(4)', 1)

    def test_get_name(self):
        self.assertEqual(self.variable.get_name(),
                         'var')

    def test_get_value(self):
        self.assertEqual(self.variable.get_value(),
                         'sqrt(4)')

    def test_get_id(self):
        self.assertEqual(self.variable.get_id(),
                         1)
