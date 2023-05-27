s=input()
res=[]
for i in s:
    if i not in res:
        res.append(i)
if(len(s)==len(res)):
    print("True")
else:
    print("False")
    