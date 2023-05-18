def fun(n):
    r=0
    rev=0
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
f=0
l=0
dl=0
df=0
for i in range(n-1,1,-1):
    if(fun(i)==i):
        f=i
        break
for i in range(n+1,100000):
    if(fun(i)==i):
        l=i
        break
df=n-f
dl=l-n
if(df==dl):
    print("%d %d"%(f,l))
elif(df>dl):
    print("%d"%(l))
else:
    print("%d"%(f))
    