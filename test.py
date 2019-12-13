# The whole quantum circuit
matrix = Identity(3)
matrix = np.matmul(H(3,1,np.pi,False), matrix)
matrix = np.matmul(H(3,2,np.pi,False), matrix)
matrix = np.matmul(X(3,1,np.pi,False), matrix)
matrix = np.matmul(H(3,0,np.pi,False), matrix)
matrix = np.matmul(RZ(3,0,np.pi/4,False), matrix)
matrix = np.matmul(CNOT(3,1,0,np.pi,False), matrix)
matrix = np.matmul(RZ(3,0,-np.pi/4,False), matrix)
matrix = np.matmul(CNOT(3,2,0,np.pi,False), matrix)
matrix = np.matmul(RZ(3,0,np.pi/4,False), matrix)
matrix = np.matmul(CNOT(3,1,0,np.pi,False), matrix)
matrix = np.matmul(RZ(3,0,-np.pi/4,False), matrix)
matrix = np.matmul(H(3,0,np.pi,False), matrix)
matrix = np.matmul(X(3,1,np.pi,False), matrix)

matrix = np.matmul(H(3,0,np.pi,False), matrix)
matrix = np.matmul(RZ(3,0,np.pi/4,False), matrix)
matrix = np.matmul(CNOT(3,1,0,np.pi,False), matrix)
matrix = np.matmul(RZ(3,0,-np.pi/4,False), matrix)
matrix = np.matmul(CNOT(3,2,0,np.pi,False), matrix)
matrix = np.matmul(RZ(3,0,np.pi/4,False), matrix)
matrix = np.matmul(CNOT(3,1,0,np.pi,False), matrix)
matrix = np.matmul(RZ(3,0,-np.pi/4,False), matrix)
matrix = np.matmul(H(3,0,np.pi,False), matrix)

state = get_zero_state(3).T
state = np.matmul(matrix,state)
print(state.T)

import matplotlib.pyplot as plt

def img_decoder(vec):
  vec = np.array(vec)
  probs = [abs(num)*255/0.5 for num in vec[4:8]]
  color_matrix = probs
  color_matrix = np.array(color_matrix).reshape(2,2)
  plt.imshow(color_matrix, cmap='gray')

img_decoder(state.T)