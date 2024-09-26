n=int(input())
for row in range(1,n*2):
    for col in range(1,n*2):
        if row<n:
            if row+col==n+1 or col-row==n-1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        else:
            if row-col==n-1 or row+col==n*3-1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
    print()
