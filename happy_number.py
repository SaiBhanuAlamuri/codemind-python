import math
def happy(n):
    f=0
    s=0
    r=0
    while(1):
        s=0
        while(n):
            r=n%10
            s=s+r*r
            n=n//10
        if s<10:
            break
        else:
            n=s
            continue
    
            
    if s==1 or s==7:
        f=1
    return f
n=int(input())
if(happy(n)==1):
    print("True")
else:
    print("False")