n=int(input())
m=int(input())
s=0
s2=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
for i in range(1,m):
    if(m%i==0):
        s2=s2+i
if(s==m and s2==n):
    print("Amicable")
else:
    print("Not Amicable")
        