from qiskit import QuantumCircuit
import Gates

def frqiEncoder(self, img, q_target, q_controls, q_ancilla):
    '''
    qc.frqiEncoder(...)のように使う。

    img (array): 画像の配列
    q_target (Qubit): target qubit
    q_controls (list[Qubit]): control qubits
    q_ancilla (Qubit): Ancillary qubit
    '''

    import numpy as np

    img = np.array(img)
    assert len(q_controls) >= np.log2(img.size), "You need more control qubits."

    img = img.reshape(img.size)
    img = img.astype('float64')
    img /= 255.0
    img = np.arcsin(img)

     # apply hadamard gates
    self.h(q_controls)

    # apply c10Ry gates (representing color data)
    for i in range(len(img)):
            if img[i] != 0:
                    self.rmcry(2 * img[i], format(i, '0'+str(len(q_controls))+'b'), q_target, q_controls, q_ancilla)

QuantumCircuit.frqiEncoder = frqiEncoder

def frqiDecoder(self, img, backend, shots, q_target, q_controls, cbit):
    '''
    generated_img = qc.frqiDecoder(...)のように使う。

    img (array): オリジナルの画像の配列
    backend: e.g. Aer.get_backend('qasm_simulator')
    shots: 測定の時のショットの数
    q_target (Qubit): target qubit
    q_controls (list[Qubit]): control qubits
    cbit: Classical bit
    '''
    import numpy as np
    from qiskit import execute

    img = np.array(img)

    self.measure([q_target] + q_controls, cbit)

    result = execute(self, backend, shots=shots).result()

    genimg = np.array([])

    #### decode
    for i in range(img.size):
            try:
                    genimg = np.append(genimg,[np.sqrt(result.get_counts(self)[format(i, '0'+str(len(q_controls))+'b')+'1']*2**len(q_controls)/shots)])
            except KeyError:
                    genimg = np.append(genimg,[0.0])

    genimg *= 255.0
    genimg = genimg.astype('int')
    genimg = genimg.reshape((len(img),int(img.size/len(img))))

    return genimg

QuantumCircuit.frqiDecoder = frqiDecoder