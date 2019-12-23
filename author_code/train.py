#!/usr/bin/env python

"""
    training_pure_state.py: training process of qwgan for pure state

"""
import time
from datetime import datetime
from model.model_pure import Generator, Discriminator, compute_fidelity, compute_cost, get_zero_state
from tools.plot_hub import plt_fidelity_vs_iter
from tools.qcircuit import *
import config_pure as cf
from tools.utils import save_model, train_log

np.random.seed()
size = cf.system_size

def get_real_matrix():
    matrix = np.eye(2**size)
    matrix = np.matmul(H(size,1), matrix)
    matrix = np.matmul(H(size,2), matrix)
    matrix = np.matmul(H(size,0), matrix)
    matrix = np.matmul(X(size,1), matrix)
    matrix = np.matmul(X(size,2), matrix)
    matrix = np.matmul(RZ(size,0,np.pi/4,False), matrix)
    matrix = np.matmul(CNOT(size,1,0), matrix)
    matrix = np.matmul(RZ(size,0,-np.pi/4,False), matrix)
    matrix = np.matmul(CNOT(size,2,0), matrix)
    matrix = np.matmul(RZ(size,0,np.pi/4,False), matrix)
    matrix = np.matmul(CNOT(size,1,0), matrix)
    matrix = np.matmul(RZ(size,0,-np.pi/4,False), matrix)
    matrix = np.matmul(H(size,0), matrix)
    matrix = np.matmul(X(size,1), matrix)
    matrix = np.matmul(X(size,2), matrix)
    matrix = np.matmul(X(size,2), matrix)
    matrix = np.matmul(H(size,0), matrix)
    matrix = np.matmul(RZ(size,0,np.pi/4,False), matrix)
    matrix = np.matmul(CNOT(size,1,0), matrix)
    matrix = np.matmul(RZ(size,0,-np.pi/4,False), matrix)
    matrix = np.matmul(CNOT(size,2,0), matrix)
    matrix = np.matmul(RZ(size,0,np.pi/4,False), matrix)
    matrix = np.matmul(CNOT(size,1,0), matrix)
    matrix = np.matmul(X(size,2), matrix)
    matrix = np.matmul(CNOT(size,1,0), matrix)
    matrix = np.matmul(RZ(size,0,-np.pi/4,False), matrix)
    matrix = np.matmul(H(size,0), matrix)
    matrix = np.matmul(X(size,2), matrix)
    return matrix

def construct_qcircuit(qc,size):
    '''
        the function to construct quantum circuit of generator
    :param qc:
    :param size:
    :return:
    '''
    qc.add_gate(Quantum_Gate("H", 0))
    qc.add_gate(Quantum_Gate("H", 1))
    qc.add_gate(Quantum_Gate("H", 2))
    qc.add_gate(Quantum_Gate("X", 1))
    qc.add_gate(Quantum_Gate("X", 2))
    qc.add_gate(Quantum_Gate("RZ", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 1, 0))
    qc.add_gate(Quantum_Gate("RZ", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 2, 0))
    qc.add_gate(Quantum_Gate("RZ", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 1, 0))
    qc.add_gate(Quantum_Gate("H", 0))
    qc.add_gate(Quantum_Gate("X", 1))
    qc.add_gate(Quantum_Gate("X", 0))
    qc.add_gate(Quantum_Gate("X", 0))
    qc.add_gate(Quantum_Gate("H", 0))
    qc.add_gate(Quantum_Gate("RZ", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 1, 0))
    qc.add_gate(Quantum_Gate("RZ", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 2, 0))
    qc.add_gate(Quantum_Gate("RZ", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("CNOT", 1, 0))
    qc.add_gate(Quantum_Gate("X", 2))
    qc.add_gate(Quantum_Gate("CNOT", 1, 0))
    qc.add_gate(Quantum_Gate("RZ", 0, angle=0.5000 * np.pi))
    qc.add_gate(Quantum_Gate("H", 0))
    qc.add_gate(Quantum_Gate("X", 2))

    theta = np.random.random(len(qc.gates))
    for i in range(len(qc.gates)):
        qc.gates[i].angle = theta[i]

    return qc

def main():

    zero_state = get_zero_state(size)

    fidelities = list()
    losses = list()

    angle = np.random.randint(1, 10, size=[size, 3])
    matrix = get_real_matrix()
    real_state = np.matmul(matrix, zero_state)

    # define generator
    gen = Generator(size)
    gen.set_qcircuit(construct_qcircuit(gen.qc,size))

    # define discriminator
    herm = [I, Pauli_X, Pauli_Y, Pauli_Z]

    dis = Discriminator(herm, size)

    f = compute_fidelity(gen,zero_state,real_state)
    # optional term, this is for controlling the initial fidelity is small.
    # while(compute_fidelity(gen,zero_state,real_state)>0.5):
    #     gen.reset_angles()
    while(compute_fidelity(gen,zero_state,real_state)<0.001):
        gen.reset_angles()

    while(f < 0.99):
        starttime = datetime.now()
        for iter in range(cf.epochs):
            print("==================================================")
            print("Epoch {}, Step_size {}".format(iter + 1, cf.eta))

            if iter % cf.step_size == 0:
                # Generator gradient descent
                gen.update_gen(dis,real_state)
                print("Loss after generator step: {}".format(compute_cost(gen, dis,real_state)))

            # Discriminator gradient ascent
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
                train_log(param, './{}qubit_log_pure.txt'.format(cf.system_size))

            if (cf.decay):
                eta = (cf.initial_eta * (cf.epochs - iter - 1) +
                       (cf.initial_eta) * iter) / cf.epochs

        f = compute_fidelity(gen,zero_state,real_state)

    plt_fidelity_vs_iter(fidelities, losses, cf, indx=0)
    save_model(gen, cf.model_gen_path)
    save_model(dis, cf.model_dis_path)
    
    fidelities[:]=[]
    losses[:]=[]
    print("end")

if __name__ == '__main__':

    main()


