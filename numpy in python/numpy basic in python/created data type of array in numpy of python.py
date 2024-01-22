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

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4,5,6,9], dtype='i')
print(arr)
print(arr.dtype)

'''
arr = np.array(['a', '2', '3'], dtype='i')#here a is string but dtype is='i' so its error#
print(arr)
'''
