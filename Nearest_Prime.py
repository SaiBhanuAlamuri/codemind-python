def fun(n):
    c=0
    f=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if c==2:
        f=1
    return f
t=int(input())
f=l=dl=df=0
for l in range(t):
    n=int(input())
    for i in range(n-1,-1,-1):
        if fun(i)==1:
            f=i
            break
    for i in range(n,10000):
        if fun(i)==1:
            l=i
            break
    df=n-f
    dl=l-n
    if(df>dl):
        print(l)
    elif(dl>df):
        print(f)
    else:
        print(f)
        