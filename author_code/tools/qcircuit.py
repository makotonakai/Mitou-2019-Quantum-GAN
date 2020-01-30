#!/usr/bin/env python

"""
    qcircuit.py: including base components and definition of quantum circuit simulation.

"""
import traceback

import numpy as np
import scipy.linalg as linalg
import os
import random

import sys
from scipy.sparse import dok_matrix

I = np.eye(2)

# Pauli matrices
Pauli_X = np.matrix([[0, 1], [1, 0]])  #: Pauli-X matrix
Pauli_Y = np.matrix([[0, -1j], [1j, 0]])  #: Pauli-Y matrix
Pauli_Z = np.matrix([[1, 0], [0, -1]])  #: Pauli-Z matrix
Hadamard = np.matrix([[1, 1], [1, -1]] / np.sqrt(2))  #: Hadamard gate
T_gate = np.matrix([[1,0],[0,np.exp(1J*np.pi/4)]])
Tdg_gate = np.matrix([[1,0],[0,np.exp(-1J*np.pi/4)]])

global param_table
param_table = dict()


def Identity(size):
    matrix = 1
    for i in range(1, size + 1):
        matrix = np.kron(matrix, I)
    return matrix
    
    
def X(size, qubit):
    matrix = 1
    for i in range(size):
        if i == qubit:
            matrix = np.kron(Pauli_X, matrix)
        else:
            matrix = np.kron(I, matrix)
    return matrix


def Y(size, qubit):
    matrix = 1
    for i in range(size):
        if i == qubit:
            matrix = np.kron(Pauli_Y, matrix)
        else:
            matrix = np.kron(I, matrix)
    return matrix
    
    
def Z(size, qubit):
    matrix = 1
    for i in range(size):
        if i == qubit:
            matrix = np.kron(Pauli_Z, matrix)
        else:
            matrix = np.kron(I, matrix)
    return matrix
    

def H(size, qubit):
    matrix = 1
    for i in range(size):
        if i == qubit:
            matrix = np.kron(Hadamard, matrix)
        else:
            matrix = np.kron(I, matrix)
    return matrix
    
    
def T(size, qubit):
    matrix = 1
    for i in range(size):
        if i == qubit:
            matrix = np.kron(T_gate, matrix)
        else:
            matrix = np.kron(I, matrix)
    return matrix
    
    
def Tdg(size, qubit):
    matrix = 1
    for i in range(size):
        if i == qubit:
            matrix = np.kron(Tdg_gate, matrix)
        else:
            matrix = np.kron(I, matrix)
    return matrix
    

def RX(size, qubit, param, is_grad):
    matrix = 1
    for i in range(size):
        if qubit == i:
            if is_grad == False:
                try:
                    matrix = np.kron(linalg.expm(-1J / 2 * param * Pauli_X), matrix)
                except Exception:
                    print('param:\n:', param)
            else:
                matrix = np.kron(-1J / 2 * Pauli_X * linalg.expm(-1J / 2 * param * Pauli_X), matrix)
        else:
            matrix = np.kron(matrix, I)

    return matrix
    

def RY(size, qubit, param, is_grad):
    matrix = 1
    for i in range(size):
        if qubit == i:
            if is_grad == False:
                try:
                    matrix = np.kron(linalg.expm(-1J / 2 * param * Pauli_Y), matrix)
                except Exception:
                    print('param:\n:', param)
            else:
                matrix = np.kron(-1J / 2 * Pauli_Y * linalg.expm(-1J / 2 * param * Pauli_Y), matrix)
        else:
            matrix = np.kron(matrix, I)

    return matrix


def RZ(size, qubit, param, is_grad):
    matrix = 1
    for i in range(size):
        if qubit == i:
            if is_grad == False:
                try:
                    matrix = np.kron(np.exp(1J/2*param)*linalg.expm(-1J / 2 * param * Pauli_Z), matrix)
                except Exception:
                    print('param:\n:', param)
            else:
                matrix = np.kron(np.exp(1J/2*param)*-1J / 2 * Pauli_Z * linalg.expm(-1J / 2 * param * Pauli_Z), matrix)
        else:
            matrix = np.kron(matrix, I)

    return matrix
    

