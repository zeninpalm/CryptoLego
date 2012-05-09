__author__ = 'ThinkPad'
from basic_primitives.bit_mapping import BitMapping, BitMappingGroup
from basic_primitives.bit_string import BitString, BitStringCombiner, BitStringDivider
from basic_primitives.bit_permutation import BitPermutation
from basic_primitives.signal_slot import SignalSupporter, slot_supporter
import basic_primitives.signal_slot as signal_slot

if __name__ == '__main__':

    input = BitString(bitstring='1011010011000100') # size = 16
    mapping1 = BitMapping({'1011':'0111'})
    mapping2 = BitMapping({'0100':'1100'})
    mapping3 = BitMapping({'1100':'0011'})
    mapping4 = BitMapping({'0100':'1101'})
    mapping_group = BitMappingGroup(mapping1, mapping2, mapping3, mapping4)
    divider = BitStringDivider([0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15])
    combiner = BitStringCombiner()

    signal_slot.connect(input, 'bitstring', divider, 'bitstring')
    signal_slot.connect(divider, 'bitstring_list', mapping_group, 'bitstring_list')
    signal_slot.connect(mapping_group, 'bitstring_list', combiner, 'bitstring_list')

    input.emit('bitstring', bitstring='1011010011000100')
    print combiner._output_bitstring
