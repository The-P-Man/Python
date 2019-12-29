"""
=================
An animated image
=================

This example demonstrates how to animate an image.
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as a

# Create the figure
fig = plt.figure('Asteroidz')

# Initialize the image
im = plt.imshow(np.random.randint(3, size=(8, 8)), animated=True)

# i = 1
def update(*args):
    '''Returns an update of the diaplayed image'''
    # global i
    # i *= 2
    arr = np.random.randint(2, size=(8, 8))
    im.set_array(arr)
    return im,


ani = a.FuncAnimation(fig, update, interval=100, blit=True)
plt.show()

# """
# =================
# An animated image
# =================

# This example demonstrates how to animate an image.
# """
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# fig = plt.figure()


# def f(x, y):
#     return np.sin(x) + np.cos(y)

# x = np.linspace(0, 2 * np.pi, 120)
# y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

# im = plt.imshow(f(x, y), animated=True)


# def updatefig(*args):
#     global x, y
#     x += np.pi / 15.
#     y += np.pi / 20.
#     im.set_array(f(x, y))
#     return im,

# ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
# plt.show()

