# 1. Base at Odd Positions
n=int(input())
for row in range(1,n+1):
    for col in range(1,(n*2)):
        if (row==n and col%2!=0) or row+col==n+1 or col-row==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print() 


# 2. Base at all positions
n=int(input())
for row in range(1,n+1):
    for col in range(1,(n*2)):
        if row==n or row+col==n+1 or col-row==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print() 
