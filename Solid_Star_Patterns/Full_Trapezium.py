n=int(input()) #No. of Rows
space=n-1
star=n//2+1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ', end='   ')
    for st in range(1,star+1):
        print('*', end='   ')
    print()
    space-=1
    star+=2
