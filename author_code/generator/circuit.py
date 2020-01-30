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
    
    
def circ_frqiEncoder(circ, img, q_controls, q_target, q_ancilla):
    '''
    qc.frqiEncoder(...)のように使う。
    img (array): 画像の配列
    q_target (Qubit): target qubit
    q_controls (list[Qubit]): control qubits
    q_ancilla (Qubit): Ancillary qubit
    '''
    img = np.array(img)
    assert len(q_controls) >= np.log2(img.size), "You need more control qubits."

    img = img.reshape(img.size)
    img = img.astype('float64')
    img /= 255.0
    img = np.arcsin(img)

    # apply hadamard gates
    for c in q_controls:
        circ.add_gate(Quantum_Gate("H", c))
  # circ.h(q_controls)

  # apply c10Ry gates (representing color data)
    for i in range(len(img)):
        if img[i] != 0:
            circ_rmcry(circ, 2 * img[i], format(i, '0'+str(len(q_controls))+'b'), q_controls, q_target, q_ancilla)
#       rmcry(circ, 2 * img[i], format(i, '0'+str(len(q_controls))+'b'), q_controls, q_target, q_ancilla)

    return circ