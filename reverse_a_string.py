def fun(n):
    return (n[::-1])
ls=list(map(str,input().split()))
ls=ls[::-1]
for i in range(len(ls)):
    ls[i]=fun(ls[i])
    print(ls[i],end=" ")

