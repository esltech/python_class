
def checkPrime1(inp_num):
    flag=True
    print("Inside Method:1")
    for i in range(2,(inp_num-1)):
        
        if inp_num%i==0:
            print("Number divisible by:",i)
            flag=False
    return flag

import math
def checkPrime2(inp_num):
    flag=True
    print("Inside Method:2")
    sq_inp_val=int(math.sqrt(inp_num))
    for i in range(2,(sq_inp_val+1)):
        
        if inp_num%i==0:
            print("Number divisible by:",i)
            flag=False
    return flag


inp=int(input("Enter a number to check:"))

#ret_bool_flag=checkPrime1(inp)
ret_bool_flag=checkPrime2(inp)
print("Return val:",ret_bool_flag)
if ret_bool_flag is True:
    print("Input number is PRIME")
else:
    print("Input number NOT PRIME")