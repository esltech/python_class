# Number Series: 0,1,1,2,3,5,8,13,21,34,55,89,144......
# F(n)=F(n-1)+F(n-2)

inp=int(input("Enter the position for the fibonecci series:"))
x=0
y=1
l1=list()
if inp<0 :
    print("Wrong Input")
elif inp==1:
    l1.append(0)
    print("The fibonecci series is:",l1)
    print("The %dth fibonecci number: %d"%(inp,y))
elif inp>1:
    l1.append(x)
    l1.append(y)
    for i in range(2,inp):
        z=x+y
        print("The value of z:",z)
        l1.append(z)
        x=y
        y=z

    print("The fibonecci series is:",l1)
    print("The %dth fibonecci number: %d"%(inp,y))
