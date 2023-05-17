n=int(input())
ls=list(map(int,input().split()))
od=0
for i in range(len(ls)):
    if(i%2!=0):
        od=od+ls[i]
print(od)
    