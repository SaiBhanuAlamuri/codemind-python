def pal(n):
    x=n
    flag=0
    r=0
    rev=0
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if(rev==x):
        flag=1
    return flag
n=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(len(ls)):
    if(pal(ls[i])==1):
        c=c+1
print(c)
        
        