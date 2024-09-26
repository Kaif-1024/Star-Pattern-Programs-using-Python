# Number Pattern
n=int(input()) 
space=n//2
val=1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,val+1):
        print(dummy,end=' ')
        if num<val//2+1:
            dummy+=1
        else:
            dummy-=1
    if row<n//2+1:
        space-=1
        val+=2
    else:
        space+=1
        val-=2
    print()
