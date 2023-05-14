n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(n):
        if i!=j:
            if(a[j]<a[i]):
                c=c+1
    print(c,end=" ")

        