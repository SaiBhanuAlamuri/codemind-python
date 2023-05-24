n=input()
arr=list(n.split())
l=s=0
m=d=0
for i in arr:
    l=0
    m=10000
    for j in i:
        if ord(j)>l:
            l=ord(j)
        if ord(j)<m:
            m=ord(j)
    d=d+l
    s=s+m
print(d-s)