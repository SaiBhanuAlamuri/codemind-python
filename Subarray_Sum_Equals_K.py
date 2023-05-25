m,n=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(m):
    s=0
    for j in range(i,m):
        s=s+a[j]
        if(s==n):
            c=c+1
print(c)
        