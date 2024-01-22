import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.array([[7, 9], [9, 2]])

arr = np.concatenate((arr1, arr2,arr3), axis=1) #axis =1 means 1st same_column + same_column
print("with axis \n ",arr)

arr = np.concatenate((arr1, arr2))
print("with out axis \n ",arr)


'''
note: axis does't work on 1D array that's why we use strak
'''