from Operators.operator import *

"""
Class for the power mathematical operation
"""


class Power(Operator):
    operator = "^"
    priority = 3

    def __init__(self):
        pass

    def calculate(self, operand1, operand2):
        return pow(float(operand1), float(operand2))