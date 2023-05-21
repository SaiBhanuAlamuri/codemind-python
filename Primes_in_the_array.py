def fun(n):
    flag=0
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        flag=1
    return flag
n=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(len(ls)):
    if(fun(ls[i])==1):
        c=c+1
print(c)
        
