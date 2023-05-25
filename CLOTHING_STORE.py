n=int(input())
a=list(map(int,input().split()))
p=0
for i in range(n):
    for j in range(n):
        if i!=j and a[i]==a[j] and a[i]!=-1:
            a[i]=-1
            a[j]=-1
            p=p+1
print(p)
        
        