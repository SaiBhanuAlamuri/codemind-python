def count(n):
    d=0
    while(n!=0):
        r=n%10
        d=d+1
        n=n//10
    return d
n=int(input())
ls=list(map(int,input().split()))
ls1=[]
c=0
for i in ls:
    ls1.append(count(i))
x=min(ls1)
for i in ls:
    if(count(i)==x):
        c=c+1
print(c)
    
    

        