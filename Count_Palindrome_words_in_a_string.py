def pal(s):
    a=""
    flag=0
    for i in s:
        if i.isupper():
            a=a+i.lower()
        else:
            a=a+i
    if rev(a)==a:
        flag=1
    return flag
def rev(s):
    return s[::-1]
ls=list(map(str,input().split()))
c=0
for i in ls:
     if(pal(i)==1):
        c=c+1
print(c)
    