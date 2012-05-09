"""
BitMapping defines mapping operations.
Such as the S-Boxes in DES, substitution in SPN network.
"""
from bit_string import *
import signal_slot
from signal_slot import SignalSupporter, slot_supporter

@SignalSupporter('bitstring')
class BitMapping(dict):

    @slot_supporter('bitstring', 'intvalue')
    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __getitem__(self, item):
        if isinstance(item, type('')):
            return dict.__getitem__(self, item)
        elif isinstance(item, type(0)):
            item_bin = bin(item)
            return dict.__getitem__(self, item_bin[2:])
        else:
            raise ValueError('BitMapping only supports bitstring or integer index value')

    def __setitem__(self, key, val):
        if isinstance(val, type('')): #bitstring specified
            dict.__setitem__(self, key, BitString(bitstring=val))

        elif isinstance(val, type(0)): #intVal specified
            val_bin = bin(val)
            dict.__setitem__(self, key, BitString(intVal=val_bin[2:]))

        else:
            raise ValueError('''BitMapping only supports bitstring or integer index value''')

    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).iteritems():
            self[k] = v

    def bitstring_handler(self, **bitstring):
        self._input_bitstring = bitstring['bitstring']
        self.apply()
        self.emit('bitstring', bitstring=str(self._output_bitstring))

    def intvalue_handler(self, **intvalue):
        self._input_bitstring = intvalue['intvalue']
        self.apply()

    def apply(self):
        self._output_bitstring = self[self._input_bitstring]

@SignalSupporter('bitstring_list')
class BitMappingGroup(object):
    @slot_supporter('bitstring_list')
    def __init__(self, *bitmappings):
        self._bitmappings = bitmappings

    def bitstring_list_handler(self, **kwargs):
        bitstrings = kwargs['bitstring_list']
        for index in range(0, len(bitstrings)):
            signal_slot.connect(bitstrings[index], 'bitstring', self._bitmappings[index], 'bitstring')
            bitstrings[index].emit('bitstring', bitstring=str(bitstrings[index]))

if __name__ == '__main__':
    from bit_permutation import BitPermutation

    # Begin test of simple bitstring mapping
    print 'Testing BitMapping'
    @SignalSupporter('bitstring', 'intvalue')
    class Foo(object):
        pass

    bm = BitMapping({'1001':'1100', '0001':'1111', '1101':'1000', '0111':'1011'})
    bp = BitPermutation([3, 0, 1, 2])
    f = Foo()

    signal_slot.connect(f, 'bitstring', bm, 'bitstring')
    signal_slot.connect(bm, 'bitstring', bp, 'bitstring')

    f.emit('bitstring', bitstring='0111')
    print bm._output_bitstring
    print bp._output_bitstring

    f.emit('bitstring', bitstring='1001')
    print bm._output_bitstring
    print bp._output_bitstring
    print 'End of BitMapping testing'
    # End of testing

    # Testing of BitMappingGroup
    print 'Testing BitMappingGroup'
    bss = [BitString(bitstring='1001'), BitString(bitstring='1101'), BitString(bitstring='001')]
    bm1 = BitMapping({'1001':'0000'})
    bm2 = BitMapping({'1101':'0111'})
    bm3 = BitMapping({'001':'010'})
    bg = BitMappingGroup(bm1, bm2, bm3)
    bg.bitstring_list_handler(bitstring_list=bss)
    print bm1._output_bitstring
    print bm2._output_bitstring
    print bm3._output_bitstring
    print 'End of BitMappingGroup testing'
    # End of testing