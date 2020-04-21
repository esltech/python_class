import array as arr # importing Array package.
inp_array= arr.array('i',[])
inp_array.insert(0,0) # Insert method
print(inp_array[0]) 
inp_array.append(1) #   Append Method
inp_array.append(2)
inp_array.append(3)
inp_array.append(4)
inp_array.append(5)
inp_array.insert(2,7)  
for i in inp_array:
    print("Array value is:",i)
inp_array.pop(2)    #   POP Method
inp_array.remove(4) #   Remove method
for i in inp_array:
    print("Array value is:",i)

