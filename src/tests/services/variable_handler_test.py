import unittest
from services.variable_handler import VariableHandler


class TestVariableHandler(unittest.TestCase):
    def setUp(self):
        self.variable_handler = VariableHandler()

    def test_create_variable(self):
        self.assertEqual(self.variable_handler.create_variable('var='),
                         None)
        self.assertEqual(self.variable_handler.create_variable('var=3('),
                         'error')

        self.variable_handler.create_variable('var=1+2')
        self.assertEqual(self.variable_handler.get_variables_as_dict(),
                         [{'name': 'var_1', 'value': '1+2', 'id': 1}])

    def test_created_variables_value_is_correct(self):
        self.assertEqual(self.variable_handler.get_created_vars(),
                         0)
        self.variable_handler.create_variable('var=2+3')
        self.assertEqual(self.variable_handler.get_created_vars(),
                         1)

    def test_get_variable_dict_by_id(self):
        self.variable_handler.create_variable('var=3+4')
        self.variable_handler.create_variable('var=5')
        self.assertEqual(self.variable_handler.get_variable_dict_by_id(2),
                         {'name': 'var_2', 'value': '5', 'id': 2})
        self.assertEqual(self.variable_handler.get_variable_dict_by_id(0),
                         None)

    def test_get_variable_buttons_list(self):
        self.variable_handler.create_variable('var=1')
        self.variable_handler.create_variable('var=2')
        self.assertEqual(self.variable_handler.get_variable_buttons_list(),
                         [[{'name': 'var_1', 'value': '1', 'id': 1},
                           {'name': 'var_2', 'value': '2', 'id': 2}]
                          ])
        self.variable_handler.create_variable('var=3')
        self.variable_handler.create_variable('var=4')
        self.assertEqual(self.variable_handler.get_variable_buttons_list(),
                         [[{'name': 'var_1', 'value': '1', 'id': 1},
                           {'name': 'var_2', 'value': '2', 'id': 2},
                           {'name': 'var_3', 'value': '3', 'id': 3}],
                          [{'name': 'var_4', 'value': '4', 'id': 4}]
                          ])
        self.setUp()
        self.variable_handler.create_variable('var=1')
        self.variable_handler.create_variable('var=2')
        self.variable_handler.create_variable('var=3')
        self.assertEqual(self.variable_handler.get_variable_buttons_list(),
                         [[{'name': 'var_1', 'value': '1', 'id': 1},
                           {'name': 'var_2', 'value': '2', 'id': 2},
                           {'name': 'var_3', 'value': '3', 'id': 3}]])
