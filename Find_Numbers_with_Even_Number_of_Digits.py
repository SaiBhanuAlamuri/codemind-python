def fun(a):
    c=0
    r=0
    while a!=0:
        r=a%10
        c=c+1
        a=a//10
    return c
n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(n):
    if(fun(arr[i])%2==0):
        s=s+1
print(s)
        