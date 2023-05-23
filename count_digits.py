def count(n):
    r=0
    d=0
    if(n<0):
        n=n*(-1)
    if(n!=0):
        while(n!=0):
            r=n%10
            d=d+1
            n=n//10
    elif(n==0):
        d=1
    return d
n=int(input())
ls=list(map(int,input().split()))
for i in ls:
    print(count(i),end=" ")
