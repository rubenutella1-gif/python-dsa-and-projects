name1=input("Enter your first name :").lower()
name2=input("Enter second name :").lower()
name1=name1.replace(" ","")
name2=name2.replace(" ","")
samechar=[]
remain=[]
for i in name1:
    for j in name2:
        if i==j:
            samechar.append(i)
            samechar.append(j)
        if i!=j:
            remain.append(i)
            remain.append(j)
samechar=list(set(samechar))
remain=list(set(remain))
print(samechar)
print(remain)