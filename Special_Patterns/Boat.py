# ░░░░░░░░░░░░░░░░░░░░░░░░ BOAT ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
n=int(input())
space=0
star=n*2+1
for row in range(1,n+1):
    if row>n//2+2:
        for sp in range(1,space+1):
            print(' ', end=' ')
        for st in range(1,star+1):
            print('*', end=' ')
        print()
        space+=1
        star-=2
    else:
        for col in range(1,star+1):
            if col==n:
                print('*', end=' ')
            elif col<=n+6 and row<n//3+3:
                if row+col<=n+7 and col>=n:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')

            else:
                print(' ', end=' ')
        print()
