def rev(n):
        r=0
        rev=0
        while(n!=0):
            r=n%10
            rev=rev*10+r
            n=n//10
        return rev
def pal(n):
        r=0
        rev=0
        f=0
        x=n
        while(n!=0):
            r=n%10
            rev=rev*10+r
            n=n//10
        if(x==rev):
            f=1
        return f
        
        
def main(n):
    while(1):
        n=n+rev(n)
        if(pal(n)==1):
            break
        else:
            continue
    return n
        
        
n=int(input())
res=main(n)
print(res)
            