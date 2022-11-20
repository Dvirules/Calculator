from sub_classes import *
from all_extensions import *

"""
The main logic class of the app - used for the calculation operation
"""


class Main:
    classes = SubClasses.classes
    all_extensions = AllExtensions.extensions

    def run_calc(self, expression):
        """
        :param expression: The string mathematical expression passed by the user
        :return: The result of the expression
        """
        num_of_operators = self.check_expr(expression)
        if not num_of_operators.isdigit(): return num_of_operators
        num_of_operators = int(num_of_operators)

        for i in range(num_of_operators):
            highest_priority_operator = self.priority_check(expression)
            highest_priority_operator_index = expression.find(highest_priority_operator)
            left_operand = ""
            left_counter = highest_priority_operator_index - 1
            right_operand = ""
            right_counter = highest_priority_operator_index + 1

            while left_counter >= 0 and expression[left_counter] not in self.classes.keys():
                left_counter -= 1
            left_operand = expression[left_counter + 1:highest_priority_operator_index]

            while right_counter <= len(expression) - 1 and expression[right_counter] not in self.classes.keys():
                right_operand += expression[right_counter]
                right_counter += 1

            expression = expression[:left_counter + 1] + str(self.classes[highest_priority_operator]().calculate(left_operand, right_operand)) + expression[right_counter:]

        return expression


    def check_expr(self, expression):
        """
        :param expression: The string mathematical expression passed by the user
        :return: An error should an incorrect character was inserted in the expression, otherwise the number of operations in the expression
        """
        num_of_operators = 0
        for c in expression:
            if not c.isdigit() and c not in self.classes.keys() and c != '.':
                return "You have inserted an invalid expression. Please make sure your expression includes only numbers and supported mathematical operators."
            if c in self.classes.keys():
                num_of_operators += 1

        return str(num_of_operators)


    def priority_check(self, expression):
        """
        :param expression: The string mathematical expression passed by the user
        :return: The operation with the highest priority in the expression
        """
        highest_priority = -1
        highest_priority_operator = ''
        for c in expression:
            if c in self.classes.keys():
                if self.classes[c].priority > highest_priority:
                    highest_priority = self.classes[c].priority
                    highest_priority_operator = self.classes[c].operator

        return highest_priority_operator

    def extension_invoker(self, extension, result):
        if extension in self.all_extensions.keys():
            return self.all_extensions[extension]().take_action(result)
        else:
            return "Not a supported extension"


