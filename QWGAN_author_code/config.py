"""
    config.py: 数値実験のパラメータ

"""

import numpy as np

label = 'pure_state'

# 量子ビット数
system_size = 3

#定数
lamb = np.float(2)

s = np.exp(-1 / (2 * lamb)) - 1
cst1 = (s / 2 + 1) ** 2
cst2 = (s / 2) * (s / 2 + 1)
cst3 = (s / 2) ** 2

# 学習のパラメータ
"""
initial_eta: 学習率
steps: 学習のステップ数
eta: 学習率(initial_etaと同じ)
step_size: ステップ数1回で計算する回数
replication: 
"""
initial_eta = 1e-1
steps = 300
decay = False
eta = initial_eta
step_size = 1
replications = 1

