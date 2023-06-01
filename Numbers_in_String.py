a=input()
s=0
for i in a:
    if i.isdigit():
        s=s+ord(i)-48
print(s)