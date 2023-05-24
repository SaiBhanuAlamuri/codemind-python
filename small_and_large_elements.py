n=input()
a=list(n.split())
mi=a[0][0]
ma=a[len(a)-1][0]
for i in a[0]:
    if(ord(i)<ord(mi)):
            mi=i
for i in a[len(a)-1]:
    if(ord(i)>ord(ma)):
        ma=i
print(mi,ma)
