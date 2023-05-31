import math
a=int(input())
b=int(input())
h=pow((a*a+b*b),0.5)
h=h/2
a=a/2
ang=round(math.degrees(math.acos(a/h)))
print(ang)
