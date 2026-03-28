import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """

    A = np.asarray(A, dtype=float)
    N, M = A.shape
    
    res = np.zeros((M, N), dtype=float)

    for i in range(N):
        for j in range(M):
            res[j, i] = A[i, j]
    
    return res
