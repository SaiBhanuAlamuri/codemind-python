n=int(input())
ls=list(map(int,input().split()))
s=0
for i in range(len(ls)):
    if(ls[i]%2==0):
        s=s+ls[i]
print(s)