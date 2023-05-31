t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    c=0
    for i in range(0,m):
        if i*i%m==n:
            fs=i
            c=1
            break
    if c==0:
        print("-1")
    else:
        print(fs)

    
        