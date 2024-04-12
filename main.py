## Instalar a biblioteca automathon
## pip install automathon 

from automathon import DFA

## WP = 0, WRB = 1, NN = 2, NNP = 3, IN = 4, DT = 5, JJ = 6, RB = 7, VB = 8, VBP = 9

Q = {'start', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'final_state'}
sigma = {'0', '1', "2", "3", "4", "5", "6", "7", "8", "9"}
delta = {
    'start': {'0': 'q1', '1': 'q4'},
    'q1': {'2': 'q2'},
    'q2': {'3': 'final_state', '4': 'q3'},
    'q3': {'3': 'final_state'},
    'q4': {'2': 'q5', '3': 'q6'},
    'q5': {'3': 'final_state'},
    'q6': {'4': 'final_state'}
}
initial_state = 'start'
F = {'q2', 'q3', 'q5', 'final_state'}

automata = DFA(Q, sigma, delta, initial_state, F)
automata.is_valid()

## Função para verificar se uma sequência é aceita pelo autômato.
## automata.accept('')