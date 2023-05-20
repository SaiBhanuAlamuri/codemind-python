n=int(input())
ls=list(map(int,input().split()))
x,y=map(int,input().split())
m=-1
for i in range(len(ls)):
    if(ls[i]<x or ls[i]>y):
        if(ls[i]>m):
            m=ls[i]
print(m)
        