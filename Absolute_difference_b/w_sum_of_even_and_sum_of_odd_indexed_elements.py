n=int(input())
ls=list(map(int,input().split()))
o=[]
e=[]
for i in range(len(ls)):
    if(i%2==0):
        e.append(ls[i])
    else:
        o.append(ls[i])
print(abs(sum(o)-sum(e)))