n=int(input())
ls=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(n):
    for j in range(n):
        print(ls[i],end=" ")
    print("")