a=input()
ar=[]
for i in a:
    if i.isspace():
        continue
    else:
        if i.upper() not in ar and i.lower() not in ar:
            ar.append(i)
print(len(ar))
   
