import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(9).reshape(3,3)
# print(arr)

# plt.figure(num=1)
# plt.imshow(arr, cmap='summer')
# plt.show()

plt.figure(num=2)
plt.imshow(arr, cmap='gray', aspect=1, norm=1)
plt.show()