a=input()
arr=list(a.split())
vow="aeiouAEIOU"
c=0
for i in arr:
    l=len(i)
    if(i[0] in vow and i[l-1] not in vow ):
        c=c+1
print(c)