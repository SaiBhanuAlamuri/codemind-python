n=input()
arr=list(n.split())
m=arr[len(arr)-1][0]
for i in arr[len(arr)-1]:
    if(ord(i)<ord(m)):
        m=i
if m.lower() in arr[len(arr)-1]:
    print(m.lower())
else:
    print(m)