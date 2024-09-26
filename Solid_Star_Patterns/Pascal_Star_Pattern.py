# 1. Approach1
n=int(input())
space=n-1
star=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        if row%2!=0:
            if st%2!=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        else:
            if st%2==0:
                print(' ',end=' ')
            else:
                print('*',end=' ')
    space-=1
    star+=2
    print()

# 2. Approach2 (Easier One)
n=int(input())
space=n-1
star=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print('*',end='   ')
    space-=1
    star+=1
    print()
