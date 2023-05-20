n=int(input())
ls=list(map(int,input().split()))
s=0
for i in ls:
    s=s+i
avg=int(s/n)
if avg in ls:
    print("True")
else:
    print("False")
    