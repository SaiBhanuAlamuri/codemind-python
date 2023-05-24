a=input()
arr=list(a.split())
vow="aeiouAEIOU"
c=0
l=len(a)
mid=l//2
for j in range(mid):
        if a[j].isspace() or a[l-j-1].isspace():
            continue
        if a[j] in vow and a[l-j-1] not in vow:
            c=c+1
        if a[j]  not in vow and a[l-j-1] in vow:
            c=c+1
print(c)
        