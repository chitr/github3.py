"""
github3.structs
===============

Contains the OrderedDict class if we're not running python 3

"""

try:
    from collections import OrderedDict
except ImportError:
    class OrderedDict(dict):
        def __init__(self, items=[]):
            super(OrderedDict, self).__init__(items)
            self.__items__ = list(items)

        def __repr__(self):
            return 'OrderedDict({0})'.format(str(self.__items__))

        def items(self):
            return self.__items__