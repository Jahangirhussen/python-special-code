'''
note: axis does't work on 1D array that's why we use strak
'''
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 0, 8])


arr = np.stack((arr1, arr2, arr3), axis=1)

print("axis does not work in 1D so use stack  \n ",arr)

# same_column + same_column
