# Approach 1
n=int(input()) # No. of Rows
space=0
star1=n
star2=0
for row in range(1,n+1):
    for st in range(1,star1+1):
        print('*',end=' ')
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star2+1):
        print('*',end=' ')
    if row==1:
        space+=1
        star1=n//2
        star2=n//2
    elif row<n//2+1 and row>1:
        space+=2
        star1-=1
        star2-=1
    else:
        space-=2
        star1+=1
        if row==n-1:
            star2=n//2
        else:
            star2+=1
    print()

# Approach 2 (Easier)
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col<=n//2+2:
            print('*',end=' ')
        elif col-row>=n//2:
            print('*',end=' ')
        elif row-col>=n//2:
            print('*',end=' ')
        elif row+col>=n*2-n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
