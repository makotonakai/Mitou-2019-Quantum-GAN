from qiskit import QuantumCircuit

def mary_4(self, angle, q_control_1, q_control_2, q_control_3, q_target):
        self.h(q_target)
        self.t(q_target)
        self.cx(q_control_1, q_target)
        self.tdg(q_target)
        self.h(q_target)
        self.cx(q_control_2, q_target)
        self.rz(angle/4, q_target)
        self.cx(q_control_3, q_target)
        self.rz(-angle/4, q_target)
        self.cx(q_control_2, q_target)
        self.rz(angle/4, q_target)
        self.cx(q_control_3, q_target)
        self.rz(-angle/4, q_target)
        self.h(q_target)
        self.t(q_target)
        self.cx(q_control_1, q_target)
        self.tdg(q_target)
        self.h(q_target)

def rmcry(self, angle, bin, q_controls, q_target, q_ancilla):

        assert len(bin) == len(q_controls), "error"
        assert len(bin) > 3, "ERROR"

        clist = [q_controls[-i-1] for i in range(len(bin)) if bin[i] == "0"]
        size = len(q_controls)

        self.x(clist)
        
        self.ccx(q_controls[0], q_controls[1], q_ancilla[0])
        self.x(q_controls[0:2])
        for i in range(2, size-4+size%2, 2):
                self.ccx(q_controls[i], q_controls[i+1], q_controls[i-1])
                self.x(q_controls[i:i+2])
        
        if size == 4:
                self.cx(q_controls[-1], q_controls[-3])
                self.cx(q_controls[-2], q_controls[-4])
        elif size%2 == 0:
                self.rccx(q_controls[-1], q_controls[-2], q_controls[-5])
        else:
                self.cx(q_controls[-1], q_controls[-4])
        
        for i in range(6-size%2, size+1, 2):
                self.rccx(q_controls[-i+3], q_controls[-i+2], q_controls[-i])

        self.mary_4(angle, q_ancilla[0], q_controls[0], q_controls[1], q_target)

        for i in reversed(range(6-size%2, size+1, 2)):
                self.rccx(q_controls[-i+3], q_controls[-i+2], q_controls[-i])
        
        if size == 4:
                self.cx(q_controls[-1], q_controls[-3])
                self.cx(q_controls[-2], q_controls[-4])
        elif size%2 == 0:
                self.rccx(q_controls[-1], q_controls[-2], q_controls[-5])
        else:
                self.cx(q_controls[-1], q_controls[-4])

        for i in reversed(range(2, size-4+size%2, 2)):
                self.x(q_controls[i:i+2])
                self.rccx(q_controls[i], q_controls[i+1], q_controls[i-1])
        self.x(q_controls[0:2])
        self.ccx(q_controls[0], q_controls[1], q_ancilla[0])

        self.x(clist)

QuantumCircuit.mary_4 = mary_4
QuantumCircuit.rmcry = rmcry