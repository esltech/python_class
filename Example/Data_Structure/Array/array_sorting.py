
#Sorting Array with time complexity O(n^2) 

import array as arr
inp_arr=arr.array('i',[])
num=int(input("Please enter the no of element:"))
for i in range(0,num):
    print("Enter %dth number"%(i),end=':')
    val=int(input())
    inp_arr.append(val)
print("")
print("Unsorted Array is:",end=' ')
for i in inp_arr:
    print(i,end=' ')

print("")

for i in range(0,num):
    for j in range(0,(num-i)-1):
        if inp_arr[j]>inp_arr[j+1]:
            #print("j:",j)
            tmp=inp_arr[j]
            inp_arr[j]=inp_arr[j+1]
            inp_arr[j+1]=tmp
        else:
            pass
print("")
print("Sorted Array is:",end='')
for i in range(0,num):
    print(inp_arr[i],end=' ')
print("")

