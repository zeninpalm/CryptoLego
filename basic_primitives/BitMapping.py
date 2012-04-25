"""
BitMapping defines mapping operations.
Such as the S-Boxes in DES, substitution in SPN network.
"""
from BitString import *

class BitMapping(dict):

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, key, val):
        if isinstance(val, type('')): #bitstring specified
            dict.__setitem__(self, key, BitString(bitstring=val))

        elif isinstance(val, type(0)): #intVal specified
            dict.__setitem__(self, key, BitString(intVal=val))

        else:
            raise ValueError('''BitMapping constructor can only be
                                called with bitstring or integer value''')

    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).iteritems():
            self[k] = v


if __name__ == '__main__':
    import doctest
    doctest.testfile('BitMappingDocTest.txt')
