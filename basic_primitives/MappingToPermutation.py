from basic_primitives.DataFlow import DataFlow

__author__ = 'ThinkPad'

class MappingToPermutation(DataFlow):
    def __init__(self, mapping, permutation):
        self._mapping = mapping
        self._permutation = permutation

    def run(self):
        bitstring = self._mapping.provide_data()
        self._permutation.permute(bitstring)