n=int(input())
x=n
r=0
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
if x==rev:
    print("True")
else:
    print("False")