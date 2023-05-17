import math
n=int(input())
st=str(n)
ls=[]
s=0
for i in st:
    ls.append(int(i))

for i in range(len(st)):
    s=s+pow(ls[i],(i+1))
if(s==n):
    print("True")
else:
    print("False")
