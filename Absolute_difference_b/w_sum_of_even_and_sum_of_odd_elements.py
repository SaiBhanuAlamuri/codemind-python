n=int(input())
ls=list(map(int,input().split()))
e=0
o=0
for i in range(len(ls)):
    if(ls[i]%2==0):
        e=e+ls[i]
    else:
        o=o+ls[i]
print(abs(e-o))