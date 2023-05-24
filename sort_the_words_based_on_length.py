def some(n):
    s=0
    for i in n:
        s=s+ord(i)
    return s

n=input()
a=list(n.split())
for i in range(len(a)-1):
        if(len(a[i])>len(a[i+1])):
            a[i],a[i+1]=a[i+1],a[i]
        if(len(a[i])==len(a[i+1])):
             if(some(a[i])>some(a[i+1])):
                 a[i],a[i+1]=a[i+1],a[i]
for i in a:
    print(i,end=" ")
            
