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

def frqiDecoder(self, result, origin_img):
    import numpy as np