import math
def count(n):
    r=0
    d=0
    while(n!=0):
        r=n%10
        d=d+1
        n=n//10
    return d
def fun(n):
    flag=0
    dc=count(n)
    r=0
    x=n
    s=0
    while(n!=0):
        r=n%10
        s=s+pow(r,dc)
        dc=dc-1
        n=n//10
    if x==s:
        flag=1
    return flag

   
    
n=int(input())
if(fun(n)==1):
    print("True")
else:
    print("False")
