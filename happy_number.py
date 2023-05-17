import math
def fun(n):
    r=0
    s=0
    while(1):
        s=0
        while(n!=0):
            r=n%10
            s=s+pow(r,2)
            n=n//10
        if(s>9):
            n=s
            continue
        else:
            break
    if(s==1 or s==7):
        res=1
    else:
        res=0
    return res
n=int(input())
if(fun(n)==1):
    print("True")
else:
    print("False")
            