import re


class InputHandler:
    """Class to validate and handle input."""

    def __init__(self):
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'pi', '-e'
                        '-0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9', '-pi', 'e']

        self.operator_regex = r"(?<!e)[-+*/^]+"
        self.symbol_regex = r"[(),]"
        self.number_regex = r"[\d]*[\.]\d*(e[+-])*\d*|\d+(e[+-])*\d*|pi|(e[+-])\d+"
        self.function_regex = r"sin+|cos+|tan+|sqrt+|min+|max+"

        self.minuses_and_pluses_in_front_of_number_regex = \
            r"^[+-]+[-+|+-]*\d*(pi)*(e[+-])*[\.]?[\d]*(e[+-])*\d*"
        self.minuses_and_pluses_in_front_of_function_regex = r"^[+-]+[-+|+-]*(sqrt|sin|tan|cos)"
        self.minus_or_plus_after_parenthesis_or_operator_regex = \
            r"(?<=[\(\^\*\/])[+]*[-]+[-+|+-]*\d+[\.]?[\d]*|(?<=[\(\^\*\/])[+]*[-]+[-+|+-]*(pi)+"

    def get_operator_regex(self):
        no_operator_after_right_parenthesis = r"[\)]+\d+"
        no_operator_before_left_parenthesis = r"(\d+|\)+)\(+"
        no_operator_before_function = r"(\d+|pi)(sqrt|sin|tan|cos)"
        no_parenthesis_after_function = r"(sqrt|sin|tan|cos)[^\(]"
        two_operators = r"[\+\-\*\/\^]+[\*\/\^]]*"
        no_number_after_operator = r"\d+[-+*/^]+$"

        return [no_operator_after_right_parenthesis,
                no_operator_before_left_parenthesis,
                two_operators,
                no_parenthesis_after_function,
                no_operator_before_function,
                no_number_after_operator,
                ]

    def get_decimal_point_regex(self):
        more_than_one_decimal_point = r"\.[^\+\-\*\/\^]*\.+"
        nothing_after_decimal_point = r"\d+\.$"
        operator_after_decimal_point = r"\.[-+*^/]"
        number_or_decimal_before_or_after_pi = r"\d+(pi)|(pi)\d|(pi)\.|\.(pi|-pi|\+pi)"
        function_after_decimal_point = \
            r"\.(sin|-sin|\+sin)|\.(cos|-cos|\+cos)|\.(tan|-tan|\+tan)|\.(sqrt|-sqrt|\+sqrt)"

        return [more_than_one_decimal_point,
                nothing_after_decimal_point,
                operator_after_decimal_point,
                number_or_decimal_before_or_after_pi,
                function_after_decimal_point,
                ]

    def get_e_regex(self):
        no_plus_or_minus_after_e = r"e[*/^()]|e(sin)|e(cos)|e(tan)|e(sqrt)|e(pi)"
        multiple_e = r"e+e"
        decimal_point_after_e = r"e[-+]\d*\.\d*"
        function_after_e = r"e[-+](sin)|e[-+](cos)e[-+](tan)|e[-+](sqrt)|e[-+](pi)"

        return [no_plus_or_minus_after_e,
                multiple_e,
                decimal_point_after_e,
                function_after_e,
                ]

    def get_error_regex(self):
        error = r"error"

        return [error]

    def get_regex_list(self):
        """Input validation.

        Returns:
            List of regular expressions for validating input.
        """
        error_regex = self.get_error_regex()
        operator_regex = self.get_operator_regex()
        decimal_point_regex = self.get_decimal_point_regex()
        e_regex = self.get_e_regex()

        regex_list = operator_regex + decimal_point_regex + e_regex + error_regex

        return regex_list

    def validate_input(self, regex_list, str_input):
        for regex in regex_list:
            string = re.findall(regex, str_input)
            if string != []:
                return False
        return True

    def is_number(self, token):
        if token in ('pi', '-pi'):
            return True
        for character in token:
            if character in self.numbers:
                return True
        return False

    def trim_matches_list(self, reference_list, list_to_clean, index):
        """Remove unwanted overlapping matches from list

        Args:
            reference_list: The higher hierarchy list to compare to.
            list_to_clean: The list that will have unwanted matches removed.
            index: The index of the tuple to compare (0 (start of string) or 1 (end of string)).

        Returns:
            List, trimmed list with unwanted matches removed.
        """
        if not reference_list:
            return list_to_clean
        trimmed_list = []
        positions_list = []
        for ref_item in reference_list:
            for item_index, item in enumerate(list_to_clean):
                if ref_item[index] == item[index]:
                    positions_list.append(item_index)
        for item_index, item in enumerate(list_to_clean):
            if not item_index in positions_list:
                trimmed_list.append(item)
        return trimmed_list

    def get_matches_list(self, str_input, regex_list):
        """Finds all matches and their start and end indexes.

        Args:
            str_input: the string to search.
            regex_list: list of regular expressions to apply.

        Returns:
            List, containing tuples of form (start_index_of_match, end_index_of_match).
        """
        matches_list = []
        for regex in regex_list:
            matches = re.finditer(regex, str_input)
            for match in matches:
                matches_list.append(match.span())
        return matches_list

    def combine_regex_to_list(self, str_input):
        """Defines regex patterns and combines lists of relevant matches into one list.

        Args:
            str_input: The string to search for matches.

        Returns:
            List, tuples of form (start_index_of_match, end_index_of_match)
        """

        minuses_list = [self.minuses_and_pluses_in_front_of_number_regex,
                        self.minus_or_plus_after_parenthesis_or_operator_regex,
                        self.minuses_and_pluses_in_front_of_function_regex]

        operators = self.get_matches_list(str_input, [self.operator_regex])
        symbols = self.get_matches_list(str_input, [self.symbol_regex])
        numbers = self.get_matches_list(str_input, [self.number_regex])
        negatives = self.get_matches_list(str_input, minuses_list)
        functions = self.get_matches_list(str_input, [self.function_regex])

        operators = self.trim_matches_list(negatives, operators, 0)
        functions = self.trim_matches_list(negatives, functions, 1)
        numbers = self.trim_matches_list(negatives, numbers, 1)

        combined_indexes = negatives + operators + symbols + numbers + functions
        return combined_indexes

    def str_input_to_list(self, str_input):
        """Transforms a string into a list
            that can be processed by the shunting_yard method in Rpn class.

        Args:
            str_input: The string to process.

        Returns:
            List, in processable form.
        """
        index_list = self.combine_regex_to_list(str_input)
        table = {key: (key, val) for key, val in index_list}
        input_list = []
        try:
            iterations = max(table)+1
        except ValueError:
            return ['error']
        for index in range(iterations):
            try:
                start = table[index][0]
                end = table[index][1]
                input_list.append(str_input[start:end])
            except KeyError:
                continue
        # print('trimmed', input_list)
        trimmed_list = self.trim_operators(input_list)
        return trimmed_list

    def trim_operators(self, input_list):
        """Removes consecutive '+' and '-' operators and replaces them with either '-', '+' or ''.

        Args:
            input_list: The list to be processed.

        Returns:
            List, with consecutive '+' and '-' operators replaced.
        """
        trimmed_list = []
        # print('input_list', input_list)
        for item in input_list:
            pos = len(item)
            if item[0] in ('+', '-'):
                if item[-1] not in ('-', '+'):
                    pos = self.get_position(item)
                    operator = self.get_operator(item[0:pos], True)
                    trimmed_list.append(operator + item[pos:len(item)])
                else:
                    operator = self.get_operator(item[0:pos], False)
                    trimmed_list.append(operator)
            elif item[0] in ('*', '/', '^'):
                trimmed_list.append(item[0])
            else:
                trimmed_list.append(item)
        # print('trimmed_list', trimmed_list)
        return trimmed_list

    def get_position(self, str_item):
        """Gets the position of the last operator token while ignoring token 'e'.

        Args:
            str_item: The string to process.

        Returns:
            Int, index + 1 of last operator token.
        """
        new_str_item = str_item
        for index, char in (list(enumerate(str_item))):
            if char in 'e':
                new_str_item = str_item[0:index+1]
                break
        for index, char in reversed(list(enumerate(new_str_item))):
            if char in ('-', '+'):
                return index+1
        return 1

    def get_operator(self, str_item, number):
        """Gets the operator that will replace the consecutive operators in the list

        Args:
            str_item: The string of consecutive operator tokens ('+' or '-') (eg. '+--').
            number: Boolean, True if the list item, that will be replaced, contains a number token.

        Returns:
            String, operator token ('-' or '+') or ''.
        """
        neg = False
        for item in str_item:
            if item == '-':
                neg = not neg
        if not neg and not number:
            return '+'
        if not neg and number:
            return ''
        return '-'
