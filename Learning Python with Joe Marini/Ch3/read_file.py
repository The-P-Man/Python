import numpy as np

with open('ch3/orbits.txt', 'r') as f:
    text = f.read()

data = text.split('\n')
arr = np.array([d.split(')') for d in data])
print(arr)

