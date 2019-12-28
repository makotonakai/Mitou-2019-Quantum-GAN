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
        assert len(bin) > 5, "ERROR"

        clist = []

        for i in bin:
                clist.append(int(i))

        for i in range(len(clist)):
                if clist[i] == 0:
                        self.x(controls[-i-1])
        
        for i in range(0, len(clist)-4+len(clist)%2, 2):
                if i == 0:
                        self.ccx(controls[i], controls[i+1], anc)
                else:
                        self.ccx(controls[i], controls[i+1], controls[i-1])

                self.x(controls[i])
                self.x(controls[i+1])
        
        if (len(clist)%2) == 0:
                self.rccx(controls[-1], controls[-2], controls[-5])
        else:
                self.cx(controls[-1], controls[-4])
        
        for i in range(6-len(clist)%2, len(clist)+1, 2):
                self.rccx(controls[-i+3], controls[-i+2], controls[-i])

        self.mary_4(angle, target, anc, controls[0], controls[1])

        for i in reversed(range(6-len(clist)%2, len(clist)+1, 2)):
                self.rccx(controls[-i+3], controls[-i+2], controls[-i])

        if (len(clist)%2) == 0:
                self.rccx(controls[-1], controls[-2], controls[-5])
        else:
                self.cx(controls[-1], controls[-4])

        for i in reversed(range(0, len(clist)-4+len(clist)%2, 2)):
                
                self.x(controls[i])
                self.x(controls[i+1])

                if i == 0:
                        self.rccx(controls[i], controls[i+1], anc)
                else:
                        self.rccx(controls[i], controls[i+1], controls[i-1])

        for i in range(len(clist)):
                if clist[i] == 0:
                        self.x(controls[-i-1])

QuantumCircuit.mary_4 = mary_4
QuantumCircuit.rmcry = rmcry