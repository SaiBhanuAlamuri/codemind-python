n=int(input())
arr=list(map(int,input().split()))
temp=arr.copy()
temp.sort()
c=0
for i in range(n):
    if arr[i]!=temp[i]:
        c=c+1
        ind=arr.index(temp[i])
        arr[ind],arr[i]=arr[i],arr[ind]
print(c)