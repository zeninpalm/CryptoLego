"""
BitMapping defines mapping operations.
Such as the S-Boxes in DES, substitution in SPN network.
"""
from BitString import *
from InputDataType import InputDataType
from OutputDataType import OutputDataType
from BitStringTarget import BitStringTarget
from BitStringSource import BitStringSource

class BitMapping(dict, BitStringTarget, BitStringSource):

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

        BitStringSource.__init__(self, None)
        BitStringTarget.__init__(self, None)

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

    def output_bit_string_handler(self, other_info=None):
        return self._output_bitstring

    def apply(self):

        self._output_bitstring = self[self._input_bitstring]


if __name__ == '__main__':
    class Foo(DataSource):
        def provide_data(self, output_type):
            return str(BitString(bitstring='1001'))

    class Bar(DataSource):
        def provide_data(self, output_type):
            return str(BitString(bitstring='0000'))

    bm = BitMapping({'1001':'1100', '0000':'1111'})
    f = Foo()
    bm.set_input(f, InputDataType.bit_string)
    bm.apply()
    print bm.provide_data(OutputDataType.bit_string)

    b = Bar()
    bm.set_input(b, InputDataType.bit_string)
    bm.apply()
    print bm.provide_data(OutputDataType.bit_string)
