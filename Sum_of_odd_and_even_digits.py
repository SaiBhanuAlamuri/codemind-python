n=int(input())
ls=list(map(int,input().split()))
ls1=[]
ls2=[]
for i in range(n):
    if(i%2==0):
        ls1.append(ls[i])
    else:
        ls2.append(ls[i])
if(sum(ls1)-sum(ls2)==0):
    print("YES")
else:
    print("NO")