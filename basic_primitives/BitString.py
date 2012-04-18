'''
BitString allows direct bit-operations.
'''
from BitVector import *

class BitString(BitVector):
    def __init__(self, bit_string = None, bit_integer = None, bit_vector = None):
        '''
        Require:    (bit_string != None and bit_integer == None and bit_vector == None)
            or      (bit_string == None and bit_integer != None and bit_vector == None)
            or      (bit_string == None and bit_integer == None and bit_vector != None)
        Ensure: BitString is initialized to the same bit pattern as the parameter specifies
        '''
        if bit_string != None:
            self._init_from_bit_string(bit_string)
        elif bit_integer != None:
            self._init_from_bit_integer(bit_integer)
        elif bit_vector != None:
            self._init_from_bit_vector(bit_vector)

    def _init_from_bit_string(self, bit_string):
        '''
        Require:    bit_string != None
        Ensure:     self.as_bit_string == bit_string
        '''
        self._bit_vector = BitVector.BitVector(bit_string = bit_string)

    def _init_from_bit_integer(self, bit_integer):
        '''
        Require:    bit_integer != None
        Ensure:     self.as_bit_integer = bit_integer
        '''
        self._bit_vector = BitVector.BitVector(bit_integer)

    def _init_from_bit_vector(self, bit_vector):
        '''
        Require:    bit_vector != None
        Ensure:     self.as_bit_vector = bit_vector
        '''
        pass


if __name__ == '__main__':
    print "In BitString module\n"

