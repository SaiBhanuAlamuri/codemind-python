import math
n=int(input())
ls=list(map(int,input().split()))
j=n-1
res=0
for i in range(len(ls)):
    if(j>=0):
        res=res+ls[i]*pow(2,j)
        j=j-1
print(res)
    