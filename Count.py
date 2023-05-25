n=int(input())
arr=list(map(int,input().split()))
se=so=0
for i in arr:
    if i%2==0:
        se=se+1
    else:
        so=so+1
print(se,so)