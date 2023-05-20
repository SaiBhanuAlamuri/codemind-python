n=int(input())
l=list(map(int,input().split()))
dic={}
for i in l:
    if i in dic:
        dic[i]=dic[i]+1
        
    else:
        dic[i]=1
for k,v in dic.items():
    print(k,end=" ")