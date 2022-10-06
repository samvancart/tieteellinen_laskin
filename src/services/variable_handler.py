from services.variable import Variable


class VariableHandler:
    """Class for handling variables."""

    def __init__(self):
        self.variables_dict = []
        self.created_vars = 0

    def create_variable(self, entry):
        value = entry.split('=')[1]
        if value == '':
            return None
        self.created_vars += 1
        var_id = self.created_vars
        variable = Variable('var_'+str(var_id), value, var_id)
        self.variables_dict.append(variable.get_variable())

    def get_variables_as_dict(self):
        return self.variables_dict

    def get_created_vars(self):
        return self.created_vars

    def get_variable_dict_by_id(self, var_id):
        for variable in self.variables_dict:
            if variable['id'] == var_id:
                return variable
        return None
