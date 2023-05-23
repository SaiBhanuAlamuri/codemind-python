n=input()
vow="aeiou"
f=0
for i in vow:
    if i in n:
        f=1
    else:
        f=0
        break
if(f==1):
    print("True")
else:
    print("False")