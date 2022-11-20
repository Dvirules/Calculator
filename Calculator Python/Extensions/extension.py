from abc import ABC, abstractmethod

"""
The base class for all operators
"""


class Extension(ABC):

    @property
    @abstractmethod
    def extension_name(self):
        pass

    def __init__(self):
        pass

    @abstractmethod
    def take_action(self, result):
        pass


