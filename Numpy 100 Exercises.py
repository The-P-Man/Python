#%%
import numpy as np

print(dir(np))

# There are 622 numpy functions
print('There are', len(dir(np)), 'numpy functions')
# %% Print the numpy versions and configuration
print(np.__version__)
np.show_config()

# %% Create a null vector of size 10
z = np.zeros(10, dtype=int)
# z = np.full(10, np.nan)

# %% Get the memory size of an array
z = np.zeros(10, dtype='int8')
print(f'The vector {z} of dtype {z.dtype} takes up {z.size} x {z.itemsize} = {z.nbytes} bytes')
z = np.zeros(10, dtype='int16')
print(f'The vector {z} of dtype {z.dtype} takes up {z.size} x {z.itemsize} = {z.nbytes} bytes')
z = np.zeros(10, dtype='int32')
print(f'The vector {z} of dtype {z.dtype} takes up {z.size} x {z.itemsize} = {z.nbytes} bytes')


# %% Make the fifth value 1
z[4] = 1
z

# %% Create a vector from 10 to 49
z = np.arange(10,50)
z


# %% Reverse a vector
z[::-1]

# %% 3 x 3 matrix from 0 to 8
np.arange(9).reshape(3,3)

# %% Get indices of non-zero elements
z = np.array([1, 2, 0, 0, 4, 0])
i = np.nonzero(z)
# i = np.where(z != 0)
i

# %% 3 x 3 identity matrix
np.eye(3, dtype=int)


# %% Create a 3 x 3 x 3 array of random numbers
np.random.random((3,3,3))

# %% Create a 10 x 10 array of random numbers and find the min and max
z = np.random.random((10, 10))
z.min(), z.max()

# %% Create a random vector of size 10 and find the mean
z = np.random.random(10)
z.mean()

# %% Create a 2D array with 1s on the border and 0s inside
z = np.ones((4, 4), dtype=int)
z[1:-1,1:-1] = 0
z

# %% Add a border of 1s around an existing array
a = [1, 2, 3, 4, 5]
print('Pad with constant', np.pad(a, 1, 'constant'))
print('Pad with edge', np.pad(a, 1, 'edge'))
print('Pad with maximum', np.pad(a, 1, 'maximum'))
print('Pad with minimum', np.pad(a, 1, 'minimum'))
print('Pad with mean', np.pad(a, 1, 'mean'))
print('Pad with median', np.pad(a, 1, 'median'))
print('Pad with reflect', np.pad(a, 1, 'reflect'))

z = np.array([[1,2],[3,4]])
print('Pad with constant', np.pad(z, pad_width=1, mode='constant'))


# %% What is the result
print(0 * np.nan)           # nan
print(np.nan - np.nan)      # nan
print(np.nan == np.nan)     # False
print(np.inf >= np.nan)     # False
print(np.nan in set([np.nan])) # True
print(0.3 == 0.1 * 3)       # False


# %% Create a 5 x 5 matrix with 1, 2, 3, 4 and 5 just below the diagonal

z = np.diag(np.arange(1, 5), k=-1)
z
# %% Create an 8 x 8 checkerboard pattern

z = np.zeros((8,8), dtype=int)
z[0::2, 0::2] = 1
z[1::2, 1::2] = 1
z

# %% What's the x,y,z of the 100th element of a (6,7,8) array
s = (6,7,8)
np.unravel_index(100, s)
# z = np.arange(np.prod(s)).reshape(s)

# %% Create a checkerboard using the tile function
z = np.diag([1,1])
np.tile(z, (4,4))

# %% Normalize a matrix
z = np.random.random((8, 8))
print(np.round(z,2))
z = (z - z.mean()) / z.std()
print(np.round(z,2))



# %% Create a custom dtype that describes color as 4 unsigned bytes.
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])


# %% Multiply a 5 x 3 matrix with a 3 x 2 matrix
A = np.random.randint(10, size=(5,3))
B = np.random.randint(10, size=(3,2))
A @ B # np.dot(A, B)

# %% Negate all elements between 3 and 8
z = np.arange(10)
z[(3 < z) & (z < 8)] = -1 * z[(3 < z) & (z < 8)]
z
# %