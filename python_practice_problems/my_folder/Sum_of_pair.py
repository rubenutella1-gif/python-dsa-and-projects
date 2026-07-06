array=[10,22,30,1,3,23,2,7]
sum=24
seen=set()
for i in array:
    complement=sum-i
    if complement in seen:
        print(f"pair is {complement},{i}")
    seen.add(i)