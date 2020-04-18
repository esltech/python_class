n = int(input('enter the number: '))

a= 1

b= 1

for i in range(1, n+1):

    if(i%2!=0):

       

        a = a*2

    else:      

        b = b*3

if(n%2!=0):

    print('\n{} term of series is {}\t'.format(n,a/2))

else:

    print('\n{} term of series is {}\t'.format(n,a/2))