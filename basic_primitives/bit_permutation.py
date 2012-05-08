"""
BitPermutation models the bits permutation operation
It permutes the bit-string according to the indices specified in indices list
"""
import signal_slot
from signal_slot import SignalSupporter, slot_supporter
from bit_string import BitString

class BitPermutation(object):

    @slot_supporter('bitstring')
    def __init__(self, permutation_list):
        if permutation_list is not None:
            self._permutation_list = permutation_list
        else:
            self._permutation_list = None

        self._input_bitstring = None
        self._output_bitstring = None


    def permute(self, permutation_list=None):
        """
        Permute according to permutation list
        """
        if permutation_list is not None:
            return self._bitstring.permute(permutation_list)
        else:
            if self._permutation_list is not None:
                return self._bitstring.permute(self._permutation_list)
        raise ValueError("Permutation list is not given nor initialized.")

    def bitstring_handler(self, **kwargs):
        self._input_bitstring = BitString(bitstring=kwargs['bitstring'])
        self.apply()

    def apply(self):
        self._output_bitstring = self._input_bitstring.permute(self._permutation_list)

if __name__ == '__main__':
    @SignalSupporter('bitstring')
    class Source(object):
        pass

    s = Source()
    bp = BitPermutation([3, 0, 2, 1])
    signal_slot.connect(s, 'bitstring', bp, 'bitstring')
    s.emit('bitstring', bitstring='1010')
    print bp._output_bitstring
