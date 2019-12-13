"""
    train.py: training process of qwgan for pure state

"""
import time
from datetime import datetime
from model.model_pure import Generator, Discriminator, compute_fidelity, compute_cost, get_zero_state
from tools.plot_hub import plt_fidelity_vs_iter
from tools.qcircuit import *
import config_pure as cf
from tools.utils import save_model, train_log,get_zero_state
import matplotlib.pyplot as plt
import itertools

np.random.seed()

def real_state_matrix(size):

  matrix = Identity(size)

  matrix = np.matmul(H(size,1,np.pi,False), matrix)
  matrix = np.matmul(H(size,2,np.pi,False), matrix)

  matrix = np.matmul(X(size,1,np.pi,False), matrix)

  matrix = np.matmul(H(size,0,np.pi,False), matrix)
  matrix = np.matmul(RZ(size,0,np.pi/4,False), matrix)
  matrix = np.matmul(CNOT(size,1,0,np.pi,False), matrix)
  matrix = np.matmul(RZ(size,0,-np.pi/4,False), matrix)
  matrix = np.matmul(CNOT(size,2,0,np.pi,False), matrix)
  matrix = np.matmul(RZ(size,0,np.pi/4,False), matrix)
  matrix = np.matmul(CNOT(size,1,0,np.pi,False), matrix)
  matrix = np.matmul(RZ(size,0,-np.pi/4,False), matrix)
  matrix = np.matmul(H(size,0,np.pi,False), matrix)
  
  matrix = np.matmul(X(size,1,np.pi,False), matrix)

  matrix = np.matmul(H(size,0,np.pi,False), matrix)
  matrix = np.matmul(RZ(size,0,np.pi/4,False), matrix)
  matrix = np.matmul(CNOT(size,1,0,np.pi,False), matrix)
  matrix = np.matmul(RZ(size,0,-np.pi/4,False), matrix)
  matrix = np.matmul(CNOT(size,2,0,np.pi,False), matrix)
  matrix = np.matmul(RZ(size,0,np.pi/4,False), matrix)
  matrix = np.matmul(CNOT(size,1,0,np.pi,False), matrix)
  matrix = np.matmul(RZ(size,0,-np.pi/4,False), matrix)
  matrix = np.matmul(H(size,0,np.pi,False), matrix)

  return matrix


def construct_qcircuit(qc,size,layer):
    '''
        the function to construct quantum circuit of generator
    :param qc:
    :param size:
    :return:
    '''

    qc.add_gate(Quantum_Gate("Y", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Y", 1, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Y", 2, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Z", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("X", 1, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 1, 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Z", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 2, 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Z", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 1, 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Z", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("X", 1, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Y", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Y", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Z", 0, angle=0.2500 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 1, 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Z", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 2, 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Z", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 1, 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Z", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("Y", 0, angle=0.5000 * np.pi))

    theta = np.random.random(len(qc.gates))
    for i in range(len(qc.gates)):
      qc.gates[i].angle = theta[i]

    return qc

zero_state = get_zero_state(system_size)
img = [[255,0], [255,0]]
matrix = real_state_matrix(system_size)
real_state = np.matmul(matrix, zero_state)
real_state = np.matrix([[0.0], [0.5], [0.0], [0.5], \
                        [0.5], [0.0], [0.5],  [0.0]])
    
#define generator
gen = Generator(system_size)
gen.set_qcircuit(construct_qcircuit(gen.qc,system_size, 1))

#define discriminator
herm = [I, X, Y, Z]

dis = Discriminator(herm, system_size)

f = compute_fidelity(gen,zero_state,real_state)

optional term, this is for controlling the initial fidelity is small.
while(compute_fidelity(gen,zero_state,real_state)>0.5):
    gen.reset_angles()
while(compute_fidelity(gen,zero_state,real_state)<0.001):
  gen.reset_angles()

losses = []
fidelities = []


while(f < 0.9999):

  starttime = datetime.now()
  for iter in range(steps):
    print("==================================================")
    print("Epoch {}, Step_size {}".format(iter + 1, eta))

    if iter % step_size == 0:
      #Generator gradient descent
      gen.update_gen(dis,real_state)
      print("Loss after generator step: {}".format(compute_cost(gen, dis,real_state)))

    #Discriminator gradient ascent
    dis.update_dis(gen,real_state)
    print("Loss after discriminator step: {}".format(compute_cost(gen, dis,real_state)))

    cost = compute_cost(gen, dis, real_state)
    fidelity = compute_fidelity(gen, zero_state, real_state)

    losses.append(cost)
    fidelities.append(fidelity)

    print("Fidelity between real and fake state: {}".format(fidelity))
    print("==================================================")

    if iter % 10 == 0:
        endtime = datetime.now()
        training_duration = (endtime - starttime).seconds / np.float(3600)
        param = 'epoches:{:4d} | fidelity:{:8f} | time:{:10s} | duration:{:8f}\n'.format(iter,round(fidelity,6),time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),round(training_duration,2))
        train_log(param, './{}qubit_log_pure.txt'.format(system_size))

    if (decay):
        eta = (initial_eta * (epochs - iter - 1) +
                (initial_eta) * iter) / epochs

    f = compute_fidelity(gen,zero_state,real_state)

  epochs = [epoch for epoch in range(len(losses))]
  fig, (axL, axR) = plt.subplots(ncols=2, figsize=(10,4))
  axL.plot(epochs, fidelities, linewidth=2)
  axL.set_title('Fidelities')
  axL.set_xlabel('steps')
  axL.set_ylabel('Fidelity between the real state and fake state')
  axL.grid(True)
  axR.plot(epochs, losses, linewidth=2)
  axR.set_title('Cost Function')
  axR.set_xlabel('steps')
  axR.set_ylabel('Value of the Cost Function')
  axR.grid(True)