n=input()
vow="aeiou"
arr=[]
for i in n:
    if i  in vow:
        if i not in arr:
            arr.append(i)
if(len(arr)==len(vow)):
    print(0)
else:
    for i in vow:
        if(i not in arr):
            print(i,end=" ")
        
