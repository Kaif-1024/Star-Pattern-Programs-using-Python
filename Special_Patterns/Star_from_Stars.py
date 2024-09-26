# Actual Star with Stars
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col or row+col==n+1 or col==n//2+1 or row==n//2+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Star inside Square
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col or row+col==n+1 or col==n//2+1 or row==n//2+1 or row==1 or col==1 or row==n or col==n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
