__author__ = 'ThinkPad'

from OutputDataType import OutputDataType
from DataSource import DataSource

class BitStringSource(DataSource):
    def __init__(self, bit_string=None):
        DataSource.__init__(self)
        self._output_bit_string = bit_string
        self.register_output_handler(OutputDataType.bit_string, self.output_bit_string_handler)

    def output_bit_string_handler(self, other_info=None):
        return self._output_bit_string

    def get_output_bit_string(self):
        return self._output_bit_string
