#Write a Python program to remove and print every third number 
# from a list of numbers until the list becomes empty.


def display_3rd_char(inp_str):
    inp_list=list(inp_str.replace(" ","")) #Removing the space from a String.
    for i in range(2,(len(inp_list)+1)):
        if (i+1)%3==0:
            #print("Index value is:",i)
            print("The value on %d index is:%s"%((i+1),inp_list[i]))


inp=input("Enter a string :")
display_3rd_char(inp)
