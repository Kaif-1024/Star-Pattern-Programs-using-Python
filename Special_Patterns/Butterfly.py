# Butterfly
n=int(input()) # Even Input
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=n//2:
            if (row>=col) | (row+col>=n+1):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        else:
            if (row+col<=n+1) | (row<=col):
                print('*',end=' ')
            else: 
                print(' ', end=' ')
    print()
