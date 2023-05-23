n=input()
arr=list(n.split())
v="aeiouAEIOU"
ls=[]
for i in arr:
    c=0
    for j in i:
        if j in v:
            c=c+1
    ls.append(c)
print(min(ls))
            
            
    