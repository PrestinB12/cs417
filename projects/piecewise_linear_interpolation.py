def calculate(data):
    """
    Calculate piecewise linear interpolation parameters.

    Args:
    - data: A list of tuples representing (x, y) data points.

    Returns:
    - list of tuples: List of tuples (x_k, x_k1, m, b) representing interpolated segments
    """
    return [
        (x_k, x_k1, (y_k1 - y_k) / (x_k1 - x_k), y_k1 - ((y_k1 - y_k) / (x_k1 - x_k)) * x_k)
        for i, ((x_k, y_k), (x_k1, y_k1)) in enumerate(zip(data[:-1], data[1:]))
        if x_k != x_k1  
    ]
