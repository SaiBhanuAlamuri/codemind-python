def su(n):
    s=0
    while(n!=0):
        r=n%10
        s=s+r
        n=n//10
    return s
    
n=int(input())
ls=list(map(int,input().split()))
so=0
for i in ls:
    so=so+su(i)
print(so)
    