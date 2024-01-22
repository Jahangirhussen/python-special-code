#Iterating means going through elements one by one

import numpy as np

arr = np.array([  [[1, 2, 3], [4, 5, 6]],   [[7, 8, 9], [10, 11, 12]]  ])
print(" full array with array shape ")
for x in arr:
      print(x)
      
      print("arr shape :",arr.shape)
      print("full array in one by one single element")
      
          
for x in arr:# x 2 time repect
    for y in x:#y 2 raw
        for z in y:# 3 calumn 
            print(z) #than back x in range por next time repect
