def fun(n):
    return (n[::-1])
ls=list(map(str,input().split()))
for i in range(len(ls)):
    ls[i]=fun(ls[i])
for i in ls:
    print(i,end=" ")