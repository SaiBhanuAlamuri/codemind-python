n=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(len(ls)):
    if(ls[i]==0 or ls[i]==1):
        c=c+1
if(c==n):
    print("True")
else:
    print("False")