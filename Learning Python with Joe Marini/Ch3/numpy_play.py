#%%
import numpy as np

# %%

x = np.arange(12).reshape(3,4)
x = np.random.randint(10, size=(3,4))
m, n = x.shape


print('x is', x)
print('The transpose is', x.T)

print('The shape is', x.shape)
print('There are', m, 'rows and', n, 'columns')
print('Dimensions', x.ndim)
print('Datatype', x.dtype)

print('The corners are', x[::m-1, ::n-1])
print('The array flipped left-right and top-bottom', x[::-1, ::-1])
print('The array flattened', x.flatten()) # x.ravel() does not create a copy
print(x.T)

# %%
if x.all():
    print('There are no zeros')
else:
    print('There is at least one zero')

if x.any():
    print('There is at least one non-zero')
else:
    print('All zeros')

print(f'The maximum value {x.max()} occurs at position {x.argmax()}: \
row {x.argmax() // (x.shape[0]+1) + 1} and \
column {x.argmax() % (x.shape[1]) + 1}')

print(f'The minimum value {x.min()} occurs at position {x.argmin()}: \
row {x.argmin() // (x.shape[0]+1) + 1} and \
column {x.argmin() % x.shape[1] + 1}')




# %%
x.clip(1,3) # will clip all the numbers to between 1 and 3
x.put((0,4,8), (1,2,3)) # Put 1, 2, 3 down the left hand side
x
