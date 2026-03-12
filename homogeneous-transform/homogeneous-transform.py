import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    points = np.array(points)
    is_single_point = points.ndim == 1

    if is_single_point:
        points = points.reshape(1, 3)

    ones = np.ones((points.shape[0], 1))
    points_h = np.hstack([points, ones])

    transformed_points_h = T @ points_h.T

    transformed_points = transformed_points_h[:3, :].T

    if is_single_point:
        return transformed_points.flatten()
    return transformed_points
    pass