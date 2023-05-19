def fun(n):
    c=0
    flag=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        flag=1
    else:
        flag=0
    return flag

t=int(input())
for i in range(t):
    f=0
    l=0
    dif1=0
    dif2=0
    n=int(input())
    for i in range(n-1,1,-1):
        if(fun(i)==1):
            f=i
            break
        
    for i in range(n,10000):
        if(fun(i)==1):
            l=i
            break
    dl=l-n
    df=n-f
    if(dl>df):
        print(f)
    elif(df>dl):
        print(l)
    else:
        if(f>l):
            print(l)
        else:
            print(f)
        