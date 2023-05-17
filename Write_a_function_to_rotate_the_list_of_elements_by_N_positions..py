n=int(input())
arr=list(map(int,input().split()))
k=int(input())
for i in range(k):
    temp=arr[0]
    val=0
    arr[0]=arr[n-1]
    for j in range(1,len(arr)):
        val=arr[j]
        arr[j]=temp
        temp=val
for i in arr:
    print(i,end=" ")
        
        