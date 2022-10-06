class Variable:
    """Class for creating variables."""

    def __init__(self, name, value, var_id):
        self.name = name
        self.value = value
        self.var_id = var_id
        self.variable_dict = {'name': self.name,
                              'value': self.value,
                              'id': self.var_id,
                              }

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_id(self):
        return self.var_id

    def get_variable(self):
        return self.variable_dict
