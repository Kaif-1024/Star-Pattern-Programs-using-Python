n=int(input()) # Only for input-->9
space1=n//2
space2=0
star1=1
star2=0
for row in range(1,n+1):
    for sp in range(1,space1+1):
        print(' ',end=' ')
    for st in range(1,star1+1):
        print('*',end=' ')
    for sp in range(1,space2+1):
        print(' ',end=' ')
    for st in range(1,star2+1):
        print('*',end=' ')
    if row<n//2+1:
        if row<n//2-1:
            star1+=2
        elif row==n//2-1:
            star1-=n//2-1
            space2+=n//2-1
            star2=star1
        else:
            star1+=1
            star2+=1
        space1-=1
    else:
        if row<n//2+2:
            star1-=1
            star2-=1
        elif row==n//2+2:
            star1+=n//2-1
            star2=0
        else:
            star1-=2
        space1+=1
    print()
