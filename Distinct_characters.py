a=input()
ar=[]
for i in a:
    if i.isspace():
        continue
    if i.lower() not in ar:
        ar.append(i.lower())
for i in range(len(ar)):
    for j in range(len(ar)-1):
        if(ar[j]>ar[j+1]):
            ar[j],ar[j+1]=ar[j+1],ar[j]
for i in ar:
    print(i,end="")