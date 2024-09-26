# Alphabet Pattern
n=int(input()) # No. of Rows
space=n//2
item=1
val=ord('A')
for row in range(1,n+1):
    item_val=val
    for sp in range(1,space+1):
        print(' ',end=' ')
    for itm in range(1,item+1):
        print(chr(item_val),end=' ')
        item_val+=1
    if row<n//2+1:
        space-=1
        item+=2
        val=item_val
    else:
        space+=1
        item-=2
        val-=item
    print()
