d={1:22,2:"Ramesh",'add':"nandigama"}
print(type(d))
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d.get(1))
print(d.update({111:"hello"}))
print(d)
for i in {1:22,2:"Ramesh",'add':"nandigama"}.keys():
    print(i)
