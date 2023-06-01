hf,sp,s=map(int,input().split())
if(hf>=50 and sp>=60 and s>=100):
    print(10)
elif(hf>=50 and sp>=60 and s<=100):
    print(9)
elif(sp>=60 and s>=100 and hf<=50):
    print(8)
elif(hf>=50 and sp<=60 and s>=100):
    print(7)
elif(hf<=50 and sp<=60 and s<=100):
    print(5)
else:
    if hf>=50 or sp>=60 or s>=100:
        print(6)

    
        
    