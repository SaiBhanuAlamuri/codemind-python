def pal(n):
    x=n
    r=rev=f=0
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if x==rev:
        f=1
    return f
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(pal(i)==1):
        print(i,end=" ")