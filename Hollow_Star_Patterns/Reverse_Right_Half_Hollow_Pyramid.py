n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==1 or col==1 or row+col==n+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
