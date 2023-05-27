n=input()
m=input()
s=""
p=""
for i in n:
    if i.isupper():
        s=s+i.lower()
    else:
        s=s+i
for i in m:
    if i.isupper():
        p=p+i.lower()
    else:
        p=p+i
a=list(s.split())
b=list(p.split())
res=[]
for i in b:
    if i in a:
        if i not in res:
            res.append(i)
if len(res)==0:
    print(0)
else:
    for i in res:
        print(i,end=" ")