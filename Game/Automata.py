from automata.fa.dfa import DFA
# DFA which matches all binary strings ending in an odd number of '1's
dfa = DFA(
    states={'S1','S2','S3'},
    input_symbols={'1', '2','3'},
    transitions={
        'S1': {'1': 'S3', '2': 'S2','3':'S1'},
        'S2': {'1': 'S3', '2': 'S2','3':'S2'},
        'S3': {'1': 'S3', '2': 'S3','3':'S3'},

    },
    initial_state='S1',
    final_states={'S3','S1','S2'}
)
#print(dfa.read_input('322'))
