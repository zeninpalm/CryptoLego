"""
BitPermutation models the bits permutation operation
It permutes the bit-string according to the indices specified in indices list
"""
from BitString import *

class BitPermutation:
    def __init__(self, permutation_list=None, **kwargs):
        if permutation_list is not None:
            self._permutation_list = permutation_list
        else:
            self._permutation_list = None

        self._bitstring = BitString(**kwargs)

    def permute(self, permutation_list=None):
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

if __name__ == '__main__':
    import doctest
    doctest.testfile('BitPermutationDocTest.txt')

