n=int(input())
space=0
star=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ', end=' ')
    for st in range(1,star+1):
        print('*', end=' ')
    print()
    space+=1
