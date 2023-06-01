ar=input()
s=input()
dic={}
c=0
for i in ar:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
for k,v in dic.items():
    if k==s:
        c=1
        print(dic[k])
        break
if(c==0):
    print("-1")