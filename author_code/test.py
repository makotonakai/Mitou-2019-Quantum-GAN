from tools.utils import get_zero_state
from tools.qcircuit import *
from frqi.frqi import *
from model.model_pure import *
from generator.gates import *

from qiskit import * 


size = 5

testimg = [[255,255,255,255], [0, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0]]

#show original image
#plt.imshow(x_train[img_num], cmap='gray')
#plt.savefig('mnistimg'+str(img_num)+'.png')
#plt.show()


qubit = 6
control = [num for num in range(1,5)]
target = 0
anc = qubit-1

gen = Generator(size)
qc_fake = gen.qc
qc_fake = circ_frqiEncoder(qc_fake, testimg, control, target, anc)
fake_state = gen.getState()
print(fake_state)








  
