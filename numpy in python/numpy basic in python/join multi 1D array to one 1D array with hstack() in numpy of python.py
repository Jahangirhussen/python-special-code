import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr3 = np.array([9, 0, 9])

arr = np.hstack((arr1, arr2, arr3))

print("with hstack        ",arr)

arr = np.concatenate((arr1, arr2, arr3))

print("with concatenate   " ,arr)
