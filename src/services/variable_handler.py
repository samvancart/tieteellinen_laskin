from services.variable import Variable


class VariableHandler:
    """Class for handling variables."""

    def __init__(self):
        self.variables_dict = []
        self.created_vars = 0

    def create_variable(self, entry):
        """Creates a variable and adds it to variables list

        Args:
            entry: variable value e.g. (var=5)

        Returns:
            List of variables as dictionaries
        """
        value = entry.split('=')[1]
        if value == '':
            return None
        self.created_vars += 1
        var_id = self.created_vars
        variable = Variable('var_'+str(var_id), value, var_id)
        return self.variables_dict.append(variable.get_variable_as_dict())

    def get_variables_as_dict(self):
        return self.variables_dict

    def get_created_vars(self):
        return self.created_vars

    def get_variable_dict_by_id(self, var_id):
        for variable in self.variables_dict:
            if variable['id'] == var_id:
                return variable
        return None

    def get_variable_buttons_list(self, buttons_in_row=3):
        """Creates 2-dimensional list (rows, columns) of variables.
        
        Args:
            buttons_in_row: The number of variables in each list.

        Returns:
            2-dimensional list
        """
        buttons = []
        rows = []
        index = 0
        counter = 0
        while index < len(self.variables_dict):
            counter += 1
            variable = self.variables_dict[index]
            if counter == buttons_in_row:
                rows.append(variable)
                buttons.append(rows)
                rows = []
                counter = 0
            else:
                rows.append(variable)
            index += 1
        if rows:
            buttons.append(rows)
        return buttons
