def fun(n):
    c=0
    flag=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        flag=1
    else:
        flag=0
    return flag
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(fun(i)==1):
        print(i)