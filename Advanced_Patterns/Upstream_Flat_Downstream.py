# Upstream | Flat | Downstream
n=int(input()) 
up=n//100
flat=(n//10)%10
down=n%10
ul=0
if up>=down:
    ul=up
else:
    ul=down
space1=up
space2=flat
desgn=1
for row in range(1,ul+2):
    if row==1:
        for sp in range(1,space1+1):
            print(' ',end=' ')
        for ds in range(1,flat+1):
            print('_',end='_')
    else:
        for sp in range(1,space1+1):
            print(' ',end=' ')
        if up>down:
            for ds in range(1,desgn+1):
                print('_|',end='')
        else:
            if row<=up+1:
                for ds in range(1,desgn+1):
                    print('_|',end='')
        for sp in range(1,space2+1):
            print(' ',end=' ')
        if down>up:
            for ds in range(1,desgn+1):
                print('|_',end='')
        else:
            if row<=down+1:
                for ds in range(1,desgn+1):
                    print('|_',end='')
        if row>=2:
            if up>down:
                if row<=up:
                    space2+=2
                else:
                    space2+=1
            elif down>up:
                if row<=up+1:
                    space2+=2
                else:
                    space2+=1
            else:
                if row<=up:
                    space2+=2
    space1-=1
    print()
