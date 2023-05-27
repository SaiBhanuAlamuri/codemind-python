a=int(input())
fa=0
fb=1
c=0
for i in range(100):
    if (fa==a):
        c=1
        break
    else:
        fn=fa+fb
        fa=fb
        fb=fn
        continue
if(c==1):
    print("True")
else:
    print("False")