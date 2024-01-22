import numpy as np

print("start copy method here ")
arr = np.array([1, 2, 3, 4, 5])
new_arr = arr.copy()
arr[0] = 42#old arr update but not new arr

print("old array with updated ",arr)
print("new array but update old after copy",new_arr)


print("start VIEW method here ")
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()#if i update anywhare any arry theb buth array updated
#arr[0] = 42
x[0] = 42#update new arrar
print(arr)
print(x)
 