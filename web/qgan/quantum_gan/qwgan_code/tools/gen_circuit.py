from .qcircuit import *
from .gen_gates import *
import itertools

def circ_encode2(circ):
    # img = np.array(list(itertools.chain.from_iterable(img)))
    # img = img.astype('float64')
    # img /= 255.0
    # img = np.arcsin(img)
    circ.add_gate(Quantum_Gate("H", 1))
    circ.add_gate(Quantum_Gate("H", 2))
    circ_C2RY_00(circ, 1, 2, 0)
    circ_C2RY_10(circ, 1, 2, 0)
    circ_C2RY_01(circ, 1, 2, 0)
    circ_C2RY_11(circ, 1, 2, 0)
    
    theta = np.random.random(len(circ.gates))
    for i in range(len(circ.gates)):
        circ.gates[i].angle = theta[i]

    return circ
    
# 4x4以上の画像のエンコード  
def circ_encode4(circ):
    '''
    qc.frqiEncoder(...)のように使う。
    img (array): 画像の配列
    q_target (Qubit): target qubit
    q_controls (list[Qubit]): control qubits
    q_ancilla (Qubit): Ancillary qubit
    '''    
    # img = np.array(list(itertools.chain.from_iterable(img)))
    # img = img.astype('float64')
    # img /= 255.0
    # img = np.arcsin(img)*2
    for i in range(1,5):
        circ.add_gate(Quantum_Gate("H", i))

    circ_C4RY_0000(circ, 1, 2, 3, 4, 0)
    circ_C4RY_1000(circ, 1, 2, 3, 4, 0)
    circ_C4RY_0100(circ, 1, 2, 3, 4, 0)
    circ_C4RY_0010(circ, 1, 2, 3, 4, 0)
    circ_C4RY_0001(circ, 1, 2, 3, 4, 0)
    circ_C4RY_1100(circ, 1, 2, 3, 4, 0)
    circ_C4RY_1010(circ, 1, 2, 3, 4, 0)
    circ_C4RY_1001(circ, 1, 2, 3, 4, 0)
    circ_C4RY_0110(circ, 1, 2, 3, 4, 0)
    circ_C4RY_0101(circ, 1, 2, 3, 4, 0)
    circ_C4RY_0011(circ, 1, 2, 3, 4, 0)
    circ_C4RY_1110(circ, 1, 2, 3, 4, 0)
    circ_C4RY_1101(circ, 1, 2, 3, 4, 0)
    circ_C4RY_1011(circ, 1, 2, 3, 4, 0)
    circ_C4RY_0111(circ, 1, 2, 3, 4, 0)
    circ_C4RY_1111(circ, 1, 2, 3, 4, 0)
    
    theta = np.random.random(len(circ.gates))
    for i in range(len(circ.gates)):
        circ.gates[i].angle = theta[i]
    
    return circ
    
    
