from Operators.operator import *
from Operators.plus import *
from Operators.minus import *
from Operators.multiplication import *
from Operators.division import *
from Operators.power import *

"""
This is a class that is used to build all dependency injections at the first initialization of the app, and serve it to the rest of it.
"""


class SubClasses:
    classes = {}

    for operation_class in Operator.__subclasses__():
        classes.update({operation_class.operator: operation_class})

