l1=[1,-2,3,-4,5,-6]
""" result=[]
l2=[]
l3=[]
for i in l1:
    if i<0:
        l2.append(i)
    else:
        l3.append(i)
print(l2+l3) """
""" positive=[x for x in l1 if x>=0]
negetive=[x for x in l1 if x<0]
result=positive+negetive
print(result) """
""" result=[]
for x in l1:
    if x>=0:
        result.append(x)
for x in l1:
    if x<0:
        result.append(x)
print(result) """
j=0
for i in l1:
    if i<0:
        l1[j]=i
        j+=1
for i in l1:
    if i>=0:
        l1[j]=i
        j+=1
print(l1)