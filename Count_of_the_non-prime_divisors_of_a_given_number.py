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
c=0
for i in range(1,n+1):
    if(fun(i)==0 and n%i==0):
        c=c+1
print(c)