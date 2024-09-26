# 1. Easy Approach
n=int(input())
for row in range(1,n+1):
    print('* '*row,end=' ')
    print()

# 2. Another Approach
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
