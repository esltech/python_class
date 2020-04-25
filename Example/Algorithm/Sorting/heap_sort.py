import array as arr

def printArray(inp_arr,arr_len):
    for i in range(0,(arr_len)):
        print(inp_arr[i],end=' ')
    print("")

def swapArrayElement(inp_arr,pos1,pos2):
    tmp=inp_arr[pos1]
    inp_arr[pos1]=inp_arr[pos2]
    inp_arr[pos2]=tmp
    #print(inp_arr,len(inp_arr))


def heapifyArray(inp_arr,l):
    print("----- Value of l:",l)
    for j in range(0,(len(inp_arr)-l)):

        node=j
        if (2*j)+1 <(arr_len-i):
            left=(2*j)+1
        else:
            left=None
        if (2*j)+2 <(arr_len-i):
            right=(2*j)+2
        else:
            right=left
        if j==(arr_len-i):
            right=left
        print("Node=",node)
        print("Left=",left)
        print("Right=",right)

        
        
        if left is not None and right is not None:
            print("Inside cond1")
            if a[node]<a[left] and a[node]< a[right]:
                if a[left]>a[right]:
                    print("left(%d)>right(%d)"%(left,right))
                    swapArrayElement(a,node,left)
                    print("Now array is l>r: ")
                    printArray(a,arr_len)
                    heapifyArray(inp_arr,j)
                    
                else:
                    print("left(%d)<=right(%d)"%(left,right))
                    swapArrayElement(a,node,right)
                    print("Now array is l<=r: ")
                    printArray(a,arr_len)
                    heapifyArray(inp_arr,j)
                    

            if a[node]<a[left] and a[node]> a[right]:
                print("left(%d)>node(%d)"%(left,node))
                swapArrayElement(a,node,left)
                printArray(a,arr_len)
                heapifyArray(inp_arr,j)

            if a[node]>a[left] and a[node]< a[right]:
                print("Right(%d)>node(%d)"%(right,node))
                swapArrayElement(a,node,right)
                printArray(a,arr_len)
                heapifyArray(inp_arr,j)

        if left is not None and right is None:
            print("Inside condition 2")
            if a[node]<a[left] and a[node]> a[right]:
                print("Left(%d)>node(%d)"%(left,node))
                swapArrayElement(a,node,left)
                heapifyArray(inp_arr,j)
    



#a=arr.array('i',[5,3,1,12,8,2])
#a=arr.array('i',[2,5,3,1])
a=arr.array('i',[6,5,9,15,2,8])
a=arr.array('i',[65,70,17,28,9,92,4])
arr_len=len(a)
print("Input array:",end=' ')
printArray(a,arr_len)
#for i in range(0,(int(arr_len/2))+1):
for i in range(0,arr_len):
    print("---------- Value of i:",i)
    heapifyArray(a,i)    
    print("Input array before swap:",end=' ')
    printArray(a,arr_len)
    swapArrayElement(a,0,(arr_len-(i+1)))
    print("Input array after swap:",end=' ')
    printArray(a,arr_len)
            