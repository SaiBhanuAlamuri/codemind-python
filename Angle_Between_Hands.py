n=input()
h=int(n[0:2])
m=int(n[3:5])
if(m%2==0):
    a=30*h*1.0-11*m/2
    if a<0:
        a=a+360
    if a>180:
        a=360-a
    print("%0.1f"%a)
else:
    a=30*h*1.0-5.5*m
    if a<0:
        a=a+360
    if a>180:
        a=360-a
    print("%0.1f"%a)
    