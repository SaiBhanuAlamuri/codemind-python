ls=list(map(str,input().split()))

for i in ls:
    c=0
    for j in str(i):
        c=c+1
    print(c,end=" ")
    