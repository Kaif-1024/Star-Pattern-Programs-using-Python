# Hollow House
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>n//2+1:
            if col==1 or row==n or col==n:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        else:
            if row+col==n//2+2 or col-row==n//2:
                print('*', end=' ')
            else:
                print(' ', end=' ')                                    
    print()

# Hollow House with Outline
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>n//2+1:
            if col==1 or row==n or col==n:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        else:
            if row+col==n//2+2 or col-row==n//2 or row==n//2+1:
                print('*', end=' ')
            else:
                print(' ', end=' ')                                    
    print()

# Full House
n=int(input())
space=n//2
star=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>n//2+1:
            for st in range(1,n+1):
                print('*',end=' ')
            break
    else:
        for sp in range(1,space+1):
            print(' ', end=' ')
        for st in range(1,star+1):
            print('*', end=' ')
        
        star+=2
        space-=1
    print()
