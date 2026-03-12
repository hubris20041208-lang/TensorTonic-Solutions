import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    v = np.asarray(v)
    norm = np.sqrt(np.sum(v**2, axis=-1))
    if v.ndim ==1:
        return float(norm)
    return norm
    pass