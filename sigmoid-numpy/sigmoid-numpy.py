import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """

    res = 1 / (1 + np.exp(-np.asarray(x, dtype=float)))

    print(res)
    
    return res