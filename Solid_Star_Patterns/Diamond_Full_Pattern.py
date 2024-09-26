n=int(input())
space=n//2
star=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ', end=' ')
    for st in range(1,star+1):
        print('*',end=' ')
    if row<n//2+1:
        space-=1
        star+=2
    else:
        space+=1
        star-=2
    print()
