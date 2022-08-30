__version__ = '0.1.0'

from mymodule.submodule_1 import *

def reload():
    import importlib
    import sys
    importlib.reload(sys.modules['mymodule'])
    print('mymodule reloaded')


def foo():
    return 'bar'