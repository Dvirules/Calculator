from Extensions.extension import *
from Extensions.color import *


"""
This is a class that is used to build all dependency injections at the first initialization of the app, and serve it to the rest of it.
"""


class AllExtensions:
    extensions = {}

    for extension_class in Extension.__subclasses__():
        extensions.update({extension_class.extension_name: extension_class})

