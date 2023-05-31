def prime(n):
    c=0
    f=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        f=1
    return f
def mega(n):
    pc=0
    d=0
    f=0
    x=n
    while(n!=0):
        r=n%10
        d=d+1
        if prime(r)==1:
            pc=pc+1
        n=n//10
    if d==pc and prime(x)==1 :
        f=1
    return f
n=int(input())
res=mega(n)
if res==1:
    print("Mega Prime")
else:
    print("Not Mega Prime")
