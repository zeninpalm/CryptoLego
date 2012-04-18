'''
BitMapping defines mapping operations.
Such as the S-Boxes in DES, substitution in SPN network.
'''
from BitVector import *

class BitMapping:
    def __init__(self):
        self._mapping_pairs = {}

    #Section of Access
    def fill_with_pairs(self, mapping_pairs):
        '''
        Require:    mapping_pairs != None
        Ensure:     foreach (from,to) in mapping_pair:
                        self.map(from) == to
        '''
        for (from_bits, to_bits) in mapping_pairs:
            self._mapping_pairs[from_bits] = BitVector(bitstring=to_bits)

    def extend_with_pair(self, mapping_pair):
        '''
        Require:    mapping_pair != None
                    len(mapping_pair[0] == len(mapping_pair[1])
        Ensure:     len(_mapping_pair) == len(old _mapping_pair)+1
        '''
        (from_bits, to_bits) = mapping_pair
        self._mapping_pairs[from_bits] = BitVector(bitstring=to_bits)


    def set_with_table(self, mapping_table):
        '''
        Require:    Table_not_none: mapping_table != None
                    No_none_row: [row != None for row in table]
        Ensure:
            foreach row in table:
                self.map(row.index) == row #The index of row is the source bit pattern
        '''
        pass

    def put(self, from_bitstring, to_bitstring):
        '''
        Require:    from_bitstring != None
                    to_bitstring != None
        Ensure:     self.map(from_bitstring) == to_bitstring
        '''
        self._mapping_pairs[from_bitstring] = BitVector(to_bitstring)

    def map(self, bit_pattern):
        '''
        Require:    Bit_pattern_valid: is_valid(bit_pattern)
        Ensure:     Correctly_mapped
        '''
        pass
    # End of Access category

    # Query
    def is_valid(self, bit_pattern):
        '''
        Require:    bit_pattern != None
        Ensure:     (Result == True) or (Result == False)
        '''
        pass

    def dump_mapping(self):
        '''
        Require:    True
        Ensure:     Return the internal mapping table as a hash-table data structure
        '''
        for (k, v) in self._mapping_pairs.iteritems():
            print "%s --> %s" % (k, v)

if __name__ == '__main__':
    import doctest
    doctest.testfile('BitMappingDocTest.txt')
