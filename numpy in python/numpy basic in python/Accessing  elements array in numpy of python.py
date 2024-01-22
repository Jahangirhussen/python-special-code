import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6],[0,1,9]])

# Accessing elements
element_at_0_1 = arr_2d[0, 1]=5  # Accessing element at row 0, column 1
print(arr_2d[0, 1])

row_1 = arr_2d[1, :]=5  # Accessing the entire second row
print(arr_2d[1, :])

row_2=arr_2d[2,:]=[1,2,3]  # Accessing the entire third row
print(arr_2d[2, :])