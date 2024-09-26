# Actual Pascal's Triangle

from math import factorial as fact
n=int(input())
space=n-1
val=0
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ', end='  ')
    for st in range(0,row):
        print(fact(val) // (fact(st) * fact(val - st)), end='    ')
    print()
    space-=1
    val+=1
