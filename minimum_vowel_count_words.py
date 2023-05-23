n=input()
arr=list(n.split())
v="aeiouAEIOU"
m=1000
for i in arr:
    c=0
    for j in i:
        if j in v:
            c=c+1
    if(m>c):
        m=c
wc=0
for i in arr:
    c=0
    for j in i:
        if j in v:
            c=c+1
    if(c==m):
        wc=wc+1
print(wc)
