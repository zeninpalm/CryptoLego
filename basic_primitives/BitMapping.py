"""
BitMapping defines mapping operations.
Such as the S-Boxes in DES, substitution in SPN network.
"""
from BitString import *
from DataSource import DataSource
from DataTarget import DataTarget
from InputDataType import InputDataType
from OutputDataType import OutputDataType

class BitMapping(dict, DataSource, DataTarget):

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

        self._data_source = None

        self._output_handlers = {OutputDataType.bit_string:self._output_bitstring_handler}
        self._output_bitstring = None

        self._input_handlers = {InputDataType.bit_string:self._input_bitstring_handler}
        self._input_bitstring = None


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

    # Section of data input handlers
    def set_input(self, data_source, input_type=None):
        """
        bitstring is default input data type
        """
        self._data_source = data_source
        if input_type is None:
            input_type = InputDataType.bit_string
        return self._input_handlers[input_type]()

    def _input_bitstring_handler(self):
        """
        This function takes bitstring format input
        """
        self._input_bitstring = self._data_source.provide_data(OutputDataType.bit_string)


    # Section of data output handlers
    def provide_data(self, output_type=None):
        """
        bitstring is default output data type
        """
        if output_type is None:
            output_type = OutputDataType.bit_string
        return self._output_handlers[output_type]()

    def _output_bitstring_handler(self):
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
