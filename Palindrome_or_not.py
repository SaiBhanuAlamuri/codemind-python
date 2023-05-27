s=input()
a=""
for i in s:
    if i.isupper():
        a=a+i.lower()
    else:
        a=a+i
if(a[::-1]==a):
    print("True")
else:
    print("False")
        