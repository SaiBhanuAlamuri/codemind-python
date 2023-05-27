def pal(n):
    f=0
    r=0
    rev=0
    x=n
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if x==rev:
        f=1
    return f
        
n=int(input())
fs=0
ls=0
for i in range(n-1,-1,-1):
    if (pal(i)==1):
        fs=i
        break
for i in range(n+1,10000):
    if (pal(i)==1):
        ls=i
        break
df=n-fs
dl=ls-n
if(df>dl):
    print(ls)
elif(df==dl):
    print("%d %d"%(fs,ls))
else:
    print(fs)
