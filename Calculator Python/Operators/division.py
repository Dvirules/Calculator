from Operators.operator import *

"""
Class for the division mathematical operation
"""

class Division(Operator):
    operator = ":"
    priority = 2

    def __init__(self):
        pass

    def calculate(self, operand1, operand2):
        return float(operand1) / float(operand2)