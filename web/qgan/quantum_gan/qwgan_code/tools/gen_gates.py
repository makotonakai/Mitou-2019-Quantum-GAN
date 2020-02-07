from .qcircuit import *

def circ_C2RY_00(circ, control1, control2, target):
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("CCNOT", control1, control2, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCNOT", control1, control2, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control2))
    

def circ_C2RY_10(circ, control1, control2, target):
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("CCNOT", control1, control2, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCNOT", control1, control2, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control2))


def circ_C2RY_01(circ, control1, control2, target):
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("CCNOT", control1, control2, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCNOT", control1, control2, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control1))
    
    
def circ_C2RY_11(circ, control1, control2, target):
    circ.add_gate(Quantum_Gate("CCNOT", control1, control2, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCNOT", control1, control2, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    
    
    
def circ_C4RY_0000(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("X", control4))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("X", control4))

    
def circ_C4RY_1000(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("X", control4))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("X", control4))

  
def circ_C4RY_0100(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("X", control4))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("X", control4))
    
    
    
def circ_C4RY_0010(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control4))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control4))
    
    
def circ_C4RY_0001(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control3))

    
def circ_C4RY_1100(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("X", control4))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("X", control4))
    
    
def circ_C4RY_1010(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control4))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control4))
    
    
    
def circ_C4RY_1001(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("X", control3))
    
    
def circ_C4RY_0110(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control4))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control4))
    
    
def circ_C4RY_0101(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control3))
    
    
def circ_C4RY_0011(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("X", control2))
    
    
def circ_C4RY_1110(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control4))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control4))

    
def circ_C4RY_1101(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control3))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control3))
    
    
def circ_C4RY_1011(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control2))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control2))
    

def circ_C4RY_0111(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("X", control1))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("X", control1))
    
    
def circ_C4RY_1111(circ, control1, control2, control3, control4, target):
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
    circ.add_gate(Quantum_Gate("CCCCNOT", control1, control2, control3, control4, target))
    circ.add_gate(Quantum_Gate("RY", target, angle = 0))
     
  


