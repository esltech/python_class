#print hello world to the Python console.
print("It is printing a String.")
#print(pow(3,5))
#print((6//2))
import math as mth
print(int(mth.sqrt(7)))
v_list=('A','E','I','O','U')
inp=input("Enter a string:")
list_inp=list(inp)
print(list_inp)
inp=inp.replace('a','%').replace('A','%')
print("After replacing A:")
inp=inp.replace('e','%').replace('E','%')
inp=inp.replace('i','%').replace('I','%')
inp=inp.replace('o','%').replace('O','%')
inp=inp.replace('u','%').replace('U','%')
print("String after replace:",inp)

