n=int(input())
ar=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(n,0,-1):
    for j in range(i):
        print(ar[i-1],end=" ")
    print("")