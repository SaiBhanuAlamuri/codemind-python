def fun(n):
    c=0
    flag=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        flag=1
    else:
        flag=0
    return flag

n=int(input())
f=0
l=0
df=0
dl=0
for i in range(n-1,1,-1):
    if(fun(i)==1):
        f=i;
        break
for i in range(n,100000):
    if(fun(i)==1):
        l=i;
        break
df=n-f
dl=l-n
print(min(df,dl))