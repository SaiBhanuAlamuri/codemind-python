n=int(input())
arr=list(map(int,input().split()))
xs=0 
ys=0
for i in range(n):
    if(i%2==0):
        xs=xs+arr[i]
    else:
        ys=ys+arr[i]
diff=abs(xs-ys)
if diff%4==0:
    print("X")
else:
    print("Y")