# Right Kaju-Katli
n=int(input())
star=1
space=n//2
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ', end=' ')
    for st in range(1, star+1):
        print('*', end=' ')
    print()
    if row<n//2+1:
        space-=1
        star+=1
    else:
        star-=1

# Left Kaju-Katli
n=int(input())
star=1
space=0
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ', end=' ')
    for st in range(1, star+1):
        print('*', end=' ')
    print()
    if row<n//2+1:
        star+=1
    else:
        star-=1
        space+=1
