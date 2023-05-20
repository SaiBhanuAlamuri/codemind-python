n=int(input())
ls=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(ls)):
    if(k==ls[i]):
        c=c+1
print(c)