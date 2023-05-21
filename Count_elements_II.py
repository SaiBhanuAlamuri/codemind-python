n,m=map(int,input().split())
fs=list(map(int,input().split()))
ss=list(map(int,input().split()))
c=0
s=0
dic1={}
dic2={}
for i in fs:
    if( i in dic1):
        dic1[i]=dic1[i]+1
    else:
        dic1[i]=1
for i in ss:
    if( i in dic2):
        dic2[i]=dic2[i]+1
    else:
        dic2[i]=1
for k,v in dic1.items():
    if(k not in ss):
        c=c+1
for k,v in dic2.items():
    if(k not in fs):
        s=s+1
    
a=s+c
print(a)
