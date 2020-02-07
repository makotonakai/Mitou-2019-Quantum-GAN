#!/usr/bin/env python

"""
    utils.py: some public tool functions

"""

import collections
import numpy as np
from scipy.linalg import sqrtm
import pickle


def get_zero_state(size):
    '''
        get the zero quantum state |0,...0>
    :param size:
    :return:
    '''
    zero_state = np.zeros(2 ** size)
    zero_state[0] = 1
    zero_state = np.asmatrix(zero_state).T
    return zero_state


def train_log(param, file_path):
    with open(file_path, 'a') as file:
        file.write(param)
        

def load_model(file_path):
    with open(file_path, 'rb') as qc:
        model = pickle.load(qc)
    return model


def save_model(gen, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(gen, file)