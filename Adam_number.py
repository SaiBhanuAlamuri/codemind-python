import math
def fun(n):
    r=0
    rev=0
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
     
n=int(input())
nr=fun(n)
sq=n*n
sqr=nr*nr
if(fun(sqr)==sq):
    print("True")
else:
    print("False")

        