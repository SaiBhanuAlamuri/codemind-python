def fun(n):
    r=d=e=o=0
    f=0
    while(n!=0):
        r=n%10
        d=d+1
        if(r%2==0):
            e=e+1
        else:
            o=o+1
        n=n//10
    if d==e:
        f=1
    elif d==o:
        f=2
    else:
        f=0
    return f
n=int(input())
res=fun(n)
if(res==1):
    print("Even")
elif(res==2):
    print("Odd")
else:
    print("Mixed")