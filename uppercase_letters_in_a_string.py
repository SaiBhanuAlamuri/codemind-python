n=input()
c=0
for i in range(len(n)):
    if(ord(n[i])>=65 and ord(n[i])<=90):
        c=c+1
print(c)
