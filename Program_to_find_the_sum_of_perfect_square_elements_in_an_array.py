def fun(a):
    res=0
    if a==1:
        res=1
    else:
        for i in range(1,a):
            if i*i==a:
                res=1
                break
            
    if res==1:
        return 1
    else:
        return 0
n=int(input())
ls=list(map(int,input().split()))
sq=0
for i in ls:
    if(fun(i)==1):
        sq=sq+i
print(sq)