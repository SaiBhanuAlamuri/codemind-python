n=input()
c=0
for i in range(len(n)):
    if(ord(n[i])>=97 and ord(n[i])<=122):
        c=c+1
print(c)