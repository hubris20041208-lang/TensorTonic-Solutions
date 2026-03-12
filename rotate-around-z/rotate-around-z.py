import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    points = np.array(points)
    is_single = points.ndim == 1
    if is_single:
        points = points.reshape(1, 3)

    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]
    
    c = np.cos(theta)
    s = np.sin(theta)

    new_x = x * c - y * s
    new_y = x * s + y * c
    new_z = z

    rotated_points = np.column_stack((new_x, new_y,new_z))
    return rotated_points.flatten() if is_single else rotated_points
    pass