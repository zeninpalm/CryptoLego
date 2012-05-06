'''
BitString allows direct bit-operations.
'''
from DataSource import DataSource
from DataTarget import DataTarget
from BitVector import *

class BitString(BitVector, DataSource, DataTarget):
    def provide_data(self):
        return self

    def apply(self):
        pass


if __name__ == '__main__':
    print "In BitString module\n"

