from qiskit import QuantumCircuit, execute
from .frqi_gates import *
import numpy as np
import itertools

# 2x2の画像のエンコード
def frqiEncoder2(circuit, img):
  img = np.array(list(itertools.chain.from_iterable(img)))
  img = img.astype('float64')
  img /= 255.0
  img = np.arcsin(img)
  circuit.h(1)
  circuit.h(2)
  for j in range(len(img)):
    if img[j] != 0:
      mary2(circuit, format(j, '02b'), 2.0 * img[j], 0, 1, 2)

  outputstate = get_vector(circuit)
  return outputstate
  
# 2x2の画像のエンコード
def get_real_state2(circuit, img):
    outputstate = frqiEncoder2(circuit, img)
    return np.matrix(outputstate)

# 2x2の画像のデコード  
def frqiDecoder2(vec):
    arr = np.array([])
    idx_list = [1,5,3,7]
    for idx in idx_list:
        arr = np.append(arr, int(abs(vec[idx])*255/0.5))
    color_matrix = arr.reshape(2,2)
    
    return color_matrix
  
# 4x4以上の画像のエンコード  
def frqiEncoder4(circ, img, q_controls, q_target, q_ancilla):
    '''
    qc.frqiEncoder(...)のように使う。
    img (array): 画像の配列
    q_target (Qubit): target qubit
    q_controls (list[Qubit]): control qubits
    q_ancilla (Qubit): Ancillary qubit
    '''
    img = np.array(img)
    assert len(q_controls) >= np.log2(img.size), "You need more control qubits."

    img = img.reshape(img.size)
    img = img.astype('float64')
    img /= 255.0
    img = np.arcsin(img)

    # apply hadamard gates
    circ.h(q_controls)

    # apply c10Ry gates (representing color data)
    for i in range(len(img)):
        if img[i] != 0:
            rmcry(circ, 2 * img[i], format(i, '0'+str(len(q_controls))+'b'), q_controls, q_target, q_ancilla)

# 4x4の画像のデコード 
def frqiDecoder4(circ, img, q_controls):
    '''
    generated_img = qc.frqiDecoder(...)のように使う。
    img (array): オリジナルの画像の配列
    backend: e.g. Aer.get_backend('qasm_simulator')
    shots: 測定の時のショットの数
    q_target (Qubit): target qubit
    q_controls (list[Qubit]): control qubits
    cbit: Classical bit
    '''
    img = np.array(img)
    vector = get_vector(circ)
    genimg = np.array([])

  #### decode
    for i in range(img.size):
        try:
            genimg = np.append(genimg, [abs(vector[int(format(i, '0'+str(len(q_controls))+'b')+'1',2)]*np.sqrt(2**len(q_controls)))])
        except:
            genimg = np.append(genimg,[0.0])

    genimg *= 255.0
    genimg = genimg.astype('int')
    genimg = genimg.reshape((len(img),int(img.size/len(img))))
    return genimg