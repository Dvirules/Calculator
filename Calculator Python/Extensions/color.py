from Extensions.extension import *
import json

"""
Class for the addition mathematical operation
"""


class Color(Extension):
    extension_name = "color"

    def __init__(self):
        pass

    def take_action(self, result):
        if float(result) % 2 == 0:
            return str({"result": result, "color": "Green"})
        else:
            return str({"result": result, "color": "Red"})
