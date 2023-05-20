n=int(input())
ls=list(map(int,input().split()))
x,y=map(int,input().split())
s=0
for i in range(len(ls)):
    if(ls[i]<x or ls[i]>y):
        s=s+ls[i]
print(s)
    