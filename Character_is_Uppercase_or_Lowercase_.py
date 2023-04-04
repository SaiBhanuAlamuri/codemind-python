ch=str(input())
if(ord(ch)>=ord('A') and ord(ch)<=ord('Z')):
    print("uppercase alphabet")
elif(ord(ch)>=ord('a') and ord(ch)<=ord('z')):
    print("lowercase alphabet")
else:
    print("not an alphabet")