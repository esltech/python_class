# Create Link List dynamically as per the user input.(Example-2)

class Node:
    def __init__(self):
        self.data=None
        self.nxt=None
    

    def assign_data(self,val):
        self.data=val

    def assign_add(self,addr):
        self.nxt=addr



def_list=list()
list_len=int(input("Please enter the no of link list element:"))
for i in range(0,list_len):

    def_list.append(Node())
    def_list[i].assign_data(int(input("Enter the list value:")))
    if i>0:
        def_list[i-1].assign_add(def_list[i])

tmp=def_list[0]
for i in range(0,len(def_list)):
    print(tmp.data,end=' ')
    tmp=tmp.nxt
print("")
