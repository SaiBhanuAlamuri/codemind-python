ls=list(map(str,input().split()))
l=[]
c=0
for i in ls:
    c=0
    for j in str(i):
        c=c+1
    l.append(c)
print(max(l))
