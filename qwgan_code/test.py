from tools.utils import get_zero_state
from tools.qcircuit import *
import itertools
from tools.frqi_gates import *
from tools.frqi_circuit import *
# from model.model_pure import *
# from generator.gates import *
# from generator.circuit import *

testimg2 = [[0,0],[255,255]]
testimg4 = [[255, 0, 255, 255], [0,0,0,0],[255, 255, 255, 255], [0,0,0,0]]
real_state = encode2(testimg2)
genimg = decode2(real_state)
print(genimg)