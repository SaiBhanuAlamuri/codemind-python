n=int(input())
ls=list(map(int,input().split()))
e=0
for i in range(len(ls)):
    if(i%2==0):
        e=e+ls[i]
print(e)