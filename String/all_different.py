# Write a Python function that takes a string and determines 
# whether all the characters are different from each other.

def check_duplicate_normal(l_inp):
    flag=False
    for i in l_inp:
        #print("List value:",i)
        for j in range(l_inp.index(i)+1,len(l_inp)):
            if i==l_inp[j]:
                flag=True
                print("Duplicate Exists with :",l_inp[j])
                return(flag)

def check_duplicate_set(l_inp):
    flag=False
    if len(l_inp)!=len(set(l_inp)):
        print("Length Mismatched!!!")
        flag=True
        return(flag)

inp=input("Please enter a string:")
list_inp=list(inp)

#Using normal process to check the duplicate in an input string.
#flg=check_duplicate_normal(list_inp)

#Using defining set process to check the duplicate in an input string.
flg=check_duplicate_set(list_inp)
if flg is True:
    print("Duplicate characters present into the String.")
else:
    print("All characters are unique in this String.")