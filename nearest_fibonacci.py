n=int(input())
arr=[]
fa=0
fb =1
for i in range(100):
    arr.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
for i in range(100):
    if arr[i]>n:
        l=arr[i]
        f=arr[i-1]
        df=n-f
        dl=l-n
        if(df==dl):
            print(f,l)
        elif df>dl:
            print(l)
        else:
            print(f)
        break
    