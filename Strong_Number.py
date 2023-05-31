import math
def fact(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    return fact
def stro(n):
    x=n
    c=0
    r=0
    s=0
    while(n!=0):
        r=n%10
        s=s+fact(r)
        n=n//10
    if s==x:
        c=1
    return c
n=int(input())
res=stro(n)
if res==1:
    print("The number %d is a strong number"%n)
else:
    print("The number %d is not a strong number"%n)
