a=input()
mi=ma=a[0]
for i in a:
    if(i.islower() or i.isupper()):
        if(ord(mi)>ord(i)):
            mi=i
        if(ord(ma)<ord(i)):
            ma=i
n=m=0
for i in a:
    if(i==mi):
        n=n+1
    if(i==ma):
        m=m+1
print(mi,n,ma,m)