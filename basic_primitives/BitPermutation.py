"""
BitPermutation models the bits permutation operation
It permutes the bit-string according to the indices specified in indices list
"""
from BitString import *
from DataSource import DataSource
from DataTarget import DataTarget
from InputDataType import InputDataType
from OutputDataType import OutputDataType
from BitStringTarget import BitStringTarget
from BitStringSource import BitStringSource

class BitPermutation(DataSource, DataTarget, BitStringTarget, BitStringSource):

    def __init__(self, permutation_list=None, **kwargs):
        DataSource.__init__(self)
        DataTarget.__init__(self)
        BitStringTarget.__init__(self, None)
        BitStringSource.__init__(self, None)

        DataSource.register_handler(self, OutputDataType.bit_string, self._output_bit_string_handler)
        DataTarget.register_handler(self, InputDataType.bit_string, self._input_bit_string_handler)

        if permutation_list is not None:
            self._permutation_list = permutation_list
        else:
            self._permutation_list = None

        self._bitstring = BitString(**kwargs)


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

    def inplace_permute(self):
        if self._permutation_list is None:
            raise ValueError("Inner permutation list is not given.")
        else:
            self._bitstring = self._bitstring.permute(self._permutation_list)

    def provide_data(self):
        pass

    def set_input(self, data_source):
        self._bitstring = data_source

    def apply(self):
        return self._bitstring.permute(self._permutation_list)

if __name__ == '__main__':
    import doctest
    doctest.testfile('BitPermutationDocTest.txt')
