def neon(n):
    sq=n*n
    r=0
    s=0
    f=0
    while(sq!=0):
        r=sq%10
        s=s+r
        sq=sq//10
    if s==n:
        f=1
    return f
n=int(input())
res=neon(n)
if res==1:
    print("Neon Number")
else:
    print("Not Neon Number")