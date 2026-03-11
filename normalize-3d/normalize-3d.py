import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v =np.asarray(v, dtype=float)
    norm = np.linalg.norm(v, axis=-1,keepdims=True)
    res = np.zeros_like(v)
    mask = norm > 1e-10
    res[mask.squeeze()] = v[mask.squeeze()] / norm[mask.squeeze()]
    return res
    pass