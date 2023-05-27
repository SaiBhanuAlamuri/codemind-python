def fun(n):
    c=0
    f=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if c==2:
        f=1
    return f
n=int(input())
if(fun(n)==1):
    print("prime")
else:
    print("not a prime")
        