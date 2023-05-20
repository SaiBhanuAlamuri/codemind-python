n=int(input())
ls=list(map(int,input().split()))
s=0
for i in ls:
    s=s+i
avg=(s/n)
print("%0.2f"%(avg))