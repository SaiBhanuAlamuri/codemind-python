import math 
n=int(input())
sq=int(pow(n,0.5))
c=0
for i in range(1,sq+1):
    if(i*i==n):
        c=1
if(c==0):
    print("False")
else:
    print("True")
        