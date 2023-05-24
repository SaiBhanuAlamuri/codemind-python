n=input()
a=list(n.split())
for i in a:
    mi=i[0]
    ma=i[0]
    for j in i:
        if(ord(j)>ord(ma)):
            ma=j
        if(ord(j)<ord(mi)):
            mi=j
    print(mi,ma,end=" ")
