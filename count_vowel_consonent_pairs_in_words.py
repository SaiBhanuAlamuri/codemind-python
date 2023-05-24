a=input()
arr=list(a.split())
vow="aeiouAEIOU"
c=0
for i in arr:
    l=len(i)
    mid=l//2
    for j in range(mid-1,-1,-1):
        if i[j] in vow and i[l-j-1] not in vow:
            c=c+1
        if i[j]  not in vow and i[l-j-1] in vow:
            c=c+1
print(c)
        