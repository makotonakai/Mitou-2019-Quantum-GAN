from tools.utils import get_zero_state
from tools.qcircuit import *
from frqi.frqi import *
from model.model_pure import *

from qiskit import * 


img_num = 0

testimg = [[0,0,0,0],[255,255,255,255],[0,0,0,0],[255,255,255,255]]
backends = Aer.backends()

qubit = 5
q = QuantumRegister(qubit, "q")
anc = QuantumRegister(1, "anc")
c = ClassicalRegister(qubit, "c")
qc = QuantumCircuit(q, anc, c)


# 2x2
# qc = QuantumCircuit(3)
# vector = frqiEncoder2(qc, testimg)
# genimg = frqiDecoder2(vector)
# print(genimg)

def circ_mary2(qc, controls, theta, t, c0, c1):
    clist = []

    for i in controls:
        clist.append(int(i))

    if clist[0] == 0:
        qc.add_gate(Quantum_Gate("X", c0))
    
    if clist[1] == 0:
        qc.add_gate(Quantum_Gate("X", c1))
    
    qc.add_gate(Quantum_Gate("H", t))

    qc.add_gate(Quantum_Gate("RZ", t, angle = theta/4))
    qc.add_gate(Quantum_Gate("CNOT", c0, t))
    qc.add_gate(Quantum_Gate("RZ", t, angle = -theta/4))
    qc.add_gate(Quantum_Gate("CNOT", c1, t))
    qc.add_gate(Quantum_Gate("RZ", t, angle = theta/4))
    qc.add_gate(Quantum_Gate("CNOT", c0, t))
    qc.add_gate(Quantum_Gate("RZ", t, angle = -theta/4))
    qc.add_gate(Quantum_Gate("H", t))

    if clist[0] == 0:
        qc.add_gate(Quantum_Gate("X", c0))
    
    if clist[1] == 0:
        qc.add_gate(Quantum_Gate("X", c1))

    return qc

    
def circ_frqiEncoder2(qc, img):
    img = np.array(list(itertools.chain.from_iterable(img)))
    img = img.astype('float64')
    img /= 255.0
    img = np.arcsin(img)
    qc.add_gate(Quantum_Gate("H", 1))
    qc.add_gate(Quantum_Gate("H", 2))
    for j in range(len(img)):
        if img[j] != 0:
            qc = circ_mary2(qc, format(j, '02b'), 2.0 * img[j], 0, 1, 2)
    return qc

size = 3
state = get_zero_state(size)
img = [[0,0], [0, 255]]

gen = Generator(size)
gen.set_qcircuit(circ_frqiEncoder2(gen.qc, img))
G = gen.getGen()

state = np.matmul(G, state)
print(state)

  
