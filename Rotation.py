t=int(input())
f=0
temp=0

for l in range(t):
    n,k=map(int,input().split())
    ls=list(map(int,input().split()))
    for i in range(k):
        ft=ls[0]
        ls[0]=ls[n-1]
        for j in range(1,n):
            temp=ls[j]
            ls[j]=ft
            ft=temp
    for i in range(n):
        if(i==n-1):
            print(ls[i])
        else:
            print(ls[i],end=" ")
    