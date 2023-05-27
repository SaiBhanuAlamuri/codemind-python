import math
def count(n):
    d=0
    while(n!=0):
        r=n%10
        d=d+1
        n=n//10
    return d
n=int(input())
sq=n*n
x=pow(10,count(n))
sqm=sq%x
if(sqm==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
        
