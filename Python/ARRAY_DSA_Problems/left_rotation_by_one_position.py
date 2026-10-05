l=[1,2,3,4,5]
first=l[0]
for i in range(1,len(l)):
    l[i-1]=l[i]
l[-1]=first
print(l)