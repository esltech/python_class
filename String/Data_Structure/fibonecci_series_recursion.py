# Number Series: 0,1,1,2,3,5,8,13,21,34,55,89,144......
# Now the series evaluted as : 0,1,1,2,3,5,8,13,21,34,55,89,144......
# F(n)=F(n-1)+F(n-2) [when n>2 only]

def Fibonacci_without_rec(input_number):
    inp=input_number
    x=1
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

    return 1


def Fibonacci_rec(input_number):
    inp1=input_number
    if inp1<=1:
        return inp1
    
    return (Fibonacci_rec(inp1-1) + Fibonacci_rec(inp1-2))


user_inp=int(input("Enter the position for the fibonecci series:"))
fun_call=Fibonacci_without_rec(user_inp)
fun_call=Fibonacci_rec(user_inp)
print("Value is:",fun_call)
