#!/usr/bin/python

class CA():
    """One dimensional two-states-per-cell cellular automaton.

    Some fun rules to try:
    rule 30 is "00011110"
    rule 110 is "01101110"
    rule 45 is "00101101"
    rule 90 is "01011010"

    """

    def __init__(self, rule="00011110", generations=26, onbit="#", offbit=" ",
                 tape_length=80):
        pass
        self.onbit = onbit
        self.offbit = offbit
        self.rule = rule
        self.generations = generations
        self.tape_length = tape_length

    def run(self):
        '''Run cellular automaton.'''
        tape = ['0'] * self.tape_length
        tape[abs(self.tape_length/2)] = '1'
        othertape = list(tape)
        for gen in xrange(self.generations):
            for i, hole in enumerate(tape):
                if i > 0 and i < len(tape)-1:
                    binary = str(tape[i-1] + tape[i] + tape[i+1]) 
                    n = int(binary, 2)
                    othertape[i] = self.rule[7-n]
            print(''.join(tape).replace(' ', '')).replace('0', self.offbit).replace('1', self.onbit)
            tape = list(othertape)

if __name__ == '__main__':
    n = CA()
    n.run()
