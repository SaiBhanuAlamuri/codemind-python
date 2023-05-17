n=int(input())
ls=list(map(int,input().split()))
dic={}
for i in ls:
    if(i in dic.keys()):
        dic[i]+=1
    else:
        dic[i]=1
for k,v in dic.items():
    print(k,end=" ")