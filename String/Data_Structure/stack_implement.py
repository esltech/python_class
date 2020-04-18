
def printStack(ref_list):
    for i in ref_list:
        print(i)
    ref_list.pop(1)

stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
printStack(stack)
#stack.pop(1)
print("----------")
print(stack)
print(stack[:2])