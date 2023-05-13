n=int(input())
arr=[n]
arr=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if i!=j:
            if(arr[i]==arr[j] and arr[i]!=-1):
                arr[i]=-1
                arr[j]=-1
c=0
for i in arr:
    if i!=-1:
        print(i,end=" ")
        c=c+1
if(c==0):
    print("-1")
        