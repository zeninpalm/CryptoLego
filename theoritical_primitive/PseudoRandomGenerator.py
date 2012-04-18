'''
PseudoRandomGenerator, built on the assumption of one-way function
'''
import OneWayFunction

class PseudoRandomGenerator(OneWayFunction):
    def __init__(self, implementation):
        pass

    def generate_bit_string(self, seed):
        '''
        Require:    Seed_given_and_legal: (seed != None) and is_legal_seed(seed)
        Ensure:     Randomness_generated: len(Result) >= len(seed)
        '''

