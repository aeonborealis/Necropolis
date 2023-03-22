import numpy as np

def f1(x):
    return x[0]**2 + 2*x[1]**2 + 3*x[2]**2 + x[0]*x[1] + x[1]*x[2] + 2*x[0]*x[2] + x[0] + x[1] + x[2]

def f2(x):
    return 2*x[0]**2 + 3*x[1]**2 + x[2]**2 + 2*x[0]*x[1] + 2*x[1]*x[2] + 3*x[0]*x[2] + 2*x[0] + x[1] + 2*x[2]

def f3(x):
    return 3*x[0]**2 + x[1]**2 + 4*x[2]**2 + x[0]*x[1] + 2*x[1]*x[2] + x[0]*x[2] + 3*x[0] + 2*x[1] + x[2]

def rainbow_encrypt(m, A, B):
    x = np.dot(A, m) # Affine transformation
    y = np.zeros_like(x)
    for i in range(x.shape[0]):
        y[i] = np.array([f1(x[i]), f2(x[i]), f3(x[i])])
    return np.dot(B, y) # Affine transformation

def rainbow_decrypt(c, A_inv, B_inv):
    y = np.dot(B_inv, c) # Affine transformation
    x = np.zeros((y.shape[0], 3))
    for i in range(y.shape[0]):
        x[i] = np.array([solve_eq(f1, y[i]), solve_eq(f2, y[i]), solve_eq(f3, y[i])])
    return np.dot(A_inv, x.T) # Affine transformation

def solve_eq(eq, res):
    # Solve equation eq(x) = res for x using numpy's root function
    coeffs = np.array([eq.__code__.co_consts[i] for i in range(1, eq.__code__.co_consts.index(None))])
    coeffs = coeffs[::-1] # Reverse order of coefficients
    coeffs = np.pad(coeffs, (0, coeffs.size), 'constant') # Add zeros for missing terms
    coeffs[1:-1] /= 2 # Divide quadratic terms by 2
    return np.roots(coeffs - res)[0].real
