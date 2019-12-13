"""
    utils.py: some public tool functions

"""

import collections
import numpy as np
from scipy.linalg import sqrtm
import pickle

def _flatten(x):
    """Iterate through an arbitrarily nested structure, flattening it in depth-first order.

    See also :func:`_unflatten`.

    Args:
        x (array, Iterable, other): each element of the Iterable may itself be an iterable object

    Yields:
        other: elements of x in depth-first order
    """
    it = x
    for x in it:
        if (isinstance(x, collections.Iterable) and
                not isinstance(x, str)):
            for y in _flatten(x):
                yield y
        else:
            yield x

def _unflatten(flat, prototype):
    """Restores an arbitrary nested structure to a flattened iterable.

    See also :func:`_flatten`.

    Args:
        flat (array): 1D array of items
        model (array, Iterable, Number): model nested structure

    Returns:
        (other, array): first elements of flat arranged into the nested
        structure of model, unused elements of flat
    """
    if isinstance(prototype, np.ndarray):
        idx = prototype.size
        res = np.array(flat)[:idx].reshape(prototype.shape)
        return res
    elif isinstance(prototype, collections.Iterable):
        res = []
        for x in prototype:
            val, flat = _unflatten(flat, x)
            res.append(val)
        return res, flat
    else:
        raise TypeError('Unsupported type in the model: {}'.format(type(prototype)))


def unflatten(flat, prototype):
    """Wrapper for :func:`_unflatten`.
    """
    # pylint:disable=len-as-condition
    result, tail = _unflatten(flat, prototype)
    if len(tail) != 0:
        raise ValueError('Flattened iterable has more elements than the model.')
    return result

def get_zero_state(size):
    '''
        get the zero quantum state |0,...0>
    :param size:
    :return:
    '''
    zero = np.array([1,0])
    state = 1
    for qubit in range(size):
      state = np.kron(state,zero)
    return state

def get_maximally_entangled_state(size):
    state = np.zeros(2 ** (2 * size), dtype=complex)
    for i in range(2 ** size):
        state_i = np.zeros(2 ** size)
        state_i[i] = 1
        state += np.kron(state_i, state_i)
    state = state / np.sqrt(2 ** size)
    state = np.asmatrix(state).T
    return state

def getreal_denmat(cf,prob_real,input_state):
    real_state_denmat = np.asmatrix(np.zeros((2 ** cf.system_size, 2 ** cf.system_size), dtype=complex))
    # linear combination of pure state
    for i in range(cf.num_to_mix):
        real_state_denmat += prob_real[i] * (np.matmul(input_state[i], input_state[i].getH()))
    return real_state_denmat


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

def plt_fidelity_vs_iter(fidelities,losses,config,indx=0):

    fig, (axs1, axs2) = plt.subplots(1, 2)
    axs1.plot(range(len(fidelities)), fidelities)
    axs1.set_xlabel('Epoch')
    axs1.set_ylabel('Fidelity between real and fake states')
    axs2.plot(range(len(losses)), losses)
    axs2.set_xlabel('Epoch')
    axs2.set_ylabel('Wasserstein Loss')
    plt.tight_layout()
    plt.savefig('{}/{}qubit_{}_{}.png'.format(config.figure_path,config.system_size, config.label, indx))
