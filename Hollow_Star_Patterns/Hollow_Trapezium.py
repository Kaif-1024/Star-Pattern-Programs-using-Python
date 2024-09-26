n=int(input())
for row in range(1,n+1):
    for col in range(1,n*2+2):
        if row+col==n+1 or col-row==n+1 or row==n or (col==n+1 and row==1):
            print('*', end='   ')
        else:
            print(' ', end='   ')
    print()
