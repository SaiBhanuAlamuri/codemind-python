import math
n=int(input())
ls=list(map(int,input().split()))
c=0
s=0
for i in range(len(ls)):
    s=s+ls[i]
avg=int(s/n)
for i in range(len(ls)):
    if(ls[i]<=avg):
        c=c+1
print(c)