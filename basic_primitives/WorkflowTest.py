from basic_primitives.BitString import BitString
from basic_primitives.BitPermutation import BitPermutation
from basic_primitives.BitMapping import BitMapping
from basic_primitives.WorkFlow import WorkFlow
from basic_primitives.DataFlow import DataFlow

__author__ = 'ThinkPad'

bs = BitString(bitstring='1001')
bm = BitMapping({'1001':'1000'})
bp = BitPermutation([2, 0, 1, 3])

data_flow1 = DataFlow(bs, bm)
data_flow2 = DataFlow(bm, bp)

data_flow1.run()
data_flow2.run()

