# Base with all Positions
n=int(input())
for row in range(1,n*2):
    for col in range(1,n+1):
        if col==n or row+col==n+1 or row-col==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Base with Odd Positions
n=int(input())
for row in range(1,n*2):
    for col in range(1,n+1):
        if (col==n and row%2!=0) or row+col==n+1 or row-col==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
