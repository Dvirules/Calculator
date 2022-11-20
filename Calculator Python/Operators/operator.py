from abc import ABC, abstractmethod

"""
The base class for all operators
"""


class Operator(ABC):

    @property
    @abstractmethod
    def operator(self):
        pass

    @property
    @abstractmethod
    def priority(self):
        pass

    def __init__(self):
        pass

    @abstractmethod
    def calculate(self, operand1, operand2):
        """
        :param operand1: The first operand in the equation
        :param operand2: The second operand in the equation
        :return: The result of the mathematical specific operator between the two operands
        """
        pass


