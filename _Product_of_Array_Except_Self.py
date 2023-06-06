n=int(input())
ls=list(map(int,input().split()))
p=1
for i in range(n):
    p=1
    for j in range(n):
        if i!=j:
            p=p*ls[j]
    print(p,end=" ")
        