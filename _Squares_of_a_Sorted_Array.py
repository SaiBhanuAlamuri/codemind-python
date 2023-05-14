n=int(input())
ls=list(map(int,input().split()))
ls.sort()
ls1=[]
for i in range(n):
    ls1.append(ls[i]*ls[i])
ls1.sort()
for i in range(n):
    print(ls1[i],end=" ")