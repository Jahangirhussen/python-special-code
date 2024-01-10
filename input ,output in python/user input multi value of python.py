''' multi type input from user here the syntax'''

#multi string input from user
x, y ,z= input("Enter three(how much need_give the all variable) numbers separated by a space: ").split()
print(x+y+z)

'''multi integer input from user but need #commas of gap of two integer'''
list1=list(map (int, input("Enter multiple integers separated by commas: ").split(",")))
print("hi\n",list1)
