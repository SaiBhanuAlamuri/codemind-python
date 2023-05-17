def rev(n):
    r=0
    re=0
    while(n!=0):
        r=n%10
        re=re*10+r
        n=n//10
    return re
n=int(input())
sq=n*n
r=rev(n)
p=r*r
q=rev(p)
if(q==sq):
    print("True")
else:
    print("False")

    