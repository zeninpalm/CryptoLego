__author__ = 'ThinkPad'

from InputDataType import InputDataType

class DataTarget(object):
    def __init__(self):
        self._input_handlers = {}
        self._data_source = None

    def apply(self):
        pass

    def register_input_handler(self, input_type, handler):
        self._input_handlers[input_type] = handler

    def set_input(self, data_source, input_type=None):
        """
        bitstring is default input data type
        """
        self._data_source = data_source
        if input_type is None:
            input_type = InputDataType.bit_string
        self._input_handlers[input_type]()
