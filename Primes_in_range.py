import math
def fun(n):
    i=2
    while(i*i<=n):
        if(n%i==0):
            return 0
        i=i+1
    return 1
        
    
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if(fun(i)==1 and i!=1):
        c=c+1
print(c)