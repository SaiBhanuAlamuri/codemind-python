n=int(input())
ls=list(map(int,input().split()))
flag=0
for i in range(len(ls)):
    if((ls[i]%2==0 and  i%2==0)or ls[i]==0):
        flag=1
    elif(ls[i]%2==0 and i%2!=0):
        flag=0
        break
       
if(flag==1):
    print("True")
else:
    print("False")
