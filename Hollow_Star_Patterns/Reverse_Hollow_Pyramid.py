# Base at all Poitions
n=int(input())
for row in range(1,n+1):
    for col in range(1,(n*2)):
        if row==1 or row==col or row+col==n*2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Base at Odd Positions
n=int(input())
for row in range(1,n+1):
    for col in range(1,(n*2)):
        if (row==1 and col%2!=0) or row==col or row+col==n*2:
            print('*', end=' ')
        else:
            print(' ', end=' ')  
    print() 
