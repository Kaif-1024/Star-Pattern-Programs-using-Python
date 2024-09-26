n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if col>=row:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
