n=input()
res=[]
for i in n:
    if i not in res:
        res.append(i)
if len(res)==len(n):
    print("Unique Number")
else:
    print("Not Unique Number")