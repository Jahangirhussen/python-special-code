import numpy as np

print("here we join 1D multiple array \n ")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([3, 9, 0])
arr = np.concatenate((arr1, arr2,arr3))
print("join multiple array with concatenate() keyword \n",arr,"\n")

