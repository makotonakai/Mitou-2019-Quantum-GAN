"""
    train.py: Quantum Wasserstein GANの学習
"""
import time
from datetime import datetime
from model import Generator, Discriminator, compute_fidelity, compute_cost, get_zero_state
from qcircuit import *
import config as cf
from utils import get_zero_state
import matplotlib.pyplot as plt
import itertools
np.random.seed()
def real_state_matrix(size):
    """
    学習データの量子状態の行列を返す関数
    Parameters
        size [int] 量子回路全体の量子ビット数
    Return
        matrix [np.matrix] 学習データの量子状態を生成するために、量子回路に掛ける行列
    """
    matrix = np.eye(2**size)
    matrix = np.matmul(Hadamard(size,1, np.pi, False), matrix)
    matrix = np.matmul(Hadamard(size,2, np.pi, False), matrix)
    matrix = np.matmul(Hadamard(size,0, np.pi, False), matrix)
    matrix = np.matmul(X(size,1,np.pi,False), matrix)
    matrix = np.matmul(X(size,2,np.pi,False), matrix)
    matrix = np.matmul(Z_Rotation(size,0,np.pi/4,False), matrix)
    matrix = np.matmul(CNOT_Rotation(size,1,0,np.pi,False), matrix)
    matrix = np.matmul(Z_Rotation(size,0,-np.pi/4,False), matrix)
    matrix = np.matmul(CNOT_Rotation(size,2,0,np.pi,False), matrix)
    matrix = np.matmul(Z_Rotation(size,0,np.pi/4,False), matrix)
    matrix = np.matmul(CNOT_Rotation(size,1,0,np.pi,False), matrix)
    matrix = np.matmul(Z_Rotation(size,0,-np.pi/4,False), matrix)
    matrix = np.matmul(Hadamard(size,0, np.pi, False), matrix)
    matrix = np.matmul(X(size,1,np.pi,False), matrix)
    matrix = np.matmul(X(size,2,np.pi,False), matrix)
    matrix = np.matmul(X(size,2,np.pi,False), matrix)
    matrix = np.matmul(Hadamard(size,0, np.pi, False), matrix)
    matrix = np.matmul(Z_Rotation(size,0,np.pi/4,False), matrix)
    matrix = np.matmul(CNOT_Rotation(size,1,0,np.pi,False), matrix)
    matrix = np.matmul(Z_Rotation(size,0,-np.pi/4,False), matrix)
    matrix = np.matmul(CNOT_Rotation(size,2,0,np.pi,False), matrix)
    matrix = np.matmul(Z_Rotation(size,0,np.pi/4,False), matrix)
    matrix = np.matmul(CNOT_Rotation(size,1,0,np.pi,False), matrix)
    matrix = np.matmul(X(size,2,np.pi,False), matrix)
    matrix = np.matmul(CNOT_Rotation(size,1,0,np.pi,False), matrix)
    matrix = np.matmul(Z_Rotation(size,0,-np.pi/4,False), matrix)
    matrix = np.matmul(Hadamard(size,0, np.pi, False), matrix)
    matrix = np.matmul(X(size,2,np.pi,False), matrix)
    return matrix
def construct_qcircuit(qc,size,layer):
    """
    Generatorの量子回路、量子ゲートを掛けていく
    Parameters
        qc [QuantumCircuit] 量子回路
        size [int] 量子回路全体の量子ビット数
    Return 
        qc [QuantumCircuit] 必要な量子ゲートが追加された量子回路
    """
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
# 初期状態
zero_state = get_zero_state(system_size)
# 生成する画像の行列表現
img = [[255,0], [255,0]]
# 学習データをエンコードするための行列
matrix = real_state_matrix(system_size)
# 学習データの状態ベクトル
real_state = np.matmul(matrix, zero_state)
# Generator
gen = Generator(system_size)
# Generatorの量子回路に量子ゲートを掛ける
gen.set_qcircuit(construct_qcircuit(gen.qc,system_size, 1))
# Psi, Phiの計算に使うエルミート行列
herm = [I, X, Y, Z]
# Discriminator
dis = Discriminator(herm, system_size)
# 学習データと生成データ間のFidelityを計算する
f = compute_fidelity(gen,zero_state,real_state)
# optional term, this is for controlling the initial fidelity is small.
# while(compute_fidelity(gen,zero_state,real_state)>0.5):
#     gen.reset_angles()
while(compute_fidelity(gen,zero_state,real_state)<0.001):
  gen.reset_angles()
#各ステップのLoss関数のリスト
losses = []
#各ステップのFidelityのリスト
fidelities = []
# Fidelityが0.9999になるまで実行する
while(f < 0.9999):
    # 各ステップの始まる時間を調べる
    starttime = datetime.now()
    for iter in range(steps):
        # 各ステップでエポック数(学習回数)と学習率を表示する
        print("==================================================")
        print("Epoch {}, Step_size {}".format(iter + 1, eta))
    if iter % step_size == 0:
      # Generatorのパラメータ(theta)を更新する
      gen.update_gen(dis,real_state)
      # コスト関数の値を表示する
      print("Loss after generator step: {}".format(compute_cost(gen, dis,real_state)))
    # Discriminatorのパラメータ(alpha, beta)を更新する
    dis.update_dis(gen,real_state)
    # コスト関数の値を表示する
    print("Loss after discriminator step: {}".format(compute_cost(gen, dis,real_state)))
    # コスト関数と学習データの量子状態と生成された量子状態のFidelityを計算する
    cost = compute_cost(gen, dis, real_state)
    fidelity = compute_fidelity(gen, zero_state, real_state)
    # コスト関数とFidelityをリストに追加する
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
    #エポック数のリストを作る
    epochs = [epoch for epoch in range(len(losses))]
    fig, (axL, axR) = plt.subplots(ncols=2, figsize=(10,4))
    # エポック数とFidelityのグラフを表示する
    axL.plot(epochs, fidelities, linewidth=2)
    axL.set_title('Fidelities')
    axL.set_xlabel('steps')
    axL.set_ylabel('Fidelity between the real state and fake state')
    axL.grid(True)
    # エポック数とコスト関数のグラフを表示する
    axR.plot(epochs, losses, linewidth=2)
    axR.set_title('Cost Function')
    axR.set_xlabel('steps')
    axR.set_ylabel('Value of the Cost Function')
    axR.grid(True)