def CNOT(size, qubit1, qubit2):
    """
    CNOTゲート
    
    Parameters
        size    [int]   回路全体の量子ビット数
        qubit1  [int]   control量子ビットのindex
        qubit2  [int]   target量子ビットのindex
        is_grad [bool]  微分されているかどうか
        
    Return
        mat [np.matrix] (2**nqubits)x(2**nqubits)の行列
    """
    if qubit1 > size or qubit2 > size or qubit1 == qubit2:
        print("You entered the wrong pair of qubits")

    # 2進数の長さ
    length = len(bin(size)[2:])
    
#     考えられるすべての状態
    states = [format(num,str(length).zfill(2)+'b').zfill(size)[::-1] for num in range(2**size)]
     
#     制御量子ビットが1のすべての状態(2進数方式)
    controlled_states = [state for state in states if state[qubit1]=='1']
    
#     上の文字列を数値にした時の状態(整数)
#     制御されるすべての状態
    target_states = []
    
    for state in controlled_states:
    
#     target qubitが0の時、1に反転させる
        if state[qubit2] == '0':
          state_list = list(state)
          state_list[qubit2] = '1'
          target_str = "".join(state_list)
          
#     target qubitが1の時、0に反転させる
        else:
          state_list = list(state)
          state_list[qubit2] = '0'
          target_str = "".join(state_list)      
        target_states.append(target_str)
        
#     
#     #(2**nqubits)^2の正方行列
    matrix = Identity(size)
    matrix = np.array(matrix)
#     
    for control, target in zip(controlled_states, target_states):
        cont_idx = states.index(control)
        tar_idx = states.index(target)
        matrix[cont_idx][cont_idx] = 0
        matrix[cont_idx][tar_idx] = 1
        matrix[tar_idx][cont_idx] = 1
        matrix[tar_idx][tar_idx] = 0

    return np.matrix(matrix)
    

class Quantum_Gate:
    def __init__(self, name, qubit1=None, qubit2=None, **kwarg):
        self.name = name
        self.qubit1 = qubit1
        self.qubit2 = qubit2
        self.r = self.get_r()
        self.s = self.get_s()

        if "angle" in kwarg:
            self.angle = kwarg["angle"]
        else:
            self.angle = None

    def get_r(self):
        if self.name == 'RX' or self.name == 'RY' or self.name == 'RZ':
            return 1/2
        else:
            return None

    def get_s(self):
        if self.r != None:
            return np.pi / (4 * self.r)
        else:
            return None

    def matrix_representation(self, size, is_grad):

        if self.angle != None:
            try:
                param = float(self.angle)
            except:
                param = param_table[self.angle]
                
        if (self.name == "RZ"):
            return RZ(size, self.qubit1, param, is_grad)

        elif (self.name == "RX"):
            return RX(size, self.qubit1, param, is_grad)

        elif (self.name == "RY"):
            return RY(size, self.qubit1, param, is_grad)

        elif (self.name == "Z"):
            return Z(size, self.qubit1)

        elif (self.name == "X"):
            return X(size, self.qubit1)

        elif (self.name == "Y"):
            return Y(size, self.qubit1)
            
        elif (self.name == "H"):
            return H(size, self.qubit1)

        elif (self.name == "CNOT"):
            return CNOT(size, self.qubit1, self.qubit2)

        else:
            raise ValueError("Gate is not defined")

    def matrix_representation_shift_phase(self, size, is_grad, signal):

        if self.angle != None:
            try:
                if self.name == 'G':
                    param = float(self.angle)
                else:
                    param = float(self.angle)
                    if is_grad == True:
                        if signal == '+':
                            param = param + self.s
                        else:
                            param = param - self.s
                        is_grad = False
            except:
                param = param_table[self.angle]

        if (self.name == "RZ"):
            return RZ(size, self.qubit1, param, is_grad)

        elif (self.name == "RX"):
            return RX(size, self.qubit1, param, is_grad)

        elif (self.name == "RY"):
            return RY(size, self.qubit1, param, is_grad)

        elif (self.name == "Z"):
            return Z(size, self.qubit1)

        elif (self.name == "X"):
            return X(size, self.qubit1)

        elif (self.name == "Y"):
            return Y(size, self.qubit1)
            
        elif (self.name == "H"):
            return H(size, self.qubit1)
            
        elif (self.name == "T"):
            return T(size, self.qubit1)
            
        elif (self.name == "Tdg"):
            return Tdg(size, self.qubit1)

        elif (self.name == "CNOT"):
            return CNOT(size, self.qubit1, self.qubit2)

        else:
            raise ValueError("Gate is not defined")


