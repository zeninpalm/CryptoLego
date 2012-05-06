__author__ = 'ThinkPad'

from InputDataType import InputDataType
from OutputDataType import OutputDataType
from DataTarget import DataTarget

class BitStringTarget(DataTarget):
    def __init__(self, bit_string=None):
        DataTarget.__init__(self)
        self._input_bitstring = bit_string
        self.register_input_handler(InputDataType.bit_string, self.input_bit_string_handler)

    def input_bit_string_handler(self, other_info=None):
        self._input_bitstring = self._data_source.provide_data(OutputDataType.bit_string)

