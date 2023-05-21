n=int(input())
ls=list(map(int,input().split()))
k=int(input())
s=0
for i in range(len(ls)):
        if(ls[i]<=k):
            s=s+ls[i]
print(s)
    