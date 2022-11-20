from Operators.operator import *

"""
Class for the addition mathematical operation
"""


class Plus(Operator):
    operator = "+"
    priority = 1
    
    def __init__(self):
        pass

    def calculate(self, operand1, operand2):
        return float(operand1) + float(operand2)