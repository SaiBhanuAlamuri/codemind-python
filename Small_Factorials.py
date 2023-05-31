def fac(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    return fact
t=int(input())
for l in range(t):
    n=int(input())
    print(fac(n))
    