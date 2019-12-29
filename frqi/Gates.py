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
        assert len(bin) > 4, "ERROR"

        clist = [controls[-i-1] for i in range(len(bin)) if bin[i] == "0"]
        size = len(controls)

        self.x(clist)
        
        for i in range(0, size-4+size%2, 2):
                if i == 0:
                        self.ccx(controls[i], controls[i+1], anc)
                else:
                        self.ccx(controls[i], controls[i+1], controls[i-1])

                self.x(controls[i:i+2])
        
        if size%2 == 0:
                self.rccx(controls[-1], controls[-2], controls[-5])
        else:
                self.cx(controls[-1], controls[-4])
        
        for i in range(6-size%2, size+1, 2):
                self.rccx(controls[-i+3], controls[-i+2], controls[-i])

        self.mary_4(angle, target, anc, controls[0], controls[1])

        for i in reversed(range(6-size%2, size+1, 2)):
                self.rccx(controls[-i+3], controls[-i+2], controls[-i])

        if size%2 == 0:
                self.rccx(controls[-1], controls[-2], controls[-5])
        else:
                self.cx(controls[-1], controls[-4])

        for i in reversed(range(0, size-4+size%2, 2)):
                
                self.x(controls[i:i+2])

                if i == 0:
                        self.rccx(controls[i], controls[i+1], anc)
                else:
                        self.rccx(controls[i], controls[i+1], controls[i-1])

        self.x(clist)

QuantumCircuit.mary_4 = mary_4
QuantumCircuit.rmcry = rmcry