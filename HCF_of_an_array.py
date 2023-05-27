n=int(input())
ls=list(map(int,input().split()))
mi=ls[0]
j=1
while j<n:
    if(ls[j]%mi==0):
        j=j+1
    else:
        mi=ls[j]%mi
print(mi)