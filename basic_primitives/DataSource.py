__author__ = 'ThinkPad'

from OutputDataType import OutputDataType

class DataSource(object):
    def __init__(self):
        self._output_handlers = {}

    def register_output_handler(self, output_type, handler):
        self._output_handlers[output_type] = handler

    # Section of data output handlers
    def provide_data(self, output_type=None):
        """
        bitstring is default output data type
        """
        if output_type is None:
            output_type = OutputDataType.bit_string
        return self._output_handlers[output_type]()

    def set_output(self, output_type, output_data):
        self._output_type = output_type
        self._output_data = output_data
