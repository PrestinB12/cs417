def calculate(data):
    """
    Just a huge return statement LOL
    """
    return [
        (x_k, x_k1, (y_k1 - y_k) / (x_k1 - x_k), y_k1 - ((y_k1 - y_k) / (x_k1 - x_k)) * x_k)
        for i, ((x_k, y_k), (x_k1, y_k1)) in enumerate(zip(data[:-1], data[1:]))
        if x_k != x_k1  
    ]
