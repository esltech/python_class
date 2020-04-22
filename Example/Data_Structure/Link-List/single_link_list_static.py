#Creating a single link list static (Example-1)

class Node:
    def __init__(self):
        self.data=None
        self.nxt=None
    

    def assign_data(self,val):
        self.data=val

    def assign_add(self,addr):
        self.nxt=addr
    

class ListPrint:
    
    def printLinklist(self,tmp):
        while(tmp):
            print(tmp.data,end=' ')
            tmp=tmp.nxt
        print("")
    

head=Node() #Implementing Head Node
head.assign_data(5)

node2=Node()
node2.assign_data(7)
head.assign_add(node2)

node3=Node()
node3.assign_data(10)
node2.assign_add(node3)

pr=ListPrint()
pr.printLinklist(head)

