n=int(input())
ls=list(map(int,input().split()))
co=0
di=0
for i in range(len(ls)):
    if(ls[i]%2!=0 and  i%2!=0):
        co=co+1
    if(i%2!=0):
        di=di+1
if(co==di):
    print("True")
else:
    print("False")