n=int(input())
ls=list(map(int,input().split()))
ls1=[]
for i in range(len(ls)):
    if(ls[i]%2!=0):
        ls1.append(ls[i])
for i in range(len(ls)):
    if(ls[i]%2==0):
        ls1.append(ls[i])
for i in ls1:
    print(i,end=" ")