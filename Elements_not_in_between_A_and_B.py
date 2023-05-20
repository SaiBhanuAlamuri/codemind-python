n=int(input())
ls=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
for i in range(len(ls)):
    if(ls[i]<x or ls[i]>y):
        print(ls[i],end=" ")
        c=1
if(c!=1):
    print("-1")