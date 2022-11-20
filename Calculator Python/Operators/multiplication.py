from Operators.operator import *

"""
Class for the multiplication mathematical operation
"""


class Multiplication(Operator):
    operator = "*"
    priority = 2

    def __init__(self):
        pass

    def calculate(self, operand1, operand2):
        return float(operand1) * float(operand2)