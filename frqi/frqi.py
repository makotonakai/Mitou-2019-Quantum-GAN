from qiskit import QuantumCircuit
import Gates

def frqiEncoder(self, img, target, controls, anc):
    import numpy as np

    img = np.array(img)
    assert len(controls) >= np.log2(img.size), "You need more control qubits."

    img = img.reshape(img.size)
    img = img.astype('float64')
    img /= 255.0
    img = np.arcsin(img)

     # apply hadamard gates
    self.h(controls)

    # apply c10Ry gates (representing color data)
    for i in range(len(img)):
            if img[i] != 0:
                    self.rmcry(2 * img[i], format(i, '0'+str(len(controls))+'b'), target, controls, anc)

QuantumCircuit.frqiEncoder = frqiEncoder

def frqiDecoder(self, img, backend, shots, target, controls, cbit):
    import numpy as np
    from qiskit import execute

    img = np.array(img)

    self.measure([target]+controls,cbit)

    result = execute(self, backend, shots=shots).result()

    genimg = np.array([])

    #### decode
    for i in range(img.size):
            try:
                    genimg = np.append(genimg,[np.sqrt(result.get_counts(self)[format(i, '0'+str(len(controls))+'b')+'1']*2**len(controls)/shots)])
            except KeyError:
                    genimg = np.append(genimg,[0.0])

    genimg *= 255.0
    genimg = genimg.astype('int')
    genimg = genimg.reshape((len(img),int(img.size/len(img))))

    return genimg

QuantumCircuit.frqiDecoder = frqiDecoder