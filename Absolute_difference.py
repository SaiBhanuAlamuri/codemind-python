def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return True
    else:
        return False
            
    

n=int(input())
arr=list(map(int,input().split()))
pr=[]
np=[]
fact1=1
fact2=1
for i in range(n):
    if(prime(arr[i]) == True):
        pr.append(arr[i])
    else:
        np.append(arr[i])
for i in pr:
    fact1=fact1*i
for i in np:
    fact2=fact2*i
print(abs(fact1-fact2))