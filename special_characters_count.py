n=input()
c=0
for i in range(len(n)):
    if(ord(n[i])>=97 and ord(n[i])<=122):
        c=c+0
    elif(ord(n[i])>=65 and ord(n[i])<=90):
        c=c+0
    elif(ord(n[i])==32):
        c=c+0
    else:
        c=c+1
print(c)