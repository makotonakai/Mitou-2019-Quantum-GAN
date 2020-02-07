from .qcircuit import *
from .frqi_gates import *
from .utils import get_zero_state

import numpy as np
import itertools

def encode2(img):
    img = np.array(list(itertools.chain.from_iterable(img)))
    img = img.astype('float64')
    img /= 255.0
    img = np.arcsin(img)*2
    size = 3
    state = get_zero_state(size)
    for i in range(1,3):
        state = np.matmul(H(size, i), state)
    state = np.matmul(C2RY_00(size, 1, 2, 0, img[0]), state)
    state = np.matmul(C2RY_10(size, 1, 2, 0, img[1]), state)
    state = np.matmul(C2RY_01(size, 1, 2, 0, img[2]), state)
    state = np.matmul(C2RY_11(size, 1, 2, 0, img[3]), state)
    return state
    
    
def decode2(state):
    state = np.array(state)
    vec = np.array([])
    for i in range(4):
        vec = np.append(vec, state[i*2])
    cos_list = [num.real*2 for num in vec]
    angle_list = [np.arccos(cos) for cos in cos_list]
    color_list = [angle*255*2/np.pi for angle in angle_list]
    color_mat = np.array([int(color) for color in color_list]).reshape(2,2)
    return color_mat

# 4x4以上の画像のエンコード  
def encode4(img):
    size = 5
    img = np.array(list(itertools.chain.from_iterable(img)))
    img = img.astype('float64')
    img /= 255.0
    img = np.arcsin(img)*2

    state = get_zero_state(size)
    for i in range(1,size):
        state = np.matmul(H(size, i), state)
    state = np.matmul(C4RY_0000(size, 1, 2, 3, 4, 0, img[0]), state)
    state = np.matmul(C4RY_1000(size, 1, 2, 3, 4, 0, img[1]), state)
    state = np.matmul(C4RY_0100(size, 1, 2, 3, 4, 0, img[2]), state)
    state = np.matmul(C4RY_0010(size, 1, 2, 3, 4, 0, img[3]), state)

    state = np.matmul(C4RY_0001(size, 1, 2, 3, 4, 0, img[4]), state)
    state = np.matmul(C4RY_1100(size, 1, 2, 3, 4, 0, img[5]), state)
    state = np.matmul(C4RY_1010(size, 1, 2, 3, 4, 0, img[6]), state)
    state = np.matmul(C4RY_1001(size, 1, 2, 3, 4, 0, img[7]), state)

    state = np.matmul(C4RY_0110(size, 1, 2, 3, 4, 0, img[8]), state)
    state = np.matmul(C4RY_0101(size, 1, 2, 3, 4, 0, img[9]), state)
    state = np.matmul(C4RY_0011(size, 1, 2, 3, 4, 0, img[10]), state)
    state = np.matmul(C4RY_1110(size, 1, 2, 3, 4, 0, img[11]), state)

    state = np.matmul(C4RY_1101(size, 1, 2, 3, 4, 0, img[12]), state)
    state = np.matmul(C4RY_1011(size, 1, 2, 3, 4, 0, img[13]), state)
    state = np.matmul(C4RY_0111(size, 1, 2, 3, 4, 0, img[14]), state)
    state = np.matmul(C4RY_1111(size, 1, 2, 3, 4, 0, img[15]), state)
    return state
    

# 4x4の画像のデコード 
def decode4(state):
    state = np.array(state)
    idx_list =  [0,2,4,8,16,6,10,18,12,20,24,14,22,26,28,30]
    vec = np.array([])
    for idx in idx_list:
        vec = np.append(vec, state[idx])
    cos_list = [num.real*4 for num in vec]
    angle_list = [np.arccos(cos) for cos in cos_list]
    color_list = [angle*255*2/np.pi for angle in angle_list]
    color_mat = np.array([int(color) for color in color_list]).reshape(4,4)
    return color_mat

    