n=input()
arr=list(n.split())
v="aeiouAEIOU"

for i in arr:
    c=0
    for j in i:
        if j in v:
            c=c+1
    print(c,end=" ")

            
            
    