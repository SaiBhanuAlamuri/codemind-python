def col(l):
    m=sorted(l)
    return l==m
a,b=map(int,input().split())
mat=[]
for i in range(a):
    x=list(map(int,input().split()))
    mat.append(x)
c=0
for j in range(b):
    z=[]
    for i in range(a):
        z.append(mat[i][j])
    if col(z):
        c=c+1
print(c)
        