import sys
import os

sys.path.append(os.getcwd())

from tools.qcircuit import *
from .gates import *
import itertools

def circ_encoder2(circ, img):
    img = np.array(list(itertools.chain.from_iterable(img)))
    img = img.astype('float64')
    img /= 255.0
    img = np.arcsin(img)
    
    circ.add_gate(Quantum_Gate("H", 1))
    circ.add_gate(Quantum_Gate("H", 2))

    for j in range(len(img)):
        if img[j] != 0:
            circ_mary2(circ, format(j, '02b'), 0, 1, 2)
            
    theta = np.random.random(len(circ.gates))
    for i in range(len(circ.gates)):
        circ.gates[i].angle = theta[i]

    return circ