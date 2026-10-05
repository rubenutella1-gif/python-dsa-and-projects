l1=[1,2,3,2,43,2,45,22,43,1,4,2,24,42,33,42]
mp={}
duplicates=[]
for i in l1:
        mp[i]=mp.get(i,0)+1
print(mp)
for i in mp:
    if mp[i]>1:
            duplicates.append(i)
print(duplicates)