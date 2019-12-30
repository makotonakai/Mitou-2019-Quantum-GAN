from qiskit import IBMQ, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, transpile
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, circuit_drawer
from qiskit import execute, Aer, BasicAer
from qiskit.aqua.circuits.gates.relative_phase_toffoli import rccx, rcccx
import numpy as np
import random
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.datasets import mnist
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, mutual_info_score, r2_score

import frqi

if __name__ == '__main__':
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        img_num = 0

        testimg = [[255,255,255,255], [0, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0]]
        #show original image
        #plt.imshow(x_train[img_num], cmap='gray')
        #plt.savefig('mnistimg'+str(img_num)+'.png')
        #plt.show()

        backends = Aer.backends()
        #print("Aer backends:",backends)

        qubit = 11
        q = QuantumRegister(qubit, "q")
        anc = QuantumRegister(1, "anc")
        c = ClassicalRegister(qubit, "c")
        qc = QuantumCircuit(q, anc, c)

        qc.frqiEncoder(x_train[img_num], q[1:qubit], q[0], anc)
        #qc.frqiEncoder(testimg, q[1:qubit], q[0], anc)

        backend_sim = Aer.get_backend('qasm_simulator')
        shots = 1024000

        genimg = qc.frqiDecoder(x_train[img_num], backend_sim, shots, q[1:11], q[0], c)
        #genimg = qc.frqiDecoder(testimg, backend_sim, shots, q[1:5], q[0], c)
        plt.imshow(genimg, cmap='gray', vmin=0, vmax=255)
        #plt.savefig('gen_'+str(img_num)+'.png')
        plt.show()