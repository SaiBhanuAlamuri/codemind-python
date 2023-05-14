n=int(input())
a=list(map(int,input().split()))
c=co=0
ma=0
for i in range(n):
    c=0
    for j in range(n):
        if i!=j:
            if a[i]==a[j]:
                c=1
                break
    if c==1:
        continue
    else:
       if(ma<a[i]):
           ma=a[i]
           co=co+1
if(co>0):
    print(ma)
else:
    print(-1)
        
            
        