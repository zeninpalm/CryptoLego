'''
BitString allows direct bit-operations.
'''
import signal_slot
from signal_slot import SignalSupporter, slot_supporter
from BitVector import *

@SignalSupporter('bitstring', 'intvalue')
class BitString(BitVector):

    @slot_supporter('bitstring', 'intvalue')
    def __init__(self, *args, **kwargs):
        BitVector.__init__(self, *args, **kwargs)
        self._input_bitstring = None
        self._output_bitstring = None

    def bitstring_handler(self, **kwargs):
        self._input_bitstring = BitString(**kwargs)
        self._output_bitstring = BitString(**kwargs)
        self.emit('bitstring', bitstring=str(self._input_bitstring))

    def intvalue_handler(self, **kwargs):
        self._input_bitstring = BitString(**kwargs)
        self.emit('intvalue', intvalue=str(self._input_bitstring))

@SignalSupporter('bitstring_list')
class BitStringDivider(object):
    @slot_supporter('bitstring')
    def __init__(self, *divide_list):
        self._divide_list = divide_list

    def bitstring_handler(self, **kwargs):
        """
        Take the input bitstring and store it internally
        """
        self._input_bitstring = BitString(**kwargs)
        self.apply()
        self.emit('bitstring_list', bitstring=self._bitstrings)

    def apply(self):
        """
        Divide the input bitstring according to specified divide_list.
        BitStringDivider generates an array of bitstring, and each bitstring contains required bits
        """
        self._bitstrings = []
        for indexes in self._divide_list:
            length = len(indexes)
            pos = 0

            a_bitstring = BitString(size=length)
            for index in indexes:
                a_bitstring[pos] = self._input_bitstring[index]
                pos = pos + 1
            self._bitstrings.append(a_bitstring)

@SignalSupporter('bitstring')
class BitStringCombiner(object):
    @slot_supporter('bitstring_list')
    def __init__(self, *combine_list):
        self._combine_list = combine_list
        self._input_bitstring_list = None
        self._output_bitstring = None

    def bitstring_list_handler(self, **kwargs):
        """

        """
        self._input_bitstring_list = kwargs['bitstring_list']

    def apply(self):
        if len(self._combine_list) == 0:
            self._combine_list = range(0, len(self._input_bitstring_list))

        length = 0
        for index in self._combine_list:
            length = length + len(self._input_bitstring_list[index])
        self._output_bitstring = BitString(size=length)

        pos = 0
        for index in self._combine_list:
            a_bitstring = self._input_bitstring_list[index]
            length = len(a_bitstring)
            for internal_pos in range(0, length):
                self._output_bitstring[pos] = a_bitstring[internal_pos]
                pos = pos + 1

if __name__ == '__main__':
    @SignalSupporter('bitstring')
    class Source(object):
        pass

    s = Source()
    bs = BitString(bitstring='1001')

    signal_slot.connect(s, 'bitstring', bs, 'bitstring')
    s.emit('bitstring', bitstring='10011')
    print bs._output_bitstring

    bd = BitStringDivider([3,4], [0, 2, 1], [7, 5, 6])
    bd.bitstring_handler(bitstring='10110010')
    bd.apply()
    for b in bd._bitstrings:
        print b

    bl = [BitString(bitstring='101'), BitString(bitstring='00110'), BitString(bitstring='1100'), BitString(bitstring='1111')]
    bc = BitStringCombiner(1, 2, 0)
    bc.bitstring_list_handler(bitstring_list=bl)
    bc.apply()
    print bc._output_bitstring