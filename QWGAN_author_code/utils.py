"""
    utils.py: Quantum Wasserstein GANの実行に必要な関数

"""

import collections
import numpy as np
from scipy.linalg import sqrtm
import pickle


def get_zero_state(size):
    """
       初期状態|10...0>を取得する
    
    Parameter
        size [int] 回路全体の量子ビットの数
    
    Return
        state [np.matrix] 初期状態|10...0>
        
    """
    zero = np.array([1,0])
    state = 1
    for qubit in range(size):
      state = np.kron(state,zero)
    return state

