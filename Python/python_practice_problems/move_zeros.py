# Move Zeros to the End of the List
""" lst1=[0, 1, 0, 3, 12]
lst2=[]
lst3=[]
for i in lst1:
    if i!=0:
        lst2.append(i)
    else:
        lst3.append(i)
        
lst4=lst2+lst3
print(lst1)
print(lst4) """
lst1=[0, 1, 0, 3, 12]
j=0
for i in range(len(lst1)):
    if lst1[i]!=0:
        lst1[j],lst1[i+1]=lst1[i],lst1[j]
print(lst1)