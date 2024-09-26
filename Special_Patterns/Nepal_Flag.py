# Nepal Flag
n=int(input()) #input-->Odd No.
for row in range(1,n*3-1):
    for col in range(1,n+1):
        if col==1:
            print('*', end='  ')
        elif row<n+1:
            if row>=col:
                print('*', end='  ')
            else:
                print(' ', end='  ')
        elif row>n and row<n*2:
            if row-col==n-1 or row-col>=n:
                print('*', end='  ')
            else:
                print(' ', end='  ')
    print()
