from qiskit import QuantumCircuit

def mary_4(self, angle, t, c0, c1, c2):
        self.h(t)
        self.t(t)
        self.cx(c0,t)
        self.tdg(t)
        self.h(t)
        self.cx(c1,t)
        self.rz(angle/4,t)
        self.cx(c2,t)
        self.rz(-angle/4,t)
        self.cx(c1,t)
        self.rz(angle/4,t)
        self.cx(c2,t)
        self.rz(-angle/4,t)
        self.h(t)
        self.t(t)
        self.cx(c0,t)
        self.tdg(t)
        self.h(t)

def rmcry(self, angle, bin, target, controls, anc):

        assert len(bin) == len(controls), "error"
        assert len(bin) > 3, "ERROR"

        clist = [controls[-i-1] for i in range(len(bin)) if bin[i] == "0"]
        size = len(controls)

        self.x(clist)
        
        self.ccx(controls[0], controls[1], anc)
        self.x(controls[0:2])
        for i in range(2, size-4+size%2, 2):
                self.ccx(controls[i], controls[i+1], controls[i-1])
                self.x(controls[i:i+2])
        
        if size == 4:
                self.cx(controls[-1], controls[-3])
                self.cx(controls[-2], controls[-4])
        elif size%2 == 0:
                self.rccx(controls[-1], controls[-2], controls[-5])
        else:
                self.cx(controls[-1], controls[-4])
        
        for i in range(6-size%2, size+1, 2):
                self.rccx(controls[-i+3], controls[-i+2], controls[-i])

        self.mary_4(angle, target, anc, controls[0], controls[1])

        for i in reversed(range(6-size%2, size+1, 2)):
                self.rccx(controls[-i+3], controls[-i+2], controls[-i])
        
        if size == 4:
                self.cx(controls[-1], controls[-3])
                self.cx(controls[-2], controls[-4])
        elif size%2 == 0:
                self.rccx(controls[-1], controls[-2], controls[-5])
        else:
                self.cx(controls[-1], controls[-4])

        for i in reversed(range(2, size-4+size%2, 2)):
                self.x(controls[i:i+2])
                self.rccx(controls[i], controls[i+1], controls[i-1])
        self.x(controls[0:2])
        self.ccx(controls[0], controls[1], anc)

        self.x(clist)

QuantumCircuit.mary_4 = mary_4
QuantumCircuit.rmcry = rmcry