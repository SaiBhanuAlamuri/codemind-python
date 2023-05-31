def fun(n):
    c=f=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if c==2:
        f=1
    return f
n=int(input())
m=int(input())
f=0
for i in range(1,10000):
    if(fun(n+m+i)==1):
        f=i
        break
print(f)
        