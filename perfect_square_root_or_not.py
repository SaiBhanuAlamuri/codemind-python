import math
def fun(n):
    res=0
    x=int(pow(n,0.5))
    for i in range(1,x+1):
        if(i*i==n):
            res=1
    if(res==1):
        return 1
    else:
        return 0
n=int(input())
if(fun(n)==1):
    print("True")
else:
    print("False")