from qiskit import QuantumCircuit, Aer, execute

# 量子状態の状態ベクトルを取得
def get_vector(circuit):
  simulator = Aer.get_backend('statevector_simulator')
  result = execute(circuit, simulator).result()
  statevector = result.get_statevector(circuit)
  return statevector
  

# 2x2以上の画像のエンコードに使うゲート
def mary2(circ, controls, angle, t, c0, c1):
  clist = []

  for i in controls:
    clist.append(int(i))

  if clist[0] == 0:
    circ.x(c0)
    
  if clist[1] == 0:
    circ.x(c1)
  
  circ.h(t)
  circ.rz(angle/4,t)
  circ.cx(c0, t)
  circ.rz(-angle/4,t)
  circ.cx(c1, t)
  circ.rz(angle/4,t)
  circ.cx(c0, t)
  circ.rz(-angle/4,t)
  circ.h(t)

  if clist[0] == 0:
    circ.x(c0)
    
  if clist[1] == 0:
    circ.x(c1)


# 4x4以上の画像のエンコードに使うゲート
def mary4(circ, angle, q_control_1, q_control_2, q_control_3, q_target):
  circ.h(q_target)
  circ.t(q_target)
  circ.cx(q_control_1, q_target)
  circ.tdg(q_target)
  circ.h(q_target)
  circ.cx(q_control_2, q_target)
  circ.rz(angle/4, q_target)
  circ.cx(q_control_3, q_target)
  circ.rz(-angle/4, q_target)
  circ.cx(q_control_2, q_target)
  circ.rz(angle/4, q_target)
  circ.cx(q_control_3, q_target)
  circ.rz(-angle/4, q_target)
  circ.h(q_target)
  circ.t(q_target)
  circ.cx(q_control_1, q_target)
  circ.tdg(q_target)
  circ.h(q_target)


# 4x4以上の画像のエンコードに使うゲート 
def rmcry(circ, angle, binary, q_controls, q_target, q_ancilla):

  assert len(binary) == len(q_controls), "error"
  assert len(binary) > 3, "ERROR"

  clist = [q_controls[-i-1] for i in range(len(binary)) if binary[i] == "0"]
  size = len(q_controls)

  circ.x(clist)

  circ.ccx(q_controls[0], q_controls[1], q_ancilla[0])
  circ.x(q_controls[0:2])
  for i in range(2, size-4+size%2, 2):
    circ.ccx(q_controls[i], q_controls[i+1], q_controls[i-1])
    circ.x(q_controls[i:i+2])

  if size == 4:
    circ.cx(q_controls[-1], q_controls[-3])
    circ.cx(q_controls[-2], q_controls[-4])

  elif size%2 == 0:
    circ.rccx(q_controls[-1], q_controls[-2], q_controls[-5])
  else:
    circ.cx(q_controls[-1], q_controls[-4])

  for i in range(6-size%2, size+1, 2):
    circ.rccx(q_controls[-i+3], q_controls[-i+2], q_controls[-i])

  mary4(circ, angle, q_ancilla[0], q_controls[0], q_controls[1], q_target)

  for i in reversed(range(6-size%2, size+1, 2)):
    circ.rccx(q_controls[-i+3], q_controls[-i+2], q_controls[-i])

  if size == 4:
    circ.cx(q_controls[-1], q_controls[-3])
    circ.cx(q_controls[-2], q_controls[-4])
  elif size%2 == 0:
    circ.rccx(q_controls[-1], q_controls[-2], q_controls[-5])
  else:
    circ.cx(q_controls[-1], q_controls[-4])

  for i in reversed(range(2, size-4+size%2, 2)):
    circ.x(q_controls[i:i+2])
    circ.rccx(q_controls[i], q_controls[i+1], q_controls[i-1])
  circ.x(q_controls[0:2])
  circ.ccx(q_controls[0], q_controls[1], q_ancilla[0])
  circ.x(clist)