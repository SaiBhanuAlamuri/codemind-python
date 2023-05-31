n=int(input())
arr=[]
fa=0
fb=1
for i in range(100):
    arr.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
for i in range(n):
    print(arr[i],end=" ")
    