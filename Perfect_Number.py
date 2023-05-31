def fun(n):
    s=0
    f=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    if s==n:
        f=1
        return True
    else:
        return False
        

n=int(input())
res=fun(n)
print(res)
