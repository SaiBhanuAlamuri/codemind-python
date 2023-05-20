def fun(n):
    flag=0
    if(n%2!=0):
        flag=1
    return flag

n=int(input())
ls=list(map(int,input().split()))
f=0
for i in range(n-1,0,-1):
    if(fun(ls[i])==1):
        f=ls[i]
        break
print(f)