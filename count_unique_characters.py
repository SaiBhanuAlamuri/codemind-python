a=input()
ar=[]
for i in range(len(a)):
    if a[i].isspace():
        continue
    if a[i].upper() not in a[:i] and a[i].upper() not in a[i+1:]:
        if a[i].lower() not in a[:i] and a[i].lower() not in a[i+1:]:
            ar.append(a[i])
for i in range(len(ar)):
    for j in range(len(ar)-1):
        if ar[j+1]<ar[j]:
            ar[j],ar[j+1]=ar[j+1],ar[j]
print(len(ar))