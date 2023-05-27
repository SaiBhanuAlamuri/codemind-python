n=input()
m=input()
s=""
p=""
for i in n:
    if i.isspace():
        continue
    else:
        s=s+i.lower()
for i in m:
    if i.isspace():
        continue
    else:
        p=p+i.lower()
res=[]
for i in s:
    if i not in p:
        if i not in res:
            res.append(i)
for i in p:
    if i not in s:
        if i not in res:
            res.append(i)
res.sort()
print(len(res))
