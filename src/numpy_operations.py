import numpy as np

vec = np.random.uniform(1, 20, 20)
arr = vec.reshape(4, 5)

max_indices = np.argmax(arr, axis=1)
arr[np.arange(4), max_indices] = 0

print(arr)
