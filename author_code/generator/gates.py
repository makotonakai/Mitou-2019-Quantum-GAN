import sys
sys.path.append('/Users/makotonakai/Mitou-2019-Quantum-GAN/author_code')


from tools.qcircuit import *

def circ_mary2(circ, controls,  t, c0, c1):
    clist = []
 
    for i in controls:
        clist.append(int(i))
 
    if clist[0] == 0:
        circ.add_gate(Quantum_Gate("X", c0))

    if clist[1] == 0:
       circ.add_gate(Quantum_Gate("X", c1))
  
    circ.add_gate(Quantum_Gate("H", t))
    circ.add_gate(Quantum_Gate("RZ", t, angle = 0))
    circ.add_gate(Quantum_Gate("CNOT", c0, t))
    circ.add_gate(Quantum_Gate("RZ", t, angle = 0))
    circ.add_gate(Quantum_Gate("CNOT", c1, t))
    circ.add_gate(Quantum_Gate("RZ", t, angle = 0))
    circ.add_gate(Quantum_Gate("CNOT", c0, t))
    circ.add_gate(Quantum_Gate("RZ", t, angle = 0))
    circ.add_gate(Quantum_Gate("H", t))

    if clist[0] == 0:
        circ.add_gate(Quantum_Gate("X", c0))

    if clist[1] == 0:
        circ.add_gate(Quantum_Gate("X", c1))
        
    return circ
        
    
def CCX(circ, q_control_1, q_control_2, q_target):

    circ.add_gate(Quantum_Gate("H", q_target))
    circ.add_gate(Quantum_Gate("CNOT", q_control_2, q_target))
    circ.add_gate(Quantum_Gate("Tdg", q_target))
    circ.add_gate(Quantum_Gate("CNOT", q_control_1, q_target))
    circ.add_gate(Quantum_Gate("T", q_target))
    circ.add_gate(Quantum_Gate("CNOT", q_control_2, q_target))
    circ.add_gate(Quantum_Gate("Tdg", q_target))
    circ.add_gate(Quantum_Gate("CNOT", q_control_1, q_target))
    circ.add_gate(Quantum_Gate("T", q_control_2))
    circ.add_gate(Quantum_Gate("T", q_target))
    circ.add_gate(Quantum_Gate("H", q_target))
    circ.add_gate(Quantum_Gate("CNOT", q_control_1, q_control_2))
    circ.add_gate(Quantum_Gate("T", q_control_1))
    circ.add_gate(Quantum_Gate("Tdg", q_control_2))
    circ.add_gate(Quantum_Gate("CNOT", q_control_1, q_control_2))
    
    
def RCCX(circ, q_control1, q_control2, q_target):

    circ.add_gate(Quantum_Gate("H", q_target))
    circ.add_gate(Quantum_Gate("T", q_target))
    circ.add_gate(Quantum_Gate("CNOT", q_control_2, q_target))
    circ.add_gate(Quantum_Gate("Tdg", q_target))
    circ.add_gate(Quantum_Gate("CNOT", q_control_1, q_target))
    circ.add_gate(Quantum_Gate("T", q_target))
    circ.add_gate(Quantum_Gate("CNOT", q_control_2, q_target))
    circ.add_gate(Quantum_Gate("Tdg", q_target))
    circ.add_gate(Quantum_Gate("H", q_target))
    
    
def circ_mary4(circ, theta, q_control_1, q_control_2, q_control_3, q_target):

    circ.add_gate(Quantum_Gate("H", q_target))
    circ.add_gate(Quantum_Gate("T", q_target))
    circ.add_gate(Quantum_Gate("CNOT", q_control_1, q_target))
    circ.add_gate(Quantum_Gate("Tdg", q_target))
    circ.add_gate(Quantum_Gate("H", q_target))
    circ.add_gate(Quantum_Gate("CNOT", q_control_2, q_target))
    circ.add_gate(Quantum_Gate("RZ", q_target, angle = theta/4))
    circ.add_gate(Quantum_Gate("CNOT", q_control_3, q_target))
    circ.add_gate(Quantum_Gate("RZ", q_target, angle = -theta/4))
    circ.add_gate(Quantum_Gate("CNOT", q_control_2, q_target))
    circ.add_gate(Quantum_Gate("RZ", q_target, angle = theta/4))
    circ.add_gate(Quantum_Gate("CNOT", q_control_3, q_target))
    circ.add_gate(Quantum_Gate("RZ", q_target, angle = -theta/4))
    circ.add_gate(Quantum_Gate("H", q_target))
    circ.add_gate(Quantum_Gate("T", q_target))
    circ.add_gate(Quantum_Gate("CNOT", q_control_1, q_target))
    circ.add_gate(Quantum_Gate("Tdg", q_target))
    circ.add_gate(Quantum_Gate("H", q_target))
    


