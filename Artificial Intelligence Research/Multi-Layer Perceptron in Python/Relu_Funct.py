import numpy as np

def relu(x):
    return np.maximum(0, x)

# Example usage
x = np.array([-2, -1, 0, 1, 2])
y = relu(x)
print(y)
