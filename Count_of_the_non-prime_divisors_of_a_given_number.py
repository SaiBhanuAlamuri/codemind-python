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
ls=[]
for i in range(1,n+1):
    if n%i==0:
        if fun(i)==0:
            ls.append(i)
print(len(ls))