class Quantum_Circuit:

    def __init__(self, size, name):
        self.size = size
        self.depth = 0
        self.gates = []
        self.name = name

    def check_ciruit(self):
        for j,gate in zip(range(len(self.gates)),self.gates):
            if gate.qubit1!=None and gate.qubit2!=None:
                if gate.qubit1>self.size-1:
                    print('Error: #{} gate:{} 1qubit is out of range'.format(j, gate.name))
                    os._exit(0)
                elif gate.qubit2>self.size-1:
                    print('Error: #{} gate:{} 2qubit is out of range'.format(j, gate.name))
                    os._exit(0)

    def get_mat_rep(self):
        matrix = Identity(self.size)
        for gate in self.gates:
            g = gate.matrix_representation(self.size, False)
            matrix = np.matmul(g, matrix)
        return np.asmatrix(matrix)

    def get_grad_mat_rep(self, index, signal='none', type='matrix_multiplication'):
        '''
            matrix multipliction: explicit way to calculate the gradient using matrix multiplication
            shift_phase: generate two quantum circuit to calculate the gradient
            Evaluating analytic gradients on quantum hardware
            https://arxiv.org/pdf/1811.11184.pdf
        :param index:
        :param type: the type of calculate gradient
        :return:
        '''
        if type == 'shift_phase':
            matrix = Identity(self.size)
            for j, gate in zip(range(len(self.gates)), self.gates):
                if index == j:
                    g = gate.matrix_representation_shift_phase(self.size, True, signal)
                    matrix = np.matmul(g, matrix)
                else:
                    g = gate.matrix_representation_shift_phase(self.size, False, signal)
                    matrix = np.matmul(g, matrix)
            return np.asmatrix(matrix)

        elif type == 'matrix_multiplication':
            matrix = Identity(self.size)
            for j, gate in zip(range(len(self.gates)), self.gates):
                if index == j:
                    g = gate.matrix_representation(self.size, True)
                    matrix = np.matmul(g, matrix)
                else:
                    g = gate.matrix_representation(self.size, False)
                    matrix = np.matmul(g, matrix)
            return np.asmatrix(matrix)

    def get_grad_qc(self,indx,type='0'):
        qc_list = list()
        for j,gate in zip(range(len(self.gates)),self.gates):
            tmp = Quantum_Gate(' ',qubit1=None,qubit2=None,angle=None)
            tmp.name = gate.name
            tmp.qubit1 = gate.qubit1
            tmp.qubit2 = gate.qubit2
            tmp.angle = gate.angle
            if j == indx:
                try:
                    if self.gates[j].name != 'G' or self.gates[j].name !='CNOT':
                        if type == '+':
                            tmp.angle = gate.angle + gate.s
                        elif type == '-':
                            tmp.angle = gate.angle - gate.s
                except:
                    print('param value error')
                qc_list.append(tmp)
            else:
                qc_list.append(tmp)
        return qc_list

    def add_gate(self, quantum_gate):
        self.depth += 1
        self.gates.append(quantum_gate)
