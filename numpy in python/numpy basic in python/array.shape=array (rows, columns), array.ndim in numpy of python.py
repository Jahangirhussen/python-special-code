import numpy as np

arr_3d = np.array([[1, 2, 3,0], [4, 5, 6,9],[2,3,4,8]])

shape = arr_3d.shape  # Returns the shape of the array (rows, columns)
dimensions = arr_3d.ndim  # Returns the number of dimensions

print("Array Shape:", shape)
print("Number of Dimensions:", dimensions)
