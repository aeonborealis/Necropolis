import random

# Define the multivariate quadratic equations
a = [[2, 1, 1], [1, 3, 1], [1, 1, 4]]
b = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

# Generate the public key and private key
def generate_keys():
    x = [random.randint(0, 10) for i in range(3)]
    y = [random.randint(0, 10) for i in range(3)]
    return (x, y)

public_key, private_key = generate_keys()

# Hash the input data using the public key
def hash_data(data):
    r = [random.randint(0, 10) for i in range(3)]
    h = [[sum([a[i][j] * r[j] for j in range(3)])] for i in range(3)]
    for d in data:
        h = [[sum([a[i][j] * h[j][k] for j in range(3)]) + b[i][k] * ord(d)] for i in range(3) for k in range(1)]
    return h

hash_value = hash_data("hello world")

# Generate a signature of the hash value using the private key
def generate_signature(hash_value, private_key):
    x, y = private_key
    s = [sum([x[j] * hash_value[j][k] for j in range(3)]) + y[k] for k in range(1)]
    return s

signature = generate_signature(hash_value, private_key)

# Verify the signature using the public key
def verify_signature(hash_value, signature, public_key):
    x, y = public_key
    s = [sum([x[j] * hash_value[j][k] for j in range(3)]) + y[k] for k in range(1)]
    return signature == s

is_valid = verify_signature(hash_value, signature, public_key)
