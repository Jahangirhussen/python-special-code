'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

import numpy as np

print("here float to int data type")
old_arr = np.array([1.1, 2.1, 3.1])
print("old array",old_arr)
print("old array data type",old_arr.dtype)
new_arr = old_arr.astype('i')
print("new array",new_arr)
print("new array data type",new_arr.dtype)

print("here int to bool data type")
old_arr = np.array([1, 0, 3,6])#without zero all true
print("old array",old_arr)
print("old array data type",old_arr.dtype)
new_arr = old_arr.astype(bool)
print("new array",new_arr)
print("new array data type",new_arr.dtype)