def circ_rmcry(circ, theta, binary, q_controls, q_target, q_ancilla):

    assert len(binary) == len(q_controls), "error"
    assert len(binary) > 3, "ERROR"

    clist = [q_controls[-i-1] for i in range(len(binary)) if binary[i] == "0"]
    size = len(q_controls)
 
    for control in clist:
        circ.add_gate(Quantum_Gate("X", control))
#   circ.x(clist)
 
    CCX(circ, q_controls[0], q_controls[1], q_ancilla[0])
#   circ.ccx(q_controls[0], q_controls[1], q_ancilla[0])
    
    for i in range(0,2):
        circ.add_gate(Quantum_Gate("X", q_controls[i]))
#   circ.x(q_controls[0:2])

    for i in range(2, size-4+size%2, 2):
        CCX(circ, q_controls[i], q_controls[i+1], q_controls[i-1])
        for j in range(i,i+2):
            circ.add_gate(Quantum_Gate("X", q_controls[j]))
#     circ.ccx(q_controls[i], q_controls[i+1], q_controls[i-1])
#     circ.x(q_controls[i:i+2])
# 
    if size == 4:
        circ.add_gate(Quantum_Gate("CNOT", q_controls[-1],q_controls[-3]))
        circ.add_gate(Quantum_Gate("CNOT", q_controls[-2],q_controls[-4]))
#     circ.cx(q_controls[-1], q_controls[-3])
#     circ.cx(q_controls[-2], q_controls[-4])
# 
    elif size%2 == 0:
        RCCX(circ, q_controls[-1], q_controls[-2], q_controls[-5])
        # circ.rccx(q_controls[-1], q_controls[-2], q_controls[-5])
    else:
        circ.add_gate(Quantum_Gate("CNOT", q_controls[-1], q_controls[-4]))  
#     circ.cx(q_controls[-1], q_controls[-4])


    for i in range(6-size%2, size+1, 2):
        RCCX(circ, q_controls[-i+3], q_controls[-i+2], q_controls[-i])
#         circ.rccx(q_controls[-i+3], q_controls[-i+2], q_controls[-i])

    circ_mary4(circ, theta, q_ancilla[0], q_controls[0], q_controls[1], q_target)
#   mary_4(circ, angle, q_ancilla[0], q_controls[0], q_controls[1], q_target)
# 
    for i in reversed(range(6-size%2, size+1, 2)):
        RCCX(circ, q_controls[-i+3], q_controls[-i+2], q_controls[-i])
#     circ.rccx(q_controls[-i+3], q_controls[-i+2], q_controls[-i])
# 
    if size == 4:
        circ.add_gate(Quantum_Gate("CNOT", q_controls[-1], q_controls[-3]))
        circ.add_gate(Quantum_Gate("CNOT", q_controls[-2], q_controls[-4]))
#     circ.cx(q_controls[-1], q_controls[-3])
#     circ.cx(q_controls[-2], q_controls[-4])

    elif size%2 == 0:
        RCCX(circ, q_controls[-1], q_controls[-2], q_controls[-5])
#     circ.rccx(q_controls[-1], q_controls[-2], q_controls[-5])

    else:
        circ.add_gate(Quantum_Gate("CNOT", q_controls[-1], q_controls[-4]))
#     circ.cx(q_controls[-1], q_controls[-4])
# 
    for i in reversed(range(2, size-4+size%2, 2)):
        for j in range(i, i+2):
            circ.add_gate(Quantum_Gate("X", q_controls[j]))
        RCCX(circ, q_controls[i], q_controls[i+1], q_controls[i-1])
#     circ.x(q_controls[i:i+2])
#     circ.rccx(q_controls[i], q_controls[i+1], q_controls[i-1])
    for i in range(0, 2):
        circ.add_gate(Quantum_Gate("X", q_controls[i]))
        
    CCX(circ, q_controls[0], q_controls[1], q_ancilla[0])
    
    for c in clist:
        circ.add_gate(Quantum_Gate("X", c))
#   circ.x(q_controls[0:2])
#   circ.ccx(q_controls[0], q_controls[1], q_ancilla[0])
#   circ.x(clist